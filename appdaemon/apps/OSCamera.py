#
# Trigger Alexa when camera motion detected 
#
import appdaemon.plugins.hass.hassapi as hass
class OScamera(hass.Hass):
    def initialize(self):
        self.listen_state(self.oscamera,"binary_sensor.blink_front_door_motion_detected", new = "on")
    def oscamera(self, entity, attribute, old, new, kwargs): 
        self.log("Motion detected")
#       self.call_service("notify/alexa_media",message="Outside Camera movement detected", data={"type":"announce","method":"all"}, target="media_player.house")
        if self.sun_down():
            self.log("After sunset lights on")
            self.turn_on("light.outside_light")
            self.turn_on("light.front_room_light")
            self.turn_on("light.kitchen_light")
            self.turn_on("light.hall_light")
       
