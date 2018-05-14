import appdaemon.plugins.hass.hassapi as hass
class HRswitch(hass.Hass):
    def initialize(self):
        self.listen_event(self.hrswitch, "click", entity_id = "binary_sensor.wall_switch_right_158d00017110b8", click_type = "single")
        self.listen_event(self.lrswitch, "click", entity_id = "binary_sensor.wall_switch_left_158d00017110b8", click_type = "single")
    def hrswitch(self,event_name, data, kwargs):
        self.toggle("switch.wall_switch_left_158d0001a21f31")
    def lrswitch(self,event_name, data, kwargs):
        self.toggle("switch.wall_switch_right_158d0001a21f31")