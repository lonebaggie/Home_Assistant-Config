# if everyone is home turn off outside light
import appdaemon.plugins.hass.hassapi as hass
class HAway(hass.Hass):
    def initialize(self):
        self.listen_state(self.haway,"sensor.allhome")
    def haway (self, entity, attribute, old, new, kwargs):
        if new == "true" :
            self.log("All home turn off Outside light")
            self.turn_off("light.outside_light")