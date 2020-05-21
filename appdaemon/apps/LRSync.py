# Program to sync Tradfri lights to Physical switch 
import appdaemon.plugins.hass.hassapi as hass
class LRsync(hass.Hass):
    def initialize(self):
        self.listen_state(self.lrsync,"light.living_room", new = "off", duration = 30)
    def lrsync(self, entity, attribute, old, new, kwargs):
        lr =self.get_state("switch.living_room")
        if lr == "on" :
            self.log("Living room switch is synced off")
            self.turn_off("switch.living_room")
        if lr == "off" :
            self.log("Force tradfri light unavailable")
            self.toggle("light.living_room")
            self.toggle("light.living_room")
            self.toggle("light.living_room")
            self.toggle("light.living_room")
            self.toggle("light.living_room")
            self.toggle("light.living_room")