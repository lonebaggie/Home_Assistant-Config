import appdaemon.plugins.hass.hassapi as hass
class ZBjoin(hass.Hass):
    def initialize(self):
        self.listen_state(self.zbjoin,"input_boolean.zigbee_permit_join")
    def zbjoin (self, entity, attribute, old, new, kwargs):
        self.log("zigbee")
        if new == "on" :
            self.log("Zigbee Join permitted")
            self.call_service("mqtt/publish", topic="zigbee2mqtt/bridge/config/permit_join",payload="true")
            self.call_service("timer/start", entity_id="timer.zigbee_permit_join")
        if new == "off" :
            self.log("Zigbee Join revoked")
            self.call_service("mqtt/publish", topic="zigbee2mqtt/bridge/config/permit_join",payload="false")
            self.call_service("timer/finish", entity_id="timer.zigbee_permit_join")