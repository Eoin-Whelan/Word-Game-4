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

    for condition in fail_conditions:
      if condition == "duplicates" and fail_conditions[condition]:
        self.column_panel_1.add_component(Reason_Panel(f"You have duplicates in your list: {' '.join(fail_conditions[condition])}"))
      if condition == "short_words" and fail_conditions[condition]:
        self.column_panel_1.add_component(Reason_Panel(f"These words were too small: {' '.join(fail_conditions[condition])}"))
      if condition == "invalid_chars" and fail_conditions[condition]:
        self.column_panel_1.add_component(Reason_Panel(f"You used these invalid letters: {' '.join(fail_conditions[condition])}"))
      if condition == "invalid_words" and fail_conditions[condition]:
        self.column_panel_1.add_component(Reason_Panel(f"You submitted these words using extra/invalid letters different from the source word: {fail_conditions[condition]}"))
      if condition == "mispelled_words" and fail_conditions[condition]:
        self.column_panel_1.add_component(Reason_Panel(f"You mispelled these words: {' '.join(fail_conditions[condition])}"))
      if condition == "invalid_num":
        self.column_panel_1.add_component(Reason_Panel(f"You submitted an incorrect number of words: {' '.join(str(fail_conditions[condition]))}, not 7"))
      #self.criteria_label.text = criteria


        # map the inputs to the function blocks
    
        # Any code you write here will run when the form opens.
    
