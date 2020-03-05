# Program to sync Tradfri lights to Physical switch 
import appdaemon.plugins.hass.hassapi as hass
class LRsync(hass.Hass):
    def initialize(self):
        self.listen_state(self.lrsync,"light.dinning_room")
        self.listen_state(self.lrsync,"light.living_room")
    def lrsync(self, entity, attribute, old, new, kwargs):
        na = self.get_state(entity,attribute="friendly_name")
        ls = self.get_state("switch.livingroom")
        self.log("{} triggered {}".format(na,new))
        if new == "on" and ls == "off" :
            self.log("Living room switch is off")
            self.turn_on("switch.livingroom")
            self.log("Living room switch is synced on")
        if new == "off" :
            dr = self.get_state("light.dinning_room")
            lr = self.get_state("light.living_room")
            if dr == "off" and lr == "off" and ls == "on" :
                self.log("Living room switch is on")
                self.turn_off("switch.livingroom")
                self.log("Living room switch is synced off")
                
            