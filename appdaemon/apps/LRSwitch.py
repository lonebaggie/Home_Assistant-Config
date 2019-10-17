# Program to sync Tradfri lights to Physical switch
import appdaemon.plugins.hass.hassapi as hass
class LRswitch(hass.Hass):
    def initialize(self):
        self.listen_state(self.lrswitch,"switch.wall_switch_158d00016cf4bc")
    def lrswitch(self, entity, attribute, old, new, kwargs):
        if new == "on" :
# if switch turned on ensure light group is turn on .There is a bug if lights are turned off and on quickly group is still off so lights appear off
            self.turn_on("light.all_living_room_lights")
            self.log("Living Room Light on ")
            if self.get_state("sensor.lrsync") == "on" :
                self.log("lights are toggle too quickly for sync")
                self.talk_sync()
                
        if new == "off" :
# if switch is off . Turn off light group and ensure timer is turned off in case light switched toggled quickly 
            self.select_option("input_select.light_state","Off")
# ensure all lighs are toggled to force unavailable 
            self.toggle("light.living_room_lights")
            self.toggle("light.dining_room_lights")
            self.log("Living Room Light Off")
    def talk_sync(self):
        mess="Lights maybe in an inconsistant state, if so please switch off and wait 30 seconds before switching back on"
        self.call_service("notify/alexa_media",message=mess, data={"type":"announce", "method":"speak"}, target="media_player.lr_dot")