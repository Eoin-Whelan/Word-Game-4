from ._anvil_designer import Fail_FormTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .Reason_Panel import Reason_Panel

class Fail_Form(Fail_FormTemplate):
  def __init__(self, fail_conditions, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    print(fail_conditions)
        # define the function blocks

    for condition in fail_conditions:
            # Set Form properties and Data Bindings.
      if condition == "short_words" and fail_conditions[condition]:
        self.column_panel_1.add_component(Reason_Panel("Words were too short: ", fail_conditions[condition]))
      if condition == "invalid_chars" and fail_conditions[condition]:
        self.column_panel_1.add_component(Reason_Panel("Use of invalid characters: ", fail_conditions[condition]))
      if condition == "invalid_words" and fail_conditions[condition]:
        self.column_panel_1.add_component(Reason_Panel("Non-valid words from source word: ", fail_conditions[condition]))
      if condition == "mispelled_words" and fail_conditions[condition]:
        self.column_panel_1.add_component(Reason_Panel("Invalid spelled words: ", fail_conditions[condition]))
      if condition == "invalid_num":
        self.column_panel_1.add_component(Reason_Panel("Invalid numer of words submitted: ", str(fail_conditions[condition])))
      #self.criteria_label.text = criteria


        # map the inputs to the function blocks
    
        # Any code you write here will run when the form opens.
    
