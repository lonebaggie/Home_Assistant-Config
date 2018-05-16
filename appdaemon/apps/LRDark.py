import appdaemon.plugins.hass.hassapi as hass
class LRdark(hass.Hass):
    def initialize(self):
        self.listen_state(self.lrdark,"input_boolean.dark")
    def lrdark (self, entity, attribute, old, new, kwargs):
        if new == "on" :
            if self.get_state("input_select.light_state") != "Dark" :
                self.select_option("input_select.light_state","Dark")
            self.turn_off("input_boolean.bright")
            self.turn_off("input_boolean.relaxed")
        if new == "off" and self.get_state("input_boolean.relaxed") == "off" and self.get_state("input_boolean.bright") == "off" :
            self.select_option("input_select.light_state","Off")