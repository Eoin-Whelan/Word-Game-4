from ._anvil_designer import Main_GameTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

clock = 0

class Main_Game(Main_GameTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.timer_1.interval = 1
    # Any code you write here will run when the form opens.

  def submit_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    global clock
    self.timer_1.interval = 0
    print(self.timer_1)
    print(clock)
    pass

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    global clock
    
    clock += 1
    pass




