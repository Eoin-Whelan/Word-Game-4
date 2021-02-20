"""
  Title:      Main_Form
  Author:     Eoin Farrell
  Student No: C00164354
  Purpose:    Serves as the parent container for multiple
              routes. It includes all other panels to allow
              potential routes to be created as desired.
              
              The routing to landing_panel is what is first
              called to display as it is the first "page" the user
              will see when accessing with a "" URL path.
              (i.e. the default address of the app)
"""

from ._anvil_designer import Main_FormTemplate
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

from ..Fail_Form import Fail_Form
from ..Win_Form import Win_Form
from ..Landing_Panel import Landing_Panel
from ..Leaderboard_Panel import Leaderboard_Panel
from ..Game_Panel import Game_Panel
from ..Win_Form import Win_Form
from ..Fail_Form import Fail_Form
from ..Log_Panel import Log_Panel


@routing.main_router
class Main_Form(Main_FormTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
