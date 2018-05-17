# Used by Alexa to change brightness. Currently Aleax cannot manipulate Item Select which controls dim levels 
# of living room lights (Off, Dark , Relaxed and Bright)
# This program is one if three which allow Alexa to turn on and off the Dim Levels via standard off/on switches (boolean) 
# It ensure only one switch of the three (Dark, Relaxed and Bright) can be active at any time. AS once a switch is on 
# it cannot be turned on again. SWitches are exposed to Aleaxa via Home assistant cloud 
#
#

import appdaemon.plugins.hass.hassapi as hass
class LRbright(hass.Hass):
    def initialize(self):
        self.listen_state(self.lrbright,"input_boolean.bright")
    def lrbright (self, entity, attribute, old, new, kwargs):
        if new == "on" :
            if self.get_state("input_select.light_state") != "Bright" :
                self.select_option("input_select.light_state","Bright")
            self.turn_off("input_boolean.dark")
            self.turn_off("input_boolean.relaxed")
        if new == "off" and self.get_state("input_boolean.relaxed") == "off" and self.get_state("input_boolean.dark") == "off" :
            self.select_option("input_select.light_state","Off")