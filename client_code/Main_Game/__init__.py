from ._anvil_designer import Main_GameTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Main_Game(Main_GameTemplate):
  c = Timer(interval=0.1)
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run when the form opens.

  def submit_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    Global c
    self.timer_1.interval = 0
    print(c)
    pass



