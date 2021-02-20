"""
  Title:      Win_Form
  Author:     Eoin Farrell
  Student No: C00164354
  Purpose:    Win_Form is the page that loads when the failure criteria for 
              a user submission returns an empty list. It displays the user's
              time back to them and allows them to enter their name and submit
              their attempt to the leaderboard.
              
              Note: Win_Form is not a URL routing path as it would allow spoofed 
              leaderboard entries. It is only displayed in the event of an attempt at
              the game itself.
"""

from ._anvil_designer import Win_FormTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from HashRouting import routing
import anvil.http


class Win_Form(Win_FormTemplate):
    """
    These global variables allows their value assignment
    in the initialization of the form which in turn allows
    the user's submission info to be directly passed to
    the server when they proceed to the leaderboard.
    """

    source_word = None
    word_matches = None
    record_time = None

    def __init__(self, given_word, words, time, **properties):
        self.init_components(**properties)
        global source_word
        global word_matches
        global record_time
        source_word = given_word
        word_matches = words
        record_time = time

        self.player_time_label.text = time
        self.victory_gif.source = "https://i.imgur.com/svbDVw7.gif"

    def button_1_click(self, **event_args):
        global record_time
        pos = anvil.server.call(
            "record_score",
            self.name_box.text,
            source_word,
            record_time,
            ", ".join(word_matches),
        )
        # route is set to the top10 form and performs a hard refresh.
        routing.set_url_hash(
            f"top10?position={pos}", replace_current_url=True, redirect=True
        )

        routing.reload_page(hard=True)