"""
  Title:
  Author:
  Student No:
  Purpose:
"""

from ._anvil_designer import Game_PanelTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import time
import random
from HashRouting import routing


@routing.route('NewGame')
class Game_Panel(Game_PanelTemplate):
  clock = 0
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user_input_box.placeholder = "Enter words here"
    given_word = random.choice([word for word in anvil.server.call('import_dictionary') if len(word) >= 8])
    self.random_word.text = given_word
    self.clock = time.time()
    # Any code you write here will run when the form opens.

  def submit_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.submit_btn.enabled = False
    words = list(filter(None, self.user_input_box.text.lower().split(" ")))

    if not words:
      self.user_input_box.text = None
      self.user_input_box.placeholder = "You need to *actually* put words in here, not just spaces. Time is ticking!"
      self.submit_btn.enabled = True

    else:
      self.clock = time.time() - self.clock
      fail_conditions = anvil.server.call('submit_answers', words, self.random_word.text)
      if any(fail_conditions.values()):
        anvil.server.call('log_attempt', "!!! ERRORS", self.random_word.text, words, anvil.http.request(anvil.server.get_api_origin() + '/get-user-agent').get_bytes().decode('utf-8'))
        open_form('Fail_Form', fail_conditions)
      else:
        print(round(self.clock, 3))
        anvil.server.call('log_attempt', "SUCCESS", self.random_word.text, words, anvil.http.request(anvil.server.get_api_origin() + '/get-user-agent').get_bytes().decode('utf-8'))
        open_form('Win_Form', self.random_word.text, words, round(self.clock, 3))


  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    self.clock += 0.001
    pass


