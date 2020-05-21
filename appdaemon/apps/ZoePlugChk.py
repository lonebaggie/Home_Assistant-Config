# Alexa warning of low temp Zoe charge
import appdaemon.plugins.hass.hassapi as hass
import datetime
class Zoeplugchk(hass.Hass):
    def initialize(self):
        runtime = datetime.time(21, 50, 0)
        handle = self.run_once(self.zoeplugchk, runtime)
    def zoeplugchk (self, kwargs):
        zch = self.get_state("sensor.zoe_battery")
        if zch < 20 :
            mess = "Zoe Checking Charge,  warning less than 20 percent remaining" 
            self.log(mess)
            if self.get_state("person.simon") == "Home" :
                self.call_service("notify/alexa_media",data={"type":"tts"},message=mess,target="media_player.lr_echo")
        if self.get_state("sensor.owm_temperature") < 2 :
            mess = "There is a frost warning for tomorrow morning, Do you need to Plug in Zoe ? "
            self.log(mess)
            if self.get_state("pesson.simon") == "Home" :
               self.call_service("notify/alexa_media",data={"type":"tts"},message=mess,target="media_player.lr_echo")