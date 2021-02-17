from ._anvil_designer import Win_PanelTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

@routing.route('WinPanel', url_keys=['winning_criteria'])
class Win_Panel(Win_PanelTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    if(self.url_dict.get('winning_criteria', '')):
      print(self.url_dict.get('winning_criteria', ''))
    else:
      self.your_pos_label_hide()
      self.pos_label_hide()