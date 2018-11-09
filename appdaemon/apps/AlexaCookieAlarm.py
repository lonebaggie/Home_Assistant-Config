# Program to alarm if Alexa cookie expires
import appdaemon.plugins.hass.hassapi as hass
class Alexacookiealarm(hass.Hass):
    def initialize(self):
        self.listen_state(self.alexacookiealarm,"sensor.alexa_alarm", new="on")
    def alexacookiealarm(self, entity, attribute, old, new, kwargs):
        self.log("Alexa cookie alarm triggered")
        self.call_service("persistent_notification/create", title = "Alexa Cookie Error",  
        message = "Alexa script failed. Login error", notification_id = "alexafail")
            

        

        