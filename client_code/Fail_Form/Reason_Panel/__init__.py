"""
  Title:      Reason_Panel
  Author:     Eoin Farrell
  Student No: C00164354
  Purpose:    Reason_Panel is the template for panels on the
              label component added potentially numerous times
              on the Fail_Form's reasons_panel.
"""

from ._anvil_designer import Reason_PanelTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Reason_Panel(Reason_PanelTemplate):
    def __init__(self, reason, **properties):
        self.init_components(**properties)
        self.reason_label.text = reason
