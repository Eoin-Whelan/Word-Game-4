from ._anvil_designer import Landing_FormTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from HashRouting import routing
import random

@routing.route('', title='Welcome!')
class Landing_Form(Landing_FormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    high_scores = app_tables.high_scores.search(tables.order_by("time",ascending=True))

  def start_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.start_btn.enabled = False
    set_url_hash("NewGame")
    routing.reload_page(hard=True)
    pass
