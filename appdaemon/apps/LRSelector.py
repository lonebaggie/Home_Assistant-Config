#
# This program actions an  Item select (Off Dark, Relaxed and bright ) on two set of Tradfri lights (living room and Dinning  3 in each set) 
#These bulbs are located  the same pysical room (open plan dining and living room)
#
#
#
import appdaemon.plugins.hass.hassapi as hass
class LRselector(hass.Hass):
    def initialize(self):
# Triggered if Item select is changed
        self.listen_state(self.lrselect,"input_select.light_state")
    def lrselect (self, entity, attribute, old, new, kwargs):
        self.ent = "light.tradfri"
        if new != "Off" and self.get_state("switch.livingroom") == "off" :
            self.turn_on("switch.livingroom")
        if new == "Dark" :
            self.call_service("light/turn_on", entity_id = self.ent, color_temp = 500)
            self.log("dark colour triggered")
            self.run_in(self.dark_b,1)
        if new == "Relaxed" :
            self.call_service("light/turn_on", entity_id = self.ent, color_temp = 420)
            self.log("relaxed colour triggered")
            self.run_in(self.relaxed_b,1)
        if new == "Bright" :
            self.call_service("light/turn_on", entity_id = self.ent, color_temp = 154)
            self.log("bright colour triggered")
            self.run_in(self.bright_b,1)
        if new == "Off" :
            self.turn_off(self.ent)
            self.turn_off("switch.livingroom")
    def dark_b(self,kwargs):
        self.call_service("light/turn_on", entity_id = self.ent, brightness = 20)
        self.log("dark  brightness triggered")
    def relaxed_b(self,kwargs):
        self.call_service("light/turn_on", entity_id = self.ent, brightness = 170)
        self.log("relaxed brightness triggered")
    def bright_b(self,kwargs):
        self.call_service("light/turn_on", entity_id = self.ent, brightness = 254)
        self.log("bright brightness triggered")
    

    
    


  
        
