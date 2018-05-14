import appdaemon.plugins.hass.hassapi as hass
import datetime
class LRcheckstate(hass.Hass):

  def initialize(self):

    time = datetime.time(0, 00, 0)
    self.run_minutely(self.lrcheckstate, time)

  def lrcheckstate(self, kwargs):
      
      self.log("Checking Light State")
      if self.get_state("group.gikea") == "off" :
          self.select_option("input_select.light_state", "Off")
      else:
          if self.get_state("light.dining_room_lights") == "on" :
              br = self.get_state("light.dining_room_lights", attribute="brightness")
          if self.get_state("light.living_room_lights") == "on" :
              br = self.get_state("light.living_room_lights", attribute="brightness")
          if br > 0 and br  < 26 :
              self.select_option("input_select.light_state", "Dark")
          if br > 25 and br < 204 :
              self.select_option("input_select.light_state", "Relaxed")
          if br > 203 :
              self.select_option("input_select.light_state", "Bright")
          
    
      
        
        