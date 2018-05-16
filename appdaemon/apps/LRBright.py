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