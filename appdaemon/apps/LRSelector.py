import appdaemon.plugins.hass.hassapi as hass
class LRselector(hass.Hass):
    def initialize(self):
        self.listen_state(self.lrselect,"input_select.light_state")
    def lrselect (self, entity, attribute, old, new, kwargs):
        lr = self.get_state("light.living_room_lights")
        dr = self.get_state("light.dining_room_lights")
        if lr == "off" and dr == "off" :
            lr = "on"
            dr = "on"
        if new == "Off" :
            self.turn_off("group.gikea")
        if new == "Dark" :
            if dr == "on" :
                self.call_service("light/turn_on", entity_id = "light.dining_room_lights", brightness = 25, color_temp = 450)
            if lr == "on" :
                self.call_service("light/turn_on", entity_id = "light.living_room_lights", brightness = 25, color_temp = 450)
        if new == "Relaxed" :
            if dr == "on" :
                self.call_service("light/turn_on", entity_id = "light.dining_room_lights", brightness = 203, color_temp = 367)
                
            if lr == "on" :
                self.call_service("light/turn_on", entity_id = "light.living_room_lights", brightness = 203, color_temp = 367)
                
        if new == "Bright" :
            if dr == "on" :
                self.call_service("light/turn_on", entity_id = "light.dining_room_lights", brightness = 254, color_temp = 250)
                
            if lr == "on" :
                self.call_service("light/turn_on", entity_id = "light.living_room_lights", brightness = 254, color_temp = 250)
                
            
        