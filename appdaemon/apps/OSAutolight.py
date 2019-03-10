# Turns porch light on after sunset
# Turns porch light off after midnight
#
import appdaemon.plugins.hass.hassapi as hass
import datetime
class OSautolight(hass.Hass):
    def initialize(self):
<<<<<<< HEAD
=======
        time = datetime.time(22, 59, 59)
>>>>>>> f4b966840133ddbf4c76aeb6ec8ee6e1df7554e9
        self.run_at_sunset(self.osautolight)
        self.run_at_sunrise(self.osautolight_off)
    def osautolight (self, kwargs):
        if self.get_state("sensor.allhome") != "true" :
            self.log("Auto Outside light off")
            self.turn_on("light.outside_light")
    def osautolight_off (self, kwargs):
        self.log("Auto Outside light off")
        self.turn_off("light.outside_light")
