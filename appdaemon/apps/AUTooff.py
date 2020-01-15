# Program to switch off switches  after set time
import appdaemon.plugins.hass.hassapi as hass
class AUtooff(hass.Hass):
    def initialize(self):
        self.listen_state(self.autooff,"switch.wall_switch_right_158d0001660d34",new="on",duration=600)
        self.listen_state(self.autooff,"switch.wall_switch_right_158d0001a6596b",new="on",duration=600)
    def autooff(self, entity, attribute, old, new, kwargs):
        ename = self.get_state(entity,attribute="friendly_name")
        self.log("{} turned off automatically ".format(ename))
        self.turn_off(entity)
        