# Program to sync Tradfri lights to Physical switch
import appdaemon.plugins.hass.hassapi as hass
class Alllights(hass.Hass):
    def initialize(self):
        self.listen_state(self.alllights,"light.all_living_room_lights",new="off")
    def alllights(self, entity, attribute, old, new, kwargs):
        self.select_option("input_select.light_state","Off")
        self.log("All Living Room Lights Off")
