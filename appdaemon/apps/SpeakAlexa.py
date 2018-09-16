import appdaemon.plugins.hass.hassapi as hass
class Speakalexa(hass.Hass):
    def initialize(self):
        self.listen_state(self.speakalexa,"input_text.tts")
    def speakalexa (self, entity, attribute, old, new, kwargs):
        talk = self.get_state("input_text.tts")
        alexa = self.get_state("input_select.alexa_state").lower()
        alexa = "media_player." + alexa
        if talk != "" :
            self.log("TTS Called")
            self.log(alexa)
            self.call_service("media_player/alexa_tts",entity_id=alexa,message=talk)