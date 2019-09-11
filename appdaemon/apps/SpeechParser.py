# Speech Parser
#
# Ver 1.0 
#
# Ver 1.1 Update Parse for removing dot from float numbers ensure did not replace full stops
#
# ver 1.2 remove : from final parse
#
# ver 2.0 added translate option
#
# This program extracts information from entities  and converts them into a readable format
# for devices such as Alexa or google assistant to read.
# The program is triggered by a dummy bulb which can be then be presented to Alexa or Google.
# Depending on the brightness level { 1 to 100}  triggered this program will parse a command line
# to extract the required information. 

#SpeechParser:
#  module: SpeechParser
#  class: Speechparser
#  trigger: "light.alexa_virtual"
#  DEBUG: 1
#  entities:
#    1:binary_sensor.door_window_sensor_158d00019e18bf # front door sensor
#    2: sensor.temperature_158d0001b9205b # living room thermostat
#    3: group.gupstairs # upstairs lights
#    4: binary_sensor.door_window_sensor_158d00019e1738 # patio door sensor
#    5: weather.dark_sky # weather
#  messages:
#    1: "The {$01=FN} is {$01=ST|off|closed}{$01=ST|on|open}""
#    2: "The {$02=FN} is currently {$02=ST} centigrade"
#    3: "The {$03=FN} are currently {$03=ST}"
#    4: "The {$04=FN}{$04=ST|on|are open,please close now"}{$04=ST|off|closed}"
#    5: >
#        {g} on {d} the {D} of {m} {y} at {t} the current outside  temperature is {$05=TP}
#        degrees winspeed is {$05=wind_speed} miles per hour
#    6: "{$02>state|18|temperature too high}{$02<state|19|temperature too low}
#  translate:
#    1: morning|morgan
#
# Each parameter of the message list matches the brightness level of the dummy bulb so 1st  parameter is 1% and so on 
# Information inside {} is used to extract information from HA text outside of the brackets is unaltered.
# use yaml > to break down long message lines 
#
# The entities list is indexed from 1 to 99 and is used by the ${state} command to extract data. 
# Use the # to add comments to each entity to help identify objects.
# 
# The following commands can be used :
# 
# d = current day in spoken format {31st}
# D = current day in name {Monday}
# m = current month in words {April}
# y = current year  {2018}
# t = current time (12h) split so correctly spoken { 11 24 PM}
# g = Greeting based on current time [morning:afternoon:evening]
#
# The $ command has  additional parameters that are order dependent
# 
# {$} State
#
# $[00-99][=|>|<][attrib]|[test value|replace value [$[00-99]= attrib] [+] [-] [1] [2] ] 
#
# $                 state command
# 00-99             number matches entities from apps.yaml
# =                 show value to replace if value to test = value to replace
# >                 show value to replace if value to test > value to replace
# <                 show value if replace if value to test < value to replace
# attrib            state name in HA can be shorten see shortcuts in code
# |                 seperator  
# test value        alpha or if using < > must be numeric 
# |                 seperator
# replace value     alpha or numeric. can be another state command [1] will display
#                   test value. [2] will diplay replace value  [+] sum the values
#                   [-] will subtract always display positive number 
#
# The translate list (this is optional) is global search and replace . 
# It will replace any text in the final parse it has the following format
# 
# 1:source|replace
# 2:source|replace
# 
# any text before the | will be replaced with text after the | .  
#
# Examples 
#
#  "The {$01=friendly_name} is {$01=state} degrees"
# 
#   This will parse to "The living room temperature is 17 point 2 degrees" 
#
# This can be further shorted by using the following shortcuts
#
#   ST = state
#   FN = friendly_name
#   TP = temperature
#   BR = brightness
#
#   "The {$01=FN} is {$01=ST} degrees"
#
#   State values can be changed
#  
#  "The {$01=FN} is {$01=ST|on|open}{$01=ST|off|closed}
#
#  This will parse to  "The Patio door is closed"  {off being replaced by closed}
#  
#  "Good {g} {D} the {d} of  {m}  {y} at {t} the current outside  temperature is {$05=TP} degrees, winspeed is {$05=wind_speed} miles per hour"
#
#  This will parse to "Good morning on Thursday the Thirty first of October 2018 at 11 52 AM the current outside temperature is 3 point 2 degrees, wind speed is 1 point 4 miles per      # hour "
#
#  "{$05>ST|15|temperature too high}"
# 
#  This will parse to "Temperature too high" if temp is greater than 15 or "” if temp is <= 15
#
#  "{$05<ST|10|temperature too low, current temperature is [1] degrees }"
#
#  This will parse to "Temperature too low, current temperature is 6.5 degress"
#  if temp is less than 10  or "” if temp is >= 10
#
#  "{$02>ST|$05=TP|Temperature is [1] degrees, [-] degrees higher than the outside temperature of [2] degrees}"
#
#  Temperature is 19.5 degrees, 5.5 degrees higher than the outside temperature  of 10 degrees
#
#  There is limited error checking. So if there are any errors or the program does not work as expected.
#  Set DEBUG: 1 . This should hightlight where the parsing errors occur. Normally misplaced brackets 
#  or commands in the wrong order
#

