import appdaemon.plugins.hass.hassapi as hass
class Speakalexa(hass.Hass):
    def initialize(self):
        self.listen_state(self.speakalexa,"input_text.tts")
    def speakalexa (self, entity, attribute, old, new, kwargs):
        alexa = self.get_state("input_select.alexa_state").lower()
        vol = self.get_state("input_number.alexa_volume")
        if alexa == "all" :
            alexa = "group.gallalexa"
        else:
            alexa = "media_player." + alexa
        if new != "" :
            self.log("TTS called from  {} message is {}".format(alexa,new))
            self.call_service("notify/alexa_media",message=new, data={"type":"tts"}, target=alexa)
            self.set_state("input_text.tts", state="")
