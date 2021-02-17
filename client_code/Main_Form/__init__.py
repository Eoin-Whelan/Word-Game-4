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
#from ..Game_Form import Game_Form
from ..Top_10 import Top_10
from ..Win_Form import Win_Form
from ..Landing_Form import Landing_Form
from ..Leaderboard_Panel import Leaderboard_Panel
from ..Game_Panel import Game_Panel
from ..Win_Form import Win_Form
from ..Fail_Form import Fail_Form
@routing.main_router
class Main_Form(Main_FormTemplate):
  def __init__(self, **properties):
      # Set Form properties and Data Bindings.
    self.init_components(**properties)
