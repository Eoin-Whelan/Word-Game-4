from ._anvil_designer import leaderboard_rowsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class leaderboard_rows(leaderboard_rowsTemplate):
  num_row = 1
  def __init__(self, **properties):
    self.pos_label.text = leaderboard_rows.num_row
    leaderboard_rows.num_row += 1
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.
