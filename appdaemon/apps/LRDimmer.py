import appdaemon.plugins.hass.hassapi as hass
class LRdimmer(hass.Hass):
    def initialize(self):
        self.listen_event(self.lrdimmer, "deconz_event")
    def lrdimmer(self,event_name, data, kwargs):
        if data["id"] == "tradfri_wireless_dimmer":
            swi = data["event"]
            self.log("tradfri dimmer {} triggered".format(swi))
            
            if swi == 1002 :
                
                self.call_service("light/turn_on", entity_id = "light.tradfri",brightness_step = 2 )
                
            if swi == 4002 :
                
                self.call_service("light/turn_on", entity_id = "light.tradfri", brightness_step = -10 )
            if swi == 2002 :
                
                self.call_service("light/turn_on", entity_id = "light.tradfri", brightness_step = 10)
                
            if swi == 3002 :
                
                self.call_service("light/turn_on", entity_id = "light.tradfri", brightness_step = -2)
            