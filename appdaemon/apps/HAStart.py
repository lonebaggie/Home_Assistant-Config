# ensure input select living room lights are synced when HA restarts
import appdaemon.plugins.hass.hassapi as hass
class HAstart(hass.Hass):
    def initialize(self):
        self.listen_event(self.hastart, "plugin_started")
    def hastart(self,event_name, data, kwargs):
        self.log("HA restarted check light sync")
        if self.get_state("switch.livingroom") == "on" :
            ls = self.get_state("input_select.light_state")
            if ls == "off" :
                self.log("Sync Lights to Unknown")
                self.select_option("input_select.light_state","Unknown")
        else :
            self.log("Sync dim levels  to off")
            self.select_option("input_select.light_state","Off")
            
            
            
            
            
            