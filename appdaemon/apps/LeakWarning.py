# TV and Alexa warning of Water Leak
import appdaemon.plugins.hass.hassapi as hass
class Leakwarning(hass.Hass):
    def initialize(self):
        self.listen_state(self.leakwarning,"binary_sensor.water_leak_sensor_158d0001c3472b",new="on")
        self.listen_state(self.leakwarning,"binary_sensor.water_leak_sensor_158d0001c347c9",new="on")
    def leakwarning (self, entity, attribute, old, new, kwargs):
        mess= "Leak Detected by " + self.friendly_name(entity)
        self.log(mess)
        self.notify(mess, name = "notify.enigma")
        self.call_service("notify/alexa_media",data={"type":"announce", "method":"all"},message=mess,target="group.gallalexa",title = "Leak Warning")
        
        