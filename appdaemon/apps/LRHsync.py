# Sync Item Select when harmony remote triggered and ensure devices
# are in the correct state
import appdaemon.plugins.hass.hassapi as hass
class LRhsync(hass.Hass):
    def initialize(self):
        self.listen_state(self.lrhsync,"sensor.harmony")
    def lrhsync (self, entity, attribute, old, new, kwargs):
        self.log("Harmony Sensor {} triggered".format(new))
        self.select_option("input_select.harmony_state",new)
        if new == "PowerOff" :
            self.log("{} Triggered".format(new))
            self.turn_off("media_player.gigablue")
            self.turn_off("media_player.sony_htxt2")
            self.turn_off("media_player.living_room")
        if new == "Roku" :
            self.log("{} commands sent".format(new))
            self.turn_off("media_player.gigablue")
            self.turn_on("media_player.sony_htxt2")
        if new == "LG" :
            self.log("{} commands sent".format(new))
            self.turn_off("media_player.gigablue")
            self.turn_off("media_player.living_room")
        if new == "TV" :
            self.log("{} commands sent".format(new))
            self.turn_on("media_player.gigablue")
            self.turn_on("media_player.sony_htxt2")
            self.turn_off("media_player.living_room")
        if new == "Sony" :
            self.log("{} commands sent".format(new))
            self.turn_off("media_player.gigablue")
            self.turn_off("media_player.living_room")
        if new == "Bluray" :
            self.log("{} commands sent".format(new))
            self.turn_on("media_player.sony_htxt2")
            self.turn_off("media_player.gigablue")
            self.turn_off("media_player.living_room")
        if new == "Speaker" :
            self.log("{} commands sent".format(new))
            self.turn_off("media_player.gigablue")
            self.turn_off("media_player.living_room")