import appdaemon.plugins.hass.hassapi as hass
class Speechparser(hass.Hass):
    
    def initialize(self):
        self.trigger=self.args["trigger"]
        self.listen_state(self.speechparser,self.trigger,new="on")
    def debug(self, text):
        if self.args["DEBUG"] == 1:
            self.log(text)
    def remove_dot(self, text):
        import re
        p = re.findall("(\d+.\d)", text)
        for i in p :
            t = i.replace("."," point ")
            text = text.replace(i,t)
        return text
    
    def speechparser (self, entity, attribute, old, new, kwargs):
        import subprocess
        import re
        self.log("{} triggered".format(self.trigger))
################################################################################
# change these lines for your TTS system.                                      #
# This uses last_called in the alexa media player via a template sensor        #                   #
# if only using 1 device change TTS_Voice = entity_id of alexa to respond      #
################################################################################
        self.call_service("alexa_media/update_last_called")                    #
        TTS_voice = self.get_state("sensor.last_alexa")                        #
################################################################################        
        self.debug("{} is the talking echo".format(TTS_voice))
# setup vars
        sub_cmd = {"d":"","D":"","m":"","y":"","t":"","g":""}
        num2words = {1:'1st',2:'2nd',3:'3rd',4:'4th',5:'5th',6:'6th',7:'7th',8:'8th',9:'9th',10:'10th',\
                     11:'11th',12:'12th',13:'13th',14:'14th',15:'15th',16:'16th',17:'17th',18:'18th',19:'19th',\
                     20:'20th',21:'21st',22:'22nd',23:'23rd',24:'24th',25:'25th',26:'26th',27:'27th',28:'28th',\
                     29:'29th',30:'30th',31:'31st'}
# load sub_cmd with current date time values
        now = self.datetime() 
        yr = now.strftime("%Y")
        cen,dec = divmod(int(yr),100)
        dayn = (now.strftime("%d"))
        sub_cmd["d"] = now.strftime("%A")
        sub_cmd["D"] = num2words[int(dayn)]
        sub_cmd["m"] = now.strftime("%B")
        mn = now.strftime("%M")
        hour = now.strftime("%I")
        am_pm = now.strftime("%p")
        sub_cmd["y"] = str(cen) + str(dec)
        sub_cmd["t"] = hour + " " + mn + " " + am_pm
        hr = int(hour)
        if am_pm == "AM" :
            greeting = "morning"
        if am_pm == "PM" and hr >= 5 :
            greeting = "evening"
        else :
            greeting = "afternoon"
        sub_cmd["g"] = greeting
        self.debug("{}".format(sub_cmd))
# get dummy light brightness
        v = self.get_state(self.trigger, attribute = "brightness")
# error checking
        if v == None :
            self.debug("Invalid trigger value {}".format(v))
            self.turn_off(self.trigger)
            return
# convert brightness 0-255 to %
        value = round((v/255*100))
        self.debug("Trigger value= {}".format(value))
# load params from apps.yaml
        try :
            ent = self.args["entities"]
        except:
            self.debug("No entities  options")
            ent  = ""
        try :
            mess = self.args["messages"]
        except:
            self.debug("No message options")
            return
        try :
            tran = self.args["translate"]
        except:
            self.debug("No translate options")
            tran = ""
        self.debug("{} of Entities {}".format(len(ent),ent))
        self.debug(" {} of Messages {}".format(len(mess),mess))
        self.debug(" {} of Translates {}".format(len(tran),tran))
        self.debug("Trigger value (%) {} bulb brightness {}".format(value,v))
# error checking
        if value > len(mess) or value == 0 or value > 99  :
            self.debug("Invalid trigger value {}".format(value))
            self.turn_off(self.trigger)
            return 
# get message line
        parse = mess[value]
