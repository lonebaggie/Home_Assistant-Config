import appdaemon.plugins.hass.hassapi as hass
class LRswitch(hass.Hass):
    def initialize(self):
        self.listen_event(self.lrswitch, "click", entity_id = "binary_sensor.wall_switch_158d0001830c7c", click_type = "single")
    def lrswitch(self,event_name, data, kwargs):
        self.toggle("light.all_living_room_lights")

        
            
        
        
        
        
        
        