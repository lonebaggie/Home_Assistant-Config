#
# Repaced orginal Xiaoma Mihome automation.  
# Used to repace orginal analog  two way switch. Switch is upstairs  and downstairs is wireless switch. 
# This program listens for left and right buton press and toggles Landing and hall switch
# Pressing both buttons turn on both lights or turns off both lights  
#

import appdaemon.plugins.hass.hassapi as hass
class HRswitch(hass.Hass):
    def initialize(self):
# Has wireless switch (left or right) button pressed
        self.listen_event(self.hrswitch, "deconz_event")
    def hrswitch(self,event_name, data, kwargs):
        if data["id"] == "hall_wireless":
            swi = data["event"]
            self.log("Hall wireless  switch {} triggered".format(swi))
            if swi == 1002 :
                self.log("Toggle landing light")
                self.toggle("light.landing_light")
            if swi == 2002 :
                self.log("Toggle hall light")
                self.toggle("light.hall_light")
            if swi == 3002 :
                self.log("All downstairs off")
                self.turn_off("light.downstairs_lights")
                self.turn_on("light.landing_light")
                