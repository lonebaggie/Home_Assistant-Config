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
    
    def bri(self,kwargs):
        bri= kwargs["b"]
        time = kwargs["time"]
        self.call_service("light/turn_on", entity_id = "light.living_room_2", brightness = bri, transition = time)
    def fade (self, kwargs):
        col = kwargs["col"]
        time = kwargs["time"]
        self.call_service("light/turn_on", entity_id = "light.living_room", color_temp = col, transition = time)

    def lrselect (self, entity, attribute, old, new, kwargs):
        lr = self.get_state("switch.living_room")
        
        

        if new == "Dark" :
            if lr == "off":
                self.turn_on("switch.living_room")
                
            else :
                self.h1= self.run_in(self.bri,0,b=1,time=6)
                self.h2 = self.run_in(self.fade,7, col=454,time=2)
                self.log("dark colour triggered")
            
        if new == "Relaxed" :
            if lr == "off":
                self.turn_on("switch.living_room")
                
            else :
                self.h1 = self.run_in(self.bri,0,b=170,time=2)
                self.h2 = self.run_in(self.fade,3, col=400, time=2)
                self.log("relaxed colour triggered")
        if new == "Bright" :
            if lr == "off":
                self.turn_on("switch.living_room")
                
            else :
                self.h1= self.run_in(self.bri,0,b=254,time=2)
                self.h2 = self.run_in(self.fade,3, col=250,time=2)
                self.log("bright colour triggered")
            
        if new == "Off" :
            
            self.turn_off("light.living_room")
            self.turn_off("light.living_room_2")
            
            
            self.log("Off triggered")
            
    
        
        
    

    
    


  
        
