# Program to sync Tradfri lights to Physical switch
import appdaemon.plugins.hass.hassapi as hass
class LRswitch(hass.Hass):
    def initialize(self):
        self.listen_state(self.lrswitch,"switch.wall_switch_158d00016cf4bc")
    def lrswitch(self, entity, attribute, old, new, kwargs):
        if new == "on" :
            self.run_in(self.relaxedon,45)
            self.log("Living Room Light on ")
        if new == "off" :
            self.select_option("input_select.light_state","Off")
            self.log("Living Room Light Off")
    def relaxedon(self,kwargs):
        self.log("Relaxed Triggered")
        self.select_option("input_select.light_state","Relaxed")
        

            
            
            
      

        
            
        
        
        
        
        
        