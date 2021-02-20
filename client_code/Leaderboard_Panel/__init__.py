"""
  Title:      Leaderboard_Panel
  Author:     Eoin Farrell
  Student No: C00164354
  Purpose:    Leaderboard_Panel is the leaderboard feature for the app
              It features the top 10 fastest player times for successful runs.
"""

from ._anvil_designer import Leaderboard_PanelTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from HashRouting import routing

# Multiple route paths in the event a user is coming from the win form.
@routing.route("top10")
@routing.route("top10", url_keys=["position"])
class Leaderboard_Panel(Leaderboard_PanelTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.high_scores_panel.items = anvil.server.call("return_leaderboard")[:10:]

        """
          When a user is coming from a win_form, the URL_key will contain the
          position of the user's submission in the leaderboard.
          
          Note: This is spoofable by a user to appear at the top of the list by
                entering '*app*/#top10?position=1' in the URL bar of their browser.
                However, this will not affect the integrity of the leaderboard data as the
                submission of successful attempts is handled in Win_form.
        """
        if self.url_dict.get("position", ""):
            self.your_pos_label.text = "Your position is:"
            self.play_game_btn.text = "Would you like to play again?"
            self.pos_label.text = (
                self.url_dict.get("position", "")
                + " out of "
                + str(len(anvil.server.call("return_leaderboard")))
            )

    # The following button click events are to route to a new game or review the rules.
    def play_game_btn_click(self, **event_args):
        routing.set_url_hash(
            "NewGame", replace_current_url=False, redirect=True
        )        
        #routing.reload_page(hard=True)

    def restart_btn_click(self, **event_args):
        routing.set_url_hash(
            "", replace_current_url=False, redirect=True
        )
        #routing.reload_page(hard=True)


