#
# This program actions an  Item select (Off Dark, Relaxed and bright ) on two set of Tradfri lights (living room and Dinning  3 in each set) 
#These bulbs are located  the same pysical room (open plan dining and living room)
# The program will  change  the brightness and colur temperture of both sets of lights or one set if the other set of bulbs is off.
#
#

import appdaemon.plugins.hass.hassapi as hass
class LRselector(hass.Hass):
    def initialize(self):
# Triggered if the superset of bulbs has changed state on or off
        self.listen_state(self.lrselect,"input_select.light_state")
    def lrselect (self, entity, attribute, old, new, kwargs):
#  Variable holds the default superset  of bulbs (6 bulbs) 
        self.ent = "light.all_living_room_lights"
        la = self.get_state(self.ent)
        lr = self.get_state("light.living_room_lights")
        dr = self.get_state("light.dining_room_lights")
# check to see if one subset of bulbs is on or off. If so changes the variable to the correct subset
        if lr == "on" and dr != "on" :
            self.ent = "light.living_room_lights"
        if lr != "on" and dr == "on" :
            self.ent = "light.dining_room_lights"
#check to sse which item of the item select has been selected
        if new == "Off" :
# resets item select and ensures all switches used by Alexa to change bulb state is off
            self.handle = self.run_in(self.delay_off,120)
            self.log("Delayed timer started")
            self.turn_off("light.all_living_room_lights")
            self.turn_off("input_boolean.dark")
            self.turn_off("input_boolean.relaxed")
            self.turn_off("input_boolean.bright")
# if switch is off no power to tradfri bulbs. Once power applied unstable for 60 seconds so delay selection util bulbs ready 
        if new != "Off" and self.get_state("switch.wall_switch_158d00016cf4bc") == "off" :
            self.turn_on("switch.wall_switch_158d00016cf4bc")
            self.log("switch triggered")
        if new == "Dark" :
# Selects dark settings and applys to all bulbs or subset. Set switch on for Alexa 
            if self.get_state("sensor.lrsync") == "on" :
                self.dark()
            else :
                self.log("talk sync")
                self.talk_sync()
            self.turn_on("input_boolean.dark")
        if new == "Relaxed" :
            if self.get_state("sensor.lrsync") == "on" :
                self.relaxed()
            else :
                self.log("talk sync")
                self.talk_sync()
            self.turn_on("input_boolean.relaxed")
# Selects relaxed settings and applys to all bulbs or subset. Set switch on for Alexa 
        if new == "Bright" :
            if self.get_state("sensor.lrsync") == "on" :
                self.bright()
            else :
                self.log("talk sync")
                self.talk_sync()
            self.turn_on("input_boolean.bright")
# Selects bright  settings and applys to all bulbs or subset. Set switch on for Alexa 

# routines to select bulbs warmth and brightness 
    def dark(self):
        self.call_service("light/turn_on", entity_id = self.ent, brightness = 25, transition = 6 , color_temp = 450)
        self.log("dark triggered")
    def relaxed(self):
        self.call_service("light/turn_on", entity_id = self.ent, brightness = 203, transition = 6 , color_temp = 367)
        self.log("relaxed triggered")
    def bright(self):
        self.call_service("light/turn_on", entity_id = self.ent, brightness = 254, transition = 6 , color_temp = 250)
        self.log("bright triggered")
    def talk_sync(self):
        self.call_service('media_player/alexa_tts', entity_id= "media_player.lr_dot", 
        message="Lights ar still syncronizing,please wait a moment before issuing further commands") 
    def delay_off(self, kwargs):    
        if self.get_state("light.all_living_room_lights") == "off" :
            self.turn_off("switch.wall_switch_158d00016cf4bc")
            self.toggle("light.all_living_room_lights")
            self.toggle("light.all_living_room_lights")
            self.toggle("light.all_living_room_lights")
            self.log("Trigger delay switch light off")
        else :
            self.log("Trigger delay switch cancelled")
            

    
    


  
        
