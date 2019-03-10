# Turns porch light on after sunset
# Turns porch light off after midnight
#
import appdaemon.plugins.hass.hassapi as hass
import datetime
class OSautolight(hass.Hass):
    def initialize(self):
        self.run_at_sunset(self.osautolight)
        self.run_at_sunrise(self.osautolight_off)
    def osautolight (self, kwargs):
        if self.get_state("sensor.allhome") != "true" :
            self.log("Auto Outside light on")
            self.turn_on("light.outside_light")
    def osautolight_off (self, kwargs):
        self.log("Auto Outside light off")
        self.turn_off("light.outside_light")
