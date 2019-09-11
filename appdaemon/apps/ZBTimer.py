import appdaemon.plugins.hass.hassapi as hass
class ZBtimer(hass.Hass):
    def initialize(self):
        self.listen_state(self.zbtimer,"timer.zigbee_permit_join")
    def zbtimer (self, entity, attribute, old, new, kwargs):
        if new != "active" :
            self.log("Zigbee Join revoked by timer")
            self.log(new)
            self.turn_off("input_boolean.zigbee_permit_join")
