# ensure input select living room lights are synced when HA restarts
import appdaemon.plugins.hass.hassapi as hass
class HAstart(hass.Hass):
    def initialize(self):
        self.listen_event(self.hastart, "plugin_started")
    def hastart(self,event_name, data, kwargs):
        self.log("HA restarted check light sync")
        if self.get_state("switch.living_room") == "on" :
            ls = self.get_state("input_select.light_state")
            if ls == "off" or ls == "Unknown" :
                self.log("Sync Lights to Unknown")
                self.select_option("input_select.light_state","Unknown")
        else :
            self.log("Sync dim levels  to off")
            self.select_option("input_select.light_state","Off")
            
        self.log("HA restarted check TV sync")
        harmony = self.get_state("sensor.harmony")
        if harmony != self.get_state("input_select.harmony_state") :
            self.log("Sync TV to {}".format(harmony))
            self.select_option("input_select.harmony_state", harmony)
            
            
            
            
            
            