from ._anvil_designer import Win_FormTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from HashRouting import routing
import anvil.http


class Win_Form(Win_FormTemplate):
  source_word = None
  word_matches = None
  record_time = None
  def __init__(self, given_word, words, time, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    global source_word
    source_word = given_word
    global word_matches
    global record_time
    print(type(words))
    word_matches = words
    record_time = time

    self.player_time_label.text = time
    self.victory_gif.source = "https://i.imgur.com/svbDVw7.gif"
    # Any code you write here will run when the form opens.
    

  def button_1_click(self, **event_args):
    global record_time
    pos = anvil.server.call('record_score', self.name_box.text, source_word, record_time, ", ".join(word_matches)) 

    routing.set_url_hash(f'top10?position={pos}', 
                           replace_current_url=True,
                           redirect = True
                          ) 
    routing.reload_page(hard=True)

