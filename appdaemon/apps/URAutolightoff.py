# Turn off Utility light if Kitchhen light turned off 
import appdaemon.plugins.hass.hassapi as hass
class URautolightoff(hass.Hass):
    def initialize(self):
        self.listen_state(self.urautolightoff,"switch.wall_switch_158d000159a94f",new="off")
    def urautolightoff (self, entity, attribute, old, new, kwargs):
        if self.get_state("switch.wall_switch_158d0001a68d54") == "on" :
            self.turn_off("switch.wall_switch_158d0001a68d54")
            
        
            