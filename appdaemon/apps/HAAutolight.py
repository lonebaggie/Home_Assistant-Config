# If hall light on no need to have outside light on
import appdaemon.plugins.hass.hassapi as hass
class HAautolight(hass.Hass):
    def initialize(self):
# Trigger if hall light state changes
        self.listen_state(self.haautolight,"light.hall_light")
    def haautolight (self, entity, attribute, old, new, kwargs):
        self.log("Hall light triggered")
        if new == "on"  and self.get_state("light.outside_light") == "on" :
            self.turn_off("light.outside_light")
            self.log("Hall light on - Turn off Outside light")
        if new == "off" and self.sun_down() and self.get_state("light.outside_light") == "off" :
            self.log("Hall light off and after sunset turn on outside light")
            self.turn_on("light.outside_light")
            
            
        
    
