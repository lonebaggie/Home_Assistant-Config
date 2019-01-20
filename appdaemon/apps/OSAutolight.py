#
# Turns porch light on if motion detected and is dark
# After 2mins turns light off
#
import appdaemon.plugins.hass.hassapi as hass
import datetime
class OSautolight(hass.Hass):
    def initialize(self):
        time = datetime.time(23, 59, 59)
        self.run_at_sunset(self.osautolight)
        self.run_daily(self.osautolightoff, time)
    def osautolight (self, kwargs):
        self.log("Auto Outside light on")
        self.turn_on("light.outside_light")
    def osautolightoff(self, kwargs):
        self.log("Auto Outside light off")
        self.turn_off("light.outside_light")
