from ._anvil_designer import Reason_PanelTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Reason_Panel(Reason_PanelTemplate):
  def __init__(self, reason, criteria, **properties):
    self.init_components(**properties)

    self.reason_label.text = reason
    self.criteria_label.text = ", ".join(criteria)
    # Any code you write here will run when the form opens.