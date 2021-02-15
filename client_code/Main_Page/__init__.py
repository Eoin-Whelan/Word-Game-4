from ._anvil_designer import Main_PageTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.http
import anvil.server
import time
from HashRouting import routing

from ..Fail_Page import Fail_Page
from ..Game_Page import Game_Page
from ..Top_10 import Top_10
from ..Win_Page import Win_Page

#@routing.main_router
class Main_Page(Main_PageTemplate):
  def __init__(self, **properties):
      # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #anvil.server.request
    print(type(routing.get_url_hash()))
    print(get_url_hash())


    # Any code you write here will run when the form opens.
    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form('Game_Page')
    pass
  
  def top_ten_direct(self):
    if get_url_hash() == "#top10":
      print("Yes")
      anvil.open_form('Top_10')
