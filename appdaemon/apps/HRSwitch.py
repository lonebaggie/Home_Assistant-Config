#
# Repaced orginal Xiaoma Mihome automation. 
#Used to repace orginal analong two way switch. Switch is upstairs  and downstairs is wireless switch. 
# THis program listen for left and right buton press and toggles Landing and hall switch
#

import appdaemon.plugins.hass.hassapi as hass
class HRswitch(hass.Hass):
    def initialize(self):
# Has wireless switch (left or right) button pressed
        self.listen_event(self.hrswitch, "click", entity_id = "binary_sensor.wall_switch_right_158d00017110b8", click_type = "single")
        self.listen_event(self.lrswitch, "click", entity_id = "binary_sensor.wall_switch_left_158d00017110b8", click_type = "single")
# hall light on or off
    def hrswitch(self,event_name, data, kwargs):
        self.toggle("switch.wall_switch_left_158d0001a21f31")
# Landing light on or off
    def lrswitch(self,event_name, data, kwargs):
        self.toggle("switch.wall_switch_right_158d0001a21f31")