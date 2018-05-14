import appdaemon.plugins.hass.hassapi as hass
class LRtradfri(hass.Hass):
    def initialize(self):
        self.listen_state(self.lrtradfri,"group.gikea",duration = 2)
    def lrtradfri (self, entity, attribute, old, new, kwargs):
        if new == "off" :
            self.select_option("input_select.light_state","Off")
        if new == "on" :
            self.select_option("input_select.light_state","Bright")
            