# Program to sync Tradfri lights to Physical switch 
import appdaemon.plugins.hass.hassapi as hass
class LRswitch(hass.Hass):
    def initialize(self):
        self.listen_state(self.lrswitch,"switch.living_room")
    def iselect(self,kwargs) :
        lr = self.get_state("input_select.light_state")
        if lr == "Off" or lr == "Unknown" :
            lr = "Relaxed"
        self.select_option("input_select.light_state","Unknown")
        self.select_option("input_select.light_state",lr)
        self.log("Room Mode synced to {}".format(lr))
    def lrswitch(self, entity, attribute, old, new, kwargs): 
        self.lrm = self.get_state("input_select.light_state")
        if new == "off" :
            self.log("Living room off")
            self.select_option("input_select.light_state","Off")
# force LRsync to make tradfri unavailable
            self.turn_on("light.living_room")
        if new == "on" :
            self.log("Living room on")
            self.h1= self.run_in(self.iselect,30)
            
            
            