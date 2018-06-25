#
# Audit feature to get Alexa to announce HA states for :
#
#    Inside Temperature 
#    Outside Temperature 
#    Lights
#    Switches
#    Batteries
#
# Program requires the following parameters
#
#    Title: Name Alexa announces eg Living room Audit
#    Trigger: Switch to trigger program 
#    Notify: Name of Alexa Notify service
#    Temp-Inside: Name of sensor
#    Temp-Outside: Name of sensor
#    Light: list of lights
#    Switch: List of switches
#    battery: list of sensors with battery levels
#
# Title,Trigger and Notify parameters are mandatory, other parameters that not required must be set to none    
#
# Example config 
#
# AuditAlexa:
# module: AuditAlexa
# class: Auditalexa
# title: "Living Room Audit"
# trigger: "input_boolean.audit_light"
# notify: "alexalr"
# temp-inside: "sensor.temperature_158d0001b9205b"
# temp-outside: "sensor.dark_sky_temperature"
# light:
#  - light.living_room_lights
#  - light.dining_room_lights
#  - light.gateway_light_34ce0081452d
# switch:
#  - switch.onoff_sonoff1
#  - switch.onoff_sonoff2
# battery:
#  - none
#
#
import appdaemon.plugins.hass.hassapi as hass
class Auditalexa(hass.Hass):
    def initialize(self):
# get vars
        self.trigger=self.args["trigger"]
        self.alexa = self.args["notify"]
# check if trigger switch triggered
        self.listen_state(self.auditalexa,self.trigger,new="on")
    def auditalexa (self, entity, attribute, old, new, kwargs):
# get vars 
        title=self.args["title"]
        it = self.args["temp-inside"]
        ot = self.args["temp-outside"]
# check if vars exist or set to none
        if it == "none" :
            it = ""
        if ot == "none" :
            ot = ""
# replace . with word "point" and add the word "degrees" so alexa temperature correctly
        if it != "" :
            it = "Inside temperature is " + self.get_state(it) + " degrees"
            it = it.replace("."," point ")
        if ot != "" :
            ot = "Outside temperture is " + self.get_state(ot) + " degrees"
            ot = ot.replace("."," point ")
#setup lists for Lights (li) switches (sw) and batteries (bt) 
        li = []
        sw = []
        bt = []
#get friendly name and state from device and add to list
        for entity in self.args["light"]:
# if var set to none skip and append none to list
            if entity != "none" :
                li.append(self.friendly_name(entity) + " " + self.get_state(entity))
            else :
                li.apend("none")
#get friendly name and state from device and add to list                
        for entity in self.args["switch"]:
#if var set to none skip and append none to list
            if entity != "none" :
                sw.append(self.friendly_name(entity) + " " + self.get_state(entity))
            else :
                sw.append("none")
#get friendly name and state from device and add to list 
        for entity in self.args["battery"]:
#if var set to none skip and append none to list
            if entity != "none" :
                temp = self.friendly_name(entity) + " " + self.get_state(entity) + " persent charged"
# replace . for point to help alexa speak correctly
                temp = temp.replace("."," point ")
                bt.append(temp)
            else :
                battery.append("none")
#create  message for alexa to speak . add , to pause to speech 
        mess = title + "," + it + "," + ot + ","
# append message for lights
        for entity in li :
            if entity != "none" :
                mess = mess + entity + ","
# append message for switches
        for entity in sw :
            if entity != "none" :
                mess = mess + entity + ","
# append message for battries
        for entity in bt :
            if entity != "none" :
                mess = mess + entity + ","
#add closing message
        mess = mess + title + "completed"
# alexa notify unable to work with white spaces repalce spaces with _        
        mess = mess.replace(" ","_")
# send notify to alexa 
        self.notify(mess,name = self.alexa)    
# turn off trigger switch
        self.turn_off(self.trigger) 
