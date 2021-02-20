"""
  Title:      Leaderboard_Panel_Row
  Author:     Eoin Farrell
  Student No: C00164354
  Purpose:    Acts as a data row in the leaderboard panel. 
"""
from ._anvil_designer import Leaderboard_Panel_RowTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Leaderboard_Panel_Row(Leaderboard_Panel_RowTemplate):
    num_row = 1

    def __init__(self, **properties):
        self.pos_label.text = Leaderboard_Panel_Row.num_row
        Leaderboard_Panel_Row.num_row += 1
        self.init_components(**properties)
