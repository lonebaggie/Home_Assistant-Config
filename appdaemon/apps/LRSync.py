# Program to sync Tradfri lights when power restored
import appdaemon.plugins.hass.hassapi as hass
class LRsync(hass.Hass):
    def initialize(self):
        self.handle = None
        self.listen_state(self.lrsync,"sensor.lrsync",new="on")
    def lrsync(self, entity, attribute, old, new, kwargs):
# ensure sync only triggered if previous state was unknown ie just turned on
        if old == "unknown" :
            self.log("sync triggered")
# if triggered by switch turned on,  default lights to relaxed 
# Also ensure Alexa is silent as not invoked by mood item select
            if self.get_state("input_select.light_state") == "Off" :
                self.select_option("input_select.light_state", "Relaxed")
# run delayed option from item select now lights are in sync
            if self.get_state("input_select.light_state") == "Dark":
                self.dark()
            if self.get_state("input_select.light_state") == "Relaxed" :
                self.relaxed()
            if self.get_state("input_select.light_state") == "Bright":
                self.bright()
# default setting for dark ,relaxed and bright 
    def dark(self):
        self.call_service("light/turn_on", entity_id = "light.all_living_room_lights", brightness = 25, transition = 6 , color_temp = 450)
        self.log("dark triggered")
    def relaxed(self):
        self.call_service("light/turn_on", entity_id = "light.all_living_room_lights", brightness = 203, transition = 6 , color_temp = 367)
        self.log("relaxed triggered")
    def bright(self):
        self.call_service("light/turn_on", entity_id = "light.all_living_room_lights", brightness = 254, transition = 6 , color_temp = 250)
        self.log("bright triggered")