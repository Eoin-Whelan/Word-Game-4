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
from ..Top_10 import Top_10


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
    self.victory_gif.source = "https://lh3.googleusercontent.com/5lLnbBqvtroaIZdTXl6_wepW-qZKFxSudsIqwv07FS2vK1QZoV7HQq6y2VdX4VHmtd-qpGLM7s5arfAJ0V3moCob9aSCRFQ4Zb6SP1p-L_82W1jx66a6VMCk3B_Jh9rXRMLMUiED-z1WbdOC1dzummKcA6_LUTBzNIrgIFBfaKUVkAnjg0qKoCszi0Gg1357f3RrJ4EvPrFXY2wXtf3GRz6JlSnyPGTa00n7js22ZCuEtCRFJ06Fv82bOuSAnUO-RVcSwhzohkNBs1RJNsY0ibYMqXb1SbvBueYSg84fuxNzFKz7p6ext2c_5SAd-LmcujVgTXT-rQBqap7daWKWfI069bNMiK19v43jvP2IpF1Ee732mN9WBunutANyjP4TZV1QviG5viRaWPSZN6VvwWCBJOEOhhWiLXI2ZxUTEaKr6561nzafDhPJIM3Tkwsp7cojb0bxHI7yEgz0ZuW_yX0gTNK6z4Sqi0UypIddPT9NUA-z3v2pTIXuToR3erK0oqZBGODUt7IWMNmjdtGHCgmy0zie4g8gatgk7k3dk6evVggR9uvntwXcMeCOfhcgt56mE5qrd5dJUZng-M7FTWa7GKVZ3FS20Z4_gl1l3tijyG6j1tQG6rqxN2DMOsci-zHMFXclRJZ5aFKPsNWfodfzpxJLwNIDoVSoOj6BCVTJtjkHxtTNc0R9XPxKjQ=w250-h202-no?authuser=0"
    # Any code you write here will run when the form opens.
    

  def button_1_click(self, **event_args):
    global record_time
    pos = anvil.server.call('record_score', self.name_box.text, source_word, record_time, ", ".join(word_matches)) 

    routing.set_url_hash(f'top10?position={pos}', 
                           replace_current_url=True,
                           redirect = True
                          ) 

