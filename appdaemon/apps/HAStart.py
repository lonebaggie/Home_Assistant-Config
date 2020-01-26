# ensure input select living room lights are synced when HA restarts
import appdaemon.plugins.hass.hassapi as hass
class HAstart(hass.Hass):
    def initialize(self):
        self.listen_event(self.hastart, "plugin_started")
    def hastart(self,event_name, data, kwargs):
        self.log("HA restarted check light sync")
        if self.get_state("switch.wall_switch_158d00016cf4bc") == "on" :
            ls = self.get_state("input_select.light_state")
            if ls == "off" :
                self.log("Sync Lights to Relaxed")
                self.turn_on("input_boolean.relaxed")
            if ls == "Dark" :
                self.log("Sync Lights to Dark")
                self.turn_on("input_boolean.dark")
            if ls == "Relaxed" :
                self.log("Sync Lights to Relaxed")
                self.turn_on("input_boolean.relaxed")
            if ls == "Bright" :
                self.log("Sync Lights to Bright")
                self.turn_on("input_boolean.bright")
        else :
            self.log("Sync dim levels  to off")
            self.turn_off("input_boolean.bright")
            self.turn_off("input_boolean.relaxed")
            self.turn_off("input_boolean.dark")
            
            