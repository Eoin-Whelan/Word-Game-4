from ._anvil_designer import Log_PanelTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from HashRouting import routing

@routing.route('log')
class Log_Panel(Log_PanelTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = anvil.server.call('return_log')
    # Any code you write here will run when the form opens.
    #if self.url_dict.get('position', ''):
    



