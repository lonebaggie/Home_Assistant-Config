import appdaemon.plugins.hass.hassapi as hass
class Tvsync(hass.Hass):
    def initialize(self):
        self.listen_state(self.tvsync,"media_player.lg_tv_remote")
    def tvsync(self, entity, attribute, old, new, kwargs):
        if new == "off" :
            self.turn_off("media_player.gigablue")
            self.call_service("media_player/select_source", entity_id = "media_player.living_room", source = "Home")
            self.log("TV sync Roku Off")
            self.log("TV sync Triggered Gigablue Off")
        if new == "playing" :
            if self.get_state("sensor.harmony") == "Gigablue" :
                self.turn_on("media_player.gigablue")
                self.log("TV sync Triggered Gigablue On")

            
