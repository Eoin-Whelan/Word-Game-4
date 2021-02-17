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

    # Set Form properties and Data Bindings.
    if reason == "short_words" and reason is not None:
      self.reason_label.text = "Words were too short: "
    if reason == "invalid_chars" and reason is not None:
      self.reason_label.text = "Use of invalid characters: "
    if reason == "invalid_words" and reason is not None:
      self.reason_label.text = "Non-valid words from source word: "
    if reason == "mispelled_words" and reason is not None:
      self.reason_label.text = "Invalid spelled words: "
    if reason == "invalid_num":
      self.reason_label.text = "Invalid numer of words submitted: "

    self.criteria_label.text = criteria
    # Any code you write here will run when the form opens.