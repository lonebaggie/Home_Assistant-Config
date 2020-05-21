# Turn off Utility light if Kitchen light is turned off . 

import appdaemon.plugins.hass.hassapi as hass
class KUsync(hass.Hass):
    def initialize(self):
        self.listen_state(self.kusync,"light.kitchen",new="off")
    def kusync (self, entity, attribute, old, new, kwargs):
        if self.get_state("light.utility") == "on" :
            self.log("Kitchen light off Utility light off") 
            self.turn_off("light.utility")
            
        
            