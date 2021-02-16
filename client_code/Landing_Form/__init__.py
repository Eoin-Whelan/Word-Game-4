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
    #anvil.server.call('record_score',"name", "source_word", round(random.uniform(10, 60), 3), "given_words")

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form('Game_Form')
    pass
