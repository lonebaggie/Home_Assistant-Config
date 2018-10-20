# Program to sync Tradfri lights to Physical switch
import appdaemon.plugins.hass.hassapi as hass
class LRswitch(hass.Hass):
    def initialize(self):
        self.handle = None
        self.listen_state(self.lrswitch,"switch.wall_switch_158d00016cf4bc")
    def lrswitch(self, entity, attribute, old, new, kwargs):
        if new == "on" :
# if switch turned on ensure light group is turn on .There is a bug if lights are turned off and on quickly group is still off so lights appear off
            self.turn_on("light.all_living_room_lights")
            self.cancel_timer(self.handle)
            self.log("Living Room Light on ")
        if new == "off" :
# if switch is off . Turn off light group and ensure timer is turned off in case light switched toggled quickly 
            self.handle=self.run_in(self.switchoff,10)
            self.select_option("input_select.light_state","Off")
            self.log("Living Room Light Off")
# routine to force Tradfri lights into unavaliable 
    def switchoff(self,kwargs):
        if self.get_state("switch.wall_switch_158d00016cf4bc") == "off" :
            self.log("force lights unavailable")
# ensure all lighs are toggled to force unavailable 
            self.toggle("light.living_room_lights")
            self.toggle("light.dining_room_lights")
            
            
            
        

            
            
            
      

        
            
        
        
        
        
        
        
