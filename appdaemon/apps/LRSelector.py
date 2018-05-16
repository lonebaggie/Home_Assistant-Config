import appdaemon.plugins.hass.hassapi as hass
class LRselector(hass.Hass):
    def initialize(self):
        self.listen_state(self.lrselect,"input_select.light_state")
    def lrselect (self, entity, attribute, old, new, kwargs):
        ent = "light.all_living_room_lights"
        la = self.get_state(ent)
        lr = self.get_state("light.living_room_lights")
        dr = self.get_state("light.dining_room_lights")
        if lr == "on" and dr != "on" :
            ent = "light.living_room_lights"
        if lr != "on" and dr == "on" :
            ent = "light.dining_room_lights"
        self.log("new = {} ent = {} la = {} lr = {} dr = {}".format(new,ent,la,lr,dr) )
        if new == "Off" :
            self.turn_off(ent)
            self.turn_off("input_boolean.dark")
            self.turn_off("input_boolean.relaxed")
            self.turn_off("input_boolean.bright")
        if new == "Dark" :
            self.log("dark triggered")
            self.call_service("light/turn_on", entity_id = ent, brightness = 25, transition = 6 , color_temp = 450)
            self.turn_on("input_boolean.dark")
        if new == "Relaxed" :
            self.log("relaxed triggered")
            self.call_service("light/turn_on", entity_id = ent, brightness = 203, transition = 6 , color_temp = 367)
            self.turn_on("input_boolean.relaxed")
        if new == "Bright" :
            self.log("bright triggered")
            self.call_service("light/turn_on", entity_id = ent, brightness = 254, transition = 6 , color_temp = 250)
            self.turn_on("input_boolean.bright")    
            
        