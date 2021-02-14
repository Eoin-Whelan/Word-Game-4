from ._anvil_designer import Win_PageTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Win_Page(Win_PageTemplate):
  def __init__(self, words, time, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    print(words)
    print(time)
    self.victory_gif.source = "https://media.tenor.com/images/cf63db03ab055fb2dcbbd887b3edf3b0/tenor.gif""
    # Any code you write here will run when the form opens.
    
