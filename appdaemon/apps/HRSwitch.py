#
# Repaced orginal Xiaoma Mihome automation. 
# Used to repace orginal analong two way switch. Switch is upstairs  and downstairs is wireless switch. 
# This program listens for left and right buton press and toggles Landing and hall switch
# Pressing both buttons turn on both lights or turns off both lights  
#

import appdaemon.plugins.hass.hassapi as hass
class HRswitch(hass.Hass):
    def initialize(self):
# Has wireless switch (left or right) button pressed
        self.listen_event(self.hrswitch, "xiaomi_aqara.click", entity_id = "binary_sensor.wall_switch_right_158d00017110b8", click_type = "single")
        self.listen_event(self.lrswitch, "xiaomi_aqara.click", entity_id = "binary_sensor.wall_switch_left_158d00017110b8", click_type = "single")
        self.listen_event(self.hrlrswitch, "xiaomi_aqara.click", entity_id = "binary_sensor.wall_switch_both_158d00017110b8", click_type = "both")
# hall light on or off
    def hrswitch(self,event_name, data, kwargs):
        self.toggle("light.hall_light")
# Landing light on or off
    def lrswitch(self,event_name, data, kwargs):
        self.toggle("light.landing_light")
# Landing light and Hall Light on or off cannot use toogle as need to sync both lights on or off.
    def hrlrswitch(self,event_name, data, kwargs):
        if self.get_state("light.hall_light") == "on" or self.get_state("light.landing_light") == "on" :
            self.turn_off("light.landing_light")
            self.turn_off("light.hall_light")
        else :
            self.turn_on("light.landing_light")
            self.turn_on("light.hall_light")
            