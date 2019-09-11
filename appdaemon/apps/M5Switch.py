import appdaemon.plugins.hass.hassapi as hass
class M5switch(hass.Hass):
    def initialize(self):
        self.listen_state(self.m5switch_a,"binary_sensor.m5_button_a",new="on")
        self.listen_state(self.m5switch_b,"binary_sensor.m5_button_b",new="on")
        self.listen_state(self.m5switch_c,"binary_sensor.m5_button_c",new="on")
    def m5switch_a(self, entity, attribute, old, new, kwargs):
        self.log("M5 Button a triggered")
        self.toggle("input_boolean.dark")
    def m5switch_b(self, entity, attribute, old, new, kwargs):
        self.log("M5 Button b triggered")
        self.toggle("input_boolean.relaxed")
    def m5switch_c(self, entity, attribute, old, new, kwargs):
        self.log("M5 Button c triggered")
        self.toggle("input_boolean.bright")