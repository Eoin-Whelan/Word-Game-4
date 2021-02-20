"""
  Title:      Game_Panel
  Author:     Eoin Farrell
  Student No: C00164354
  Purpose:    Game_Panel is the main panel for Word Game 4.
              User enters a word, which is then passed to either
              a pass or fail form depending on fail conditions
              being met.
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


@routing.route("NewGame")
class Game_Panel(Game_PanelTemplate):
    clock = 0
  
    """
      Initialization selects a random word from the dictionary file
      equal or greater than 8 characters and records the current time
      to record the player's time on submission.
    """
    def __init__(self, **properties):
        self.init_components(**properties)
        self.user_input_box.placeholder = "Enter words here"
        given_word = random.choice(
            [word for word in anvil.server.call("import_dictionary") if len(word) >= 8]
        )
        self.random_word.text = given_word
        self.clock = time.time()

    """
      When the submit button is clicked, the text of the input box is
      converted to a list, filtering out whitespace entries. If the list
      is empty, the user is directed back to fill out the box before
      attempting to submit. Otherwise, their time taken is recorded and 
      their attempt is submitted. The submission is passed to
      the server which returns a dictionary of failure criteria.
      
      If the dict is empty, the submission was a success and the win form
      is loaded. Otherwise, they are sent to the failure form to see where
      they went wrong. Beforehand, their attempt is logged to a data table with
      the relevant information.
    """
    def submit_btn_click(self, **event_args):
        self.submit_btn.enabled = False
        words = list(filter(None, self.user_input_box.text.lower().split(" ")))

        if not words:
            self.user_input_box.text = None
            self.user_input_box.placeholder = "You need to *actually* put words in here, not just spaces. Time is ticking!"
            self.submit_btn.enabled = True

        else:
            self.clock = time.time() - self.clock
            fail_conditions = anvil.server.call(
                "submit_answers", words, self.random_word.text
            )
            
            # A log of the user input, and browser info is passed to the server
            if any(fail_conditions.values()):
                anvil.server.call(
                    "log_attempt",
                    "!!! ERRORS",
                    self.random_word.text,
                    words,
                    anvil.http.request(
                        anvil.server.get_api_origin() + "/get-user-agent"
                    ).get_bytes().decode("utf-8"),
                )
                open_form("Fail_Form", fail_conditions)
            else:
                anvil.server.call(
                    "log_attempt",
                    "SUCCESS",
                    self.random_word.text,
                    words,
                    anvil.http.request(
                        anvil.server.get_api_origin() + "/get-user-agent"
                    ).get_bytes().decode("utf-8"),
                )
                open_form(
                    "Win_Form", self.random_word.text, words, round(self.clock, 2)
                )