# error checking
        if parse.count("{") != parse.count("}"):
            self.debug("Mismatch of {}")
            self.turn_off(self.trigger)
            return 
# error checking
        if parse.count("[") != parse.count("]"):
            self.debug("Mismatch of []")
            self.turn_off(self.trigger)
            return 
################################################################################
# shortcuts add as required                                                    #
################################################################################
        parse = parse.replace("FN","friendly_name").replace("TP","temperature")
        parse = parse.replace("BR","brightness").replace("ST","state")         
        
        self.debug("parse data = {}".format(parse))
# extract three types of message commands simple {.} short {......}
# and extended {......|*|*} via regex
        simple = re.findall("({[a-zA-Z]})",parse)
        short = re.findall("({.[0-9][0-9].\w+})",parse)
        extend = re.findall("({.[0-9=><\w]+\|.+?\|.+?})",parse)
        self.debug("simple {}".format(simple))
        self.debug("short {}".format(short))
        self.debug("extend {}".format(extend))
# loop to extract {.} commands
        for i in simple :
            scmd = i[1]
            sval = sub_cmd[scmd]
            parse = parse.replace(i,sval)
            self.debug("simple parse= {}".format(parse))
# loop to extract short commands {......}
        for i in short :
# regex to split command 
            scmd = re.findall("{(\$)([0-9][0-9])(.)(\w+)}",i)
            self.debug("scmd = {}".format(scmd))
            ind = int(scmd[0][1])
            st = scmd[0][3]
            self.debug("ind {} state {}".format(ind,st))
# get state value from HA
            sval = str((self.get_state(ent[ind], attribute = st)))
            sval = self.remove_dot(sval)
            parse = parse.replace(i,sval)
            self.debug("short parse= {}".format(parse))
# loop to extract extended commands {......|*|*}
        for i in extend :
# regex to split command 
            scmd = re.findall("{(\$)([0-9][0-9])(.)(\w+)\|(.+)\|(.+)}",i)
            self.debug("scmd = {}".format(scmd))
            ind = int(scmd[0][1])
            op = scmd[0][2]
            st = scmd[0][3]
            s1 = scmd[0][4]
            s2 = scmd[0][5]
            self.debug("ind {} state {}".format(ind,st))
# get state value from HA
            sval = str((self.get_state(ent[ind], attribute = st)))
# check if extended value is state 
            if s1[0] == "$" :
                ind= int(s1[1:3])
                st = s1[4:]
                self.debug("ind1 {} state {}".format(ind,st))
# get state value from HA
                cval =  str(self.get_state(ent[ind], attribute =st))
            else:
                cval = s1
# replace [] values
            s2 = s2.replace("[1]",sval)
            s2 = s2.replace("[2]",cval)
# stop TTS saying "dot"
            s2 = self.remove_dot(s2)
            self.debug("ext output parse= {}".format(s2))
# test operators
            self.debug("input value = {} replace Value = {}".format(s1,s2))
            self.debug("operator is {}".format(op))
            if op == "=" :
                if sval == cval :
                    sval = s2
                else :
                    sval = ""
            if op == "<"  or op == ">":
                posv =round(abs(float(sval) - float(cval)),2)
                posv = str(posv)
                val = s1 + s2
                val = str(val)
                s2 = s2.replace("[-]",posv)
                s2 = s2.replace("[+]",val)
                if float(sval) < float(cval) :
                    s2 = self.remove_dot(s2)
                    sval = s2
                elif float(sval) > float(cval) :
                    s2 = self.remove_dot(s2)
                    sval = s2
                else :
                    sval = ""
# update parse
            parse = parse.replace(i,sval)
            self.debug("extended parse= {}".format(parse))
################################################################################
# this is the parsed message ready for reading.remove white spaces and :       #
################################################################################        
        parse = " ".join(parse.split())
        parse = parse.replace(":","")
# add any translations
        for i in tran :
            self.debug("translate {}".format(tran[i]))
            scmd = re.findall("[a-zA-Z ,]*",tran[i])
            self.debug("translate source {} replace with  {}".format(scmd[0],scmd[2]))
            parse = parse.replace(scmd[0],scmd[2])
        self.debug("Message {} for {} is {}".format(value,TTS_voice,parse))   
################################################################################
# this is the code for sending messagae via alexa_media notify                 #
# replace with notify or whenever command used                                 #
################################################################################
        self.call_service("notify/alexa_media",data={"type":"tts"},message=parse,target=TTS_voice)
# turn off trigger bulb
        self.turn_off(self.trigger)
