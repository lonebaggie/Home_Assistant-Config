import appdaemon.plugins.hass.hassapi as hass
class LRtradfri(hass.Hass):
    def initialize(self):
        self.listen_state(self.lrtradfri,"light.all_living_room_lights",duration = 10)
    def lrtradfri (self, entity, attribute, old, new, kwargs):
        if new == "off" :
            self.select_option("input_select.light_state", "Off")
        if new == "on" and self.get_state("input_select.light_state") == "Off" :
            br = self.get_state(entity,attribute="brightness")
            if br == 25 :
                self.select_option("input_select.light_state", "Dark")
            if br == 203 :
                self.select_option("input_select.light_state", "Relaxed")
            if br == 254 :
                self.select_option("input_select.light_state", "Bright")
                
                
            