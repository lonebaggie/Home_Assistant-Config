import appdaemon.plugins.hass.hassapi as hass
class Harmonyselect(hass.Hass):
    def initialize(self):
        self.listen_state(self.harmonyselect,"remote.harmony_hub",attribute="current_activity")
    def harmonyselect (self, entity, attribute, old, new, kwargs):
        if self.get_state("input_select.harmony_state") != new :
            self.log("Harmony Triggered")
            self.select_option("input_select.harmony_state",new)
        
        