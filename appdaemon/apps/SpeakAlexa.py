import appdaemon.plugins.hass.hassapi as hass
class Speakalexa(hass.Hass):
    def initialize(self):
        self.listen_state(self.speakalexa,"input_text.alexa")
    def speakalexa (self, entity, attribute, old, new, kwargs):
        talk = self.get_state("input_text.alexa")
        if talk != "" :
            self.log("TTS Called")
            self.call_service("media_player/alexa_tts",entity_id="media_player.lr_dot",message=talk)