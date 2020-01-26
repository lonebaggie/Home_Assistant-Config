#
# Allow teanage daughter to turn off lights without getting out of bed
#

import appdaemon.plugins.hass.hassapi as hass
class MRswitch(hass.Hass):
    def initialize(self):
        self.listen_event(self.mrswitch, "xiaomi_aqara.click", entity_id = "binary_sensor.switch_158d00018721c6", click_type = "single")
    def mrswitch(self,event_name, data, kwargs):
        self.toggle("light.maddy_light")