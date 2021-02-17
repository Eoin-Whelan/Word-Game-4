from ._anvil_designer import Top_10Template
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
#@routing.route('Top10')
class Top_10(Top_10Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.high_scores.items = anvil.server.call('return_leaderboard')[:10:]
    # Any code you write here will run when the form opens.
    #if self.url_dict.get('position', ''):
    
    if(self.url_dict.get('position', '')):
      self.your_pos_label.text = "Your position is:"
      self.play_game_btn.text = "Would you like to play again?"
      self.pos_label.text = self.url_dict.get('position', '') + " out of " + str(len(anvil.server.call('return_leaderboard')))
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
    routing.set_url_hash("NewGame", 
                           replace_current_url=True,
                           redirect = True
                          ) 




