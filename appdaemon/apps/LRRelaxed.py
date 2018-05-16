import appdaemon.plugins.hass.hassapi as hass
class LRrelaxed(hass.Hass):
    def initialize(self):
        self.listen_state(self.lrrelaxed,"input_boolean.relaxed")
    def lrrelaxed (self, entity, attribute, old, new, kwargs):
        if new == "on" :
            if self.get_state("input_select.light_state") != "Relaxed" :
                self.select_option("input_select.light_state","Relaxed")
            self.turn_off("input_boolean.dark")
            self.turn_off("input_boolean.bright")
        if new == "off" and self.get_state("input_boolean.dark") == "off" and self.get_state("input_boolean.bright") == "off" :
            self.select_option("input_select.light_state","Off")