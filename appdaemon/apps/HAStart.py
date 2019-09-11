import appdaemon.plugins.hass.hassapi as hass
class HAstart(hass.Hass):
    def initialize(self):
        self.listen_event(self.hastart, "plugin_started")
    def hastart(self,event_name, data, kwargs):
        self.log("HA restarted check light sync")
        if self.get_state("switch.wall_switch_158d00016cf4bc") == "on" and self.get_state("input_select.light_state") == "off" :
            self.log("Sync Lights to Relaxed")
            self.select_option("input_select.light_state","Relaxed")
            