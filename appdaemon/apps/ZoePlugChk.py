# Alexa warning of low temp Zoe charge
import appdaemon.plugins.hass.hassapi as hass
import datetime
class Zoeplugchk(hass.Hass):
    def initialize(self):
        runtime = datetime.time(21, 50, 0)
        handle = self.run_once(self.zoeplugchk, runtime)
    def zoeplugchk (self, kwargs):
        w0 = self.get_state("sensor.bad_weather")
        w8 = self.get_state("sensor.bad_weather_8")
        self.log("Zoe Checking temperature. Frost warning is {} and in 8 hours is {} ".format(w0,w8))
        if w0 != "clear" or w8 != "clear" :
            mess = "There is a frost warning for tomorrow morning, Do you need to Plug in Zoe ? "   
            self.log(mess)
            if self.get_state("device_tracker.simon_phone") == "home":
               self.call_service("notify/alexa_media",data={"type":"announce", "method":"all"},message=mess,target="group.gallalexa",title = "Zoe Low Temperature")