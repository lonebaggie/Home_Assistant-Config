# smtp and Alexa warning of failed zoe charge
import appdaemon.plugins.hass.hassapi as hass
class Zoestatus(hass.Hass):
    def initialize(self):
        self.listen_state(self.zoestatus,"sensor.zoe_charge",new="false")
    def zoestatus (self, entity, attribute, old, new, kwargs):
        mess= "Zoe has stopped charging at " + self.get_state("sensor.zoe_clevel") + " Percent"
        self.log(mess)
        if float(self.get_state("sensor.zoe_clevel")) < 90  and self.get_state("device_tracker.simon_phone") == "home":
            if self.now_is_between("22:30:00", "08:00:00"):
                self.log("As late attempt to restart Zoe Charge silently")
                self.turn_on("switch.zoe_charge")
            else :
             self.call_service("notify/alexa_media",data={"type":"announce", "method":"all"},message=mess,target="group.gallalexa",title = "Zoe Charge warning")