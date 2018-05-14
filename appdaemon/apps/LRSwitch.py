import appdaemon.plugins.hass.hassapi as hass
class LRswitch(hass.Hass):
    def initialize(self):
        self.listen_event(self.lrswitch, "click", entity_id = "binary_sensor.wall_switch_158d0001830c7c", click_type = "single")
    def lrswitch(self,event_name, data, kwargs):
        lr = self.get_state("light.living_room_lights")
        dr = self.get_state("light.dining_room_lights")
        if dr == "on" or lr == "on" :
            self.turn_off("light.living_room_lights")
            self.turn_off("light.dining_room_lights")
            
        if dr == "off" and lr == "off" :
            self.turn_on("light.living_room_lights")
            self.turn_on("light.dining_room_lights")
            
        if dr == "on" and lr == "on" :
            self.turn_off("light.living_room_lights")
            self.turn_off("light.dining_room_lights")
            
        
            
        
        
        
        
        
        