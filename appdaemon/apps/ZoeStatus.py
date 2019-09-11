# smtp and Alexa warning of failed zoe charge
import appdaemon.plugins.hass.hassapi as hass
class Zoestatus(hass.Hass):
    def initialize(self):
        self.listen_state(self.zoestatus,"sensor.zoe_charge",new="False")
    def zoestatus (self, entity, attribute, old, new, kwargs):
        mess= "Zoe has stopped charging at " + self.get_state("sensor.zoe_clevel") + " Percent"
        self.log(mess)
        if self.get_state("sensor.zoe_clevel") < 95  and self.get_state("device_tracker.simon_phone") == "home":
            self.call_service("notify/alexa_media",data={"type":"announce", "method":"all"},message=mess,target="group.gallalexa",title = "Zoe Charge warning")