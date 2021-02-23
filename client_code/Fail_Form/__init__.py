"""
  Title:      Fail_Form
  Author:     Eoin Farrell
  Student No: C00164354
  Purpose:    Fail_Form is the page on which the user's incorrect input is
              displayed back as criteria for their failed attempt.
              
              Note: FailForm is not a URL routing path as a user does not need direct
              access via a hash URL. It is only displayed in the event of an attempt at
              the game itself.
"""

from ._anvil_designer import Fail_FormTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .Reason_Panel import Reason_Panel
from HashRouting import routing


class Fail_Form(Fail_FormTemplate):
    def __init__(self, fail_conditions, **properties):

        self.init_components(**properties)
        """
        Loops acts similary to a switch statement by generating a panel
        containing a label stating the fail condition the player's input
        met.
        """
        for condition in fail_conditions:
            if condition == "source_word" and fail_conditions[condition]:
                self.reasons_column_panel.add_component(
                    Reason_Panel(
                        f"You used the source word: {fail_conditions[condition]}"
                    )
                )
            if condition == "duplicates" and fail_conditions[condition]:
                self.reasons_column_panel.add_component(
                    Reason_Panel(
                        f"You have duplicates in your list: {', '.join(fail_conditions[condition])}"
                    )
                )
            if condition == "short_words" and fail_conditions[condition]:
                self.reasons_column_panel.add_component(
                    Reason_Panel(
                        f"These words were too small: {', '.join(fail_conditions[condition])}"
                    )
                )
            if condition == "invalid_chars" and fail_conditions[condition]:
                self.reasons_column_panel.add_component(
                    Reason_Panel(
                        f"You used these invalid/extra letters: {', '.join(fail_conditions[condition])}"
                    )
                )
            if condition == "invalid_words" and fail_conditions[condition]:
                self.reasons_column_panel.add_component(
                    Reason_Panel(
                        f"You submitted these words using extra/invalid letters: {', '.join(fail_conditions[condition])}"
                    )
                )
            if condition == "mispelled_words" and fail_conditions[condition]:
                self.reasons_column_panel.add_component(
                    Reason_Panel(
                        f"You mispelled these words: {', '.join(fail_conditions[condition])}"
                    )
                )
            if condition == "invalid_num":
                self.reasons_column_panel.add_component(
                    Reason_Panel(
                        f"You submitted an incorrect number of words: {''.join(str(fail_conditions[condition]))}, not 7"
                    )
                )

    def restart_btn_click(self, **event_args):
        """
        When the user wishes to play the game again, the game
        is refreshed given the URL route will still fall under
        the #NewGame route.
        """
        self.restart_btn.enabled = False
        self.rules_btn.enabled = False
        routing.reload_page(hard=True)

    def rules_btn_click(self, **event_args):
        """
        Entire application is restarted, thereby reverting the
        player back to the rules/landing page.
        """
        self.restart_btn.enabled = False
        self.rules_btn.enabled = False
        routing.set_url_hash("")
        routing.reload_page(hard=True)
