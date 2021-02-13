from ._anvil_designer import Landing_PageTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Landing_Page(Landing_PageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    diction = anvil.server.call('occurence_dict', "aratauro")
    word = "taurus"
    anvil.server.call('submit_answers', word, "arataadsasdassdgvcfdscurus")
    # Any code you write here will run when the form opens.
    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form('Main_Game')
    pass

