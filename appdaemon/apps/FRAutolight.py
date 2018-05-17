import appdaemon.plugins.hass.hassapi as hass
class FRautolight(hass.Hass):
    def initialize(self):
        self.listen_state(self.frautolight,"binary_sensor.motion_sensor_158d000187392e",new="on")
    def frautolight (self, entity, attribute, old, new, kwargs):
        if self.now_is_between("21:00:00", "06:00:00") and self.get_state("switch.wall_switch_158d0001828c33") == "off" :
            self.turn_on("switch.wall_switch_158d0001828c33")
            self.turn_on("switch.wall_switch_left_158d0001a21f31")
            self.turn_on("switch.wall_switch_158d00016cefdb")
            
