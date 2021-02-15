from ._anvil_designer import Landing_PageTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.http
import anvil.server

class Landing_Page(Landing_PageTemplate):
  def __init__(self, **properties):
      # Set Form properties and Data Bindings.
    self.init_components(**properties)
    diction = anvil.server.call('occurence_dict', "aratauro")
    #anvil.server.request
    print(anvil.server.context)
    if anvil.server.context is "server_module":
      print("Came for top 10")
    # Any code you write here will run when the form opens.
    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form('Main_Game')
    pass

