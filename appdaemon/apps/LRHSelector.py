# Use Input select  to trigger Harmony Remote. If triggered by remote
# or Alexa ensure input select not triggered twice
import appdaemon.plugins.hass.hassapi as hass
class LRhselector(hass.Hass):
    def initialize(self):
        self.listen_state(self.lrhselect,"input_select.harmony_state")
    def lrhselect (self, entity, attribute, old, new, kwargs):
# get current harmony state
        hr = self.get_state("sensor.harmony")
        self.log("Harmony remote triggered")
# if triggered  input select state not match current stare trigger
        if new == "PowerOff" and hr != "PowerOff" :
            self.log("PowerOff Triggered")
            self.call_service("remote/turn_off",entity_id="remote.harmony_hub")
        elif new != hr:
            self.log("{} Triggered".format(new))
            self.call_service("remote/turn_on", entity_id = "remote.harmony_hub", activity = new) 
          
            
            
        
            