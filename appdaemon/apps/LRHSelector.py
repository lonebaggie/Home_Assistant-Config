import appdaemon.plugins.hass.hassapi as hass
class LRhselector(hass.Hass):
    def initialize(self):
        self.listen_state(self.lrhselect,"input_select.harmony_state")
    def lrhselect (self, entity, attribute, old, new, kwargs):
        hr = self.get_state("remote.harmony_hub", attribute="current activity")
        if new == "PowerOff" and hr != "PowerOff" :
            self.call_service("remote/turn_off",entity_id="remote.harmony_hub")
            self.turn_off("media_player.gigablue")
            self.turn_off("media_player.sony_htxt2")
        if new == "Roku" and hr != "Roku":
            self.call_service("remote/turn_on",entity_id="remote.harmony_hub",activity="30826655")
            self.turn_off("media_player.gigablue")
        if new == "LG" and hr != "LG":
            self.call_service("remote/turn_on",entity_id="remote.harmony_hub",activity="22125862")
            self.turn_off("media_player.gigablue")
        if new == "TV" and hr != "TV":
            self.call_service("remote/turn_on",entity_id="remote.harmony_hub",activity="25990763")
            self.turn_on("media_player.gigablue")
        if new == "Sony" and hr !="Sony" :
            self.call_service("remote/turn_on",entity_id="remote.harmony_hub",activity="22141284")
            self.turn_off("media_player.gigablue")
        if new == "Bluray" and hr != "Bluray":
            self.call_service("remote/turn_on",entity_id="remote.harmony_hub",activity="41594592")
            self.turn_on("media_player/media_player.sony_htxt2")
            self.turn_off("media_player.gigablue")
        if new == "Speaker" and hr != "Speaker" :
            self.call_service("remote/turn_on",entity_id="remote.harmony_hub",activity="22125718")
            self.turn_off("media_player.gigablue")
            
            
            
        
            