# Program to sync Tradfri lights to Physical switch 
import appdaemon.plugins.hass.hassapi as hass
class LRswitch(hass.Hass):
    def initialize(self):
        self.listen_state(self.lrswitch,"switch.livingroom")
    def lrswitch(self, entity, attribute, old, new, kwargs): 
        lrm = self.get_state("input_select.light_state")
        if new == "off" :
            self.log("Living room off")
            self.turn_off("light.tradfri")
            self.select_option("input_select.light_state","Off")
        if new == "on" :
            self.log("Living room on")
            self.turn_on("light.tradfri")
            self.handle = self.run_in(self.delay_on,20)
    def delay_on(self,kwargs) :
        lrs = self.get_state("input_select.light_state")
        if lrs == "Off" or lrs == "Unknown" :
            lrs = "Relaxed"
        if self.get_state("switch.livingroom") == "on" :
            self.log("Set delayed room mood to {}".format(lrs))
            self.select_option("input_select.light_state","Unknown")
            self.select_option("input_select.light_state",lrs)
  