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
#  Varibale holds the default superset  of bulbs (6 bulbs) 
        ent = "light.all_living_room_lights"
        la = self.get_state(ent)
        lr = self.get_state("light.living_room_lights")
        dr = self.get_state("light.dining_room_lights")
# check to see if one subset of bulbs is on or off. If so changes the variable to the correct subset
        if lr == "on" and dr != "on" :
            ent = "light.living_room_lights"
        if lr != "on" and dr == "on" :
            ent = "light.dining_room_lights"
#check to sse which item of the item select has been selected
        if new == "Off" :
# resets item select and ensures all switches used by Alexa to change bulb state is off
            self.turn_off(ent)
            self.turn_off("input_boolean.dark")
            self.turn_off("input_boolean.relaxed")
            self.turn_off("input_boolean.bright")
        if new == "Dark" :
# Selects dark settings and applys to all bulbs or subset. Set switch on for Alexa 
            
            self.call_service("light/turn_on", entity_id = ent, brightness = 25, transition = 6 , color_temp = 450)
            self.turn_on("input_boolean.dark")
        if new == "Relaxed" :
# Selects dark settings and applys to all bulbs or subset. Set switch on for Alexa 
            self.log("relaxed triggered")
            self.call_service("light/turn_on", entity_id = ent, brightness = 203, transition = 6 , color_temp = 367)
            self.turn_on("input_boolean.relaxed")
        if new == "Bright" :
# Selects dark settings and applys to all bulbs or subset. Set switch on for Alexa 
            self.log("bright triggered")
            self.call_service("light/turn_on", entity_id = ent, brightness = 254, transition = 6 , color_temp = 250)
            self.turn_on("input_boolean.bright")    
            
        