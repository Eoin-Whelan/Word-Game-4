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
@routing.route('top10', url_keys =['position'])
#@routing.route('Top10')
class Top_10(Top_10Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.high_scores.items = anvil.server.call('return_top_ten')
    # Any code you write here will run when the form opens.
    pos = self.
