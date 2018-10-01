# smtp and Alexa warning of Water Leak
import appdaemon.plugins.hass.hassapi as hass
class Leakwarning(hass.Hass):
    def initialize(self):
        self.listen_state(self.leakwarning,"binary_sensor.water_leak_sensor_158d0001c3472b",new="on")
        self.listen_state(self.leakwarning,"binary_sensor.water_leak_sensor_158d0001c347c9",new="on")
    def leakwarning (self, entity, attribute, old, new, kwargs):
        mess= "Leak Detected by " + self.friendly_name(entity)
        self.log(mess)
        self.notify(mess, title = "Leak Warning", name = "notify.gmail_alert")
        self.call_service('media_player/alexa_tts', entity_id= "media_player.downstairs", message= mess)
        self.call_service('media_player/alexa_tts', entity_id= "media_player.br_echo", message= mess)
        