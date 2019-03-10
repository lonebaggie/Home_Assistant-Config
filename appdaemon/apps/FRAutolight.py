#
# Grampy Aid turn lights when Gramp's get up at night via motion Sensor . Turns on lights to Aid Toilet time !
# Added input boolean to turn off automation manually  . Had cat issues which triggered motion senor. 
# Moved sensor so cat unable to trigger 

import appdaemon.plugins.hass.hassapi as hass
class FRautolight(hass.Hass):
    def initialize(self):
# Trigger if Motion detected
        self.listen_state(self.frautolight,"binary_sensor.motion_sensor_158d000187392e",new="on")
    def frautolight (self, entity, attribute, old, new, kwargs):
#Only turn on lights if already off and between set times and when boolean switch on 
        if self.now_is_between("sunset - 00:45:00", "sunrise + 00:45:00") and self.get_state("light.front_room_light") == "off" and self.get_state("input_boolean.ms1") == "on" :
            self.turn_on("light.front_room_light")
            self.turn_on("light.hall_light")
            self.turn_on("light.hall_toilet_light")
            
