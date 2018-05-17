#
# Grampy Aid turn lights when Gramp's get up at night via motion Sensor . Turns on lights to Aid Toilet time !
#

import appdaemon.plugins.hass.hassapi as hass
class FRautolight(hass.Hass):
    def initialize(self):
# Trigger if Motion detected
        self.listen_state(self.frautolight,"binary_sensor.motion_sensor_158d000187392e",new="on")
    def frautolight (self, entity, attribute, old, new, kwargs):
#Only turn on lights if already off and between set times
        if self.now_is_between("21:00:00", "06:00:00") and self.get_state("switch.wall_switch_158d0001828c33") == "off" :
#turn on lights
            self.turn_on("switch.wall_switch_158d0001828c33")
            self.turn_on("switch.wall_switch_left_158d0001a21f31")
            self.turn_on("switch.wall_switch_158d00016cefdb")
            
