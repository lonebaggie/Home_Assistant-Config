#
# Program to allow teanage daughter to turn off lights without getting out of bed
#

import appdaemon.plugins.hass.hassapi as hass
class MRswitch(hass.Hass):
    def initialize(self):
        self.listen_event(self.mrswitch, "click", entity_id = "binary_sensor.switch_158d00018721c6", click_type = "single")
    def mrswitch(self,event_name, data, kwargs):
        self.toggle("switch.wall_switch_158d0001a2424b")