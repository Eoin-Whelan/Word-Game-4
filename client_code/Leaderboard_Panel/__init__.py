"""
  Title:
  Author:
  Student No:
  Purpose:
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

@routing.route('top10')
@routing.route('top10', url_keys=['position'])
class Leaderboard_Panel(Leaderboard_PanelTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.high_scores_panel.items = anvil.server.call('return_leaderboard')[:10:]
    # Any code you write here will run when the form opens.
    #if self.url_dict.get('position', ''):
    
    if(self.url_dict.get('position', '')):
      self.your_pos_label.text = "Your position is:"
      self.play_game_btn.text = "Would you like to play again?"
      self.pos_label.text = self.url_dict.get('position', '') + " out of " + str(len(anvil.server.call('return_leaderboard')))
      set_url_hash('top10')
    else:
      self.your_pos_label_hide()
      self.pos_label_hide()
      
  def your_pos_label_hide(self, **event_args):
    """This method is called when the Label is removed from the screen"""
    pass

  def pos_label_hide(self, **event_args):
    """This method is called when the Label is removed from the screen"""
    pass

  def play_game_btn_click(self, **event_args):
    set_url_hash('')
   # set_url_hash('top10', pos)
    routing.reload_page(hard=True)


