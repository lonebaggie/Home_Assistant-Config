#
# Allow teanage daughter to turn off lights without getting out of bed
#

import appdaemon.plugins.hass.hassapi as hass
class MRswitch(hass.Hass):
    def initialize(self):
        self.listen_event(self.mrswitch, "deconz_event")
    def mrswitch(self,event_name, data, kwargs):
        if data["id"] == "maddy_switch":
            swi = data["event"]
            self.log("{} triggered".format(swi))
            if swi == 1002 :
                self.log("toggle light")
                self.toggle("light.maddy_light")