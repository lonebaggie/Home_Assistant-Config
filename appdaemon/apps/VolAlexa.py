# change volume of alexa via input number on UI
import appdaemon.plugins.hass.hassapi as hass
class Volalexa(hass.Hass):
    def initialize(self):
        self.listen_state(self.volalexa,"input_number.alexa_volume")
    def volalexa (self, entity, attribute, old, new, kwargs):
        alexa = self.get_state("input_select.alexa_state").lower()
        if alexa == "all" :
            alexa = "group.gallalexa"
        else:
            alexa = "media_player." + alexa
        self.log("TTS volume for {} is {}".format(alexa,new))
        self.call_service("media_player/volume_set",entity_id=alexa,volume_level=new)