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
            self.call_service("media_player/turn_on",entity_id ="media_player.enigma_2")
            self.log("Enigma 2 on")
            if sony == "off" :
                self.call_service("media_player/turn_on",entity_id ="media_player.sony_htxt2")
                self.log("Sony on")
            self.call_service("media_player/select_source",entity_id ="media_player.sony_htxt2", source = "TV")
        else:
            self.call_service("media_player/turn_off",entity_id ="media_player.enigma_2") 
            self.log("Enigma 2 off")
        if new == "Speaker" :
            if sony == "off" :
                self.call_service("media_player/turn_on", entity_id ="media_player.sony_htxt2")
                self.log("Sony on")
            self.call_service("media_player/select_source",entity_id ="media_player.sony_htxt2", source = "Bluetooth Audio")    
            self.log("Bluetooth on")
        if new == "Sony" :
            if sony == "off" :
                self.call_service("media_player/turn_on",entity_id ="media_player.sony_htxt2")
                self.log("Sony on")
        if new == "Radio" :
            if sony == "off" :
                self.call_service("media_player/turn_on", entity_id ="media_player.sony_htxt2")
                self.log("Sony on")
        if new == "PowerOff" :
            if sony == "on" :
                self.log("Sony off")
                self.call_service("media_player/turn_off", entity_id ="media_player.sony_htxt2")
            
          