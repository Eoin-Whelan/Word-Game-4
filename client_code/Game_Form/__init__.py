from ._anvil_designer import Game_FormTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import time
import random


class Game_Form(Game_FormTemplate):
  clock = time.time()
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    given_word = random.choice([word for word in anvil.server.call('import_dictionary') if len(word) >= 8])
    self.random_word.text = given_word
    # Any code you write here will run when the form opens.

  def submit_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.clock = time.time() - self.clock
    words = self.user_input_box.text
    #words = "towing towel wing goat twong toe nile"
    #words = "towing towel wing tong legion tingle nile"
    fail_conditions = anvil.server.call('submit_answers', words, self.random_word.text)
    if any(fail_conditions.values()):
      open_form('Fail_Form', fail_conditions)
    else:
      print(round(self.clock, 3))
      open_form('Win_Form', self.random_word.text, words, round(self.clock, 3))
    pass

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    self.clock += 0.001
    pass




