# Auto Zoe heat on in Winter
import appdaemon.plugins.hass.hassapi as hass
import datetime
class Zoeprecon(hass.Hass):
    def initialize(self):
        runtime = datetime.time(7, 30, 0)
        handle = self.run_once(self.zoeprecon, runtime)
    def zoeprecon (self, kwargs):
        self.log("Zoe Precon triggered")
        if self.get_state("sensor.zoe_plugged") == "True" :
            self.log("Zoe plugged in")
        
            w0 = self.get_state("sensor.bad_weather")
            if w0  == "snow" or w0 == "frost" :
                self.log("Frost Zoe Precon triggered" )
                self.turn_on("switch.zoe_precon")
            else :
                self.log("No frost NO Precon")
                
        else:
            self.log("Zoe not plugged in NO Precon")