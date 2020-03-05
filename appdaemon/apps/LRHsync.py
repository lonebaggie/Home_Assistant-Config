# Sync Item Select when harmony remote triggered and ensure enigma and sony
# are in the correct state
import appdaemon.plugins.hass.hassapi as hass
class LRhsync(hass.Hass):
    def initialize(self):
        self.listen_state(self.lrhsync,"sensor.harmony")
    def lrhsync (self, entity, attribute, old, new, kwargs):
        self.log("Harmony Sensor {} triggered".format(new))
        self.select_option("input_select.harmony_state",new)
        sony = self.get_state("media_player.sony_htxt2")
        if new == "TV" :
            self.log("{} commands sent".format(new))
            self.log("enigma 2 on")
            self.call_service("media_player/turn_on",entity_id ="media_player.enigma_2")
        else:
            self.log("enigma 2 off")
            self.call_service("media_player/turn_off",entity_id ="media_player.enigma_2")
            
        if new == "PowerOff" :
            self.log("{} Triggered".format(new))
            if sony == "on" :
                self.log("Sony off")
                self.call_service("media_player/turn_off",entity_id ="media_player.sony_htxt2")
        else:
            if sony == "off" :
                self.log("Sony on")
                self.call_service("media_player/turn_on",entity_id ="media_player.sony_htxt2")
            

        
            