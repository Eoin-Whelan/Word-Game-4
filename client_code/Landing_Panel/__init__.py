"""
  Title:      Landing_Panel
  Author:     Eoin Farrell
  Student No: C00164354
  Purpose:    Landing_Panel serves as both the rules page
              and the first page a user will see when they
              load up the app. Players can navigate to a new
              game from here.
"""

from ._anvil_designer import Landing_PanelTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from HashRouting import routing
import random


@routing.route("", title="Welcome!")
class Landing_Panel(Landing_PanelTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

    def start_btn_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.start_btn.enabled = False
        routing.set_url_hash("NewGame", replace_current_url=True, redirect=True)
        pass
