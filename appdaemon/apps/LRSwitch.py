# Program replaces phyiscal switch . Turns tradfri bulbs on and off via Xiaoma wireless switch
import appdaemon.plugins.hass.hassapi as hass
class LRswitch(hass.Hass):
    def initialize(self):
        self.listen_event(self.lrswitch, "click", entity_id = "binary_sensor.wall_switch_158d0001830c7c", click_type = "single")
    def lrswitch(self,event_name, data, kwargs):
        if self.get_state("light.all_living_room_lights") == "off" :
            self.turn_on("input_boolean.relaxed")
        else :
            self.turn_off("light.all_living_room_lights")

            
            
            
      

        
            
        
        
        
        
        
        