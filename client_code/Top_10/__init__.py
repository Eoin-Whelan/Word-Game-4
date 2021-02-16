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
      pos = (self.url_dict.get('position', ''))
      print(type(pos))
      print(pos)
      self.your_pos_label_show()      
      self.pos_label_show()   

  def your_pos_label_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    print("Showing label!!!")

    pass

  def pos_label_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    print("Showing label!!!")
    self.pos_label.text = self.url_dict.get('position', '')
    pass


