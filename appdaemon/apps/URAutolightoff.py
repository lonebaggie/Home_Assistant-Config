# Turn off Utility light if Kitchen light is turned off . 

import appdaemon.plugins.hass.hassapi as hass
class URautolightoff(hass.Hass):
    def initialize(self):
        self.listen_state(self.urautolightoff,"light.kitchen_light",new="off")
    def urautolightoff (self, entity, attribute, old, new, kwargs):
        if self.get_state("light.utility_light") == "on" :
            self.turn_off("light.utility_light")
            
        
            