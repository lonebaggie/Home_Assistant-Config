#
# Turns porch light on if motion detected and is dark
# After 2mins turns light off
#
import appdaemon.plugins.hass.hassapi as hass
class OSautolight(hass.Hass):
    def initialize(self):
        self.listen_state(self.osautolight,"binary_sensor.motion_sensor_158d0001e43e18")
    def osautolight (self, entity, attribute, old, new, kwargs):
        if self.sun_down() and self.get_state("input_boolean.ms3") == "on":
            self.turn_on("switch.wall_switch_158d0001614701")
            self.run_in(self.light_off, 120)
    def light_off(self, kwargs):
        self.turn_off("switch.wall_switch_158d0001614701")
    