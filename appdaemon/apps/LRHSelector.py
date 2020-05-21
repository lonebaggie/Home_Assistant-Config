# Use Input select  to trigger Harmony Remote. If triggered by remote
# or Alexa ensure input select not triggered twice
import appdaemon.plugins.hass.hassapi as hass
class LRhselector(hass.Hass):
    def initialize(self):
        self.listen_state(self.lrhselect,"input_select.harmony_state")
    def lrhselect (self, entity, attribute, old, new, kwargs):
        self.log("{} Triggered".format(new))
        if self.get_state("sensor.harmony") != new :
            self.log("{} service called".format(new))
            self.call_service("remote/turn_on",entity_id = "remote.harmony_hub", activity = new) 