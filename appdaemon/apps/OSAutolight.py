import appdaemon.plugins.hass.hassapi as hass
class OSautolight(hass.Hass):
    def initialize(self):
        self.listen_state(self.osautolight,"sensor.outside_motion_sensor_battery")
    def osautolight (self, entity, attribute, old, new, kwargs):
        if sun_down() :
            self.turn_on("switch.wall_switch_158d0001614701")
            self.run_in(self.light_off, 120)
    def light_off(self, kwargs):
        self.turn_off("switch.wall_switch_158d0001614701")
    