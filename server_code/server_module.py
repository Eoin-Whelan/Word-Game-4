import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil.google.drive import app_files
import anvil.http
from . import Module1
 
      
@anvil.server.callable
def occurence_dict(word):
  occurences = {}
  for letter in word:
    occurences.update({letter: word.count(letter)})
  return occurences

#SCV
@anvil.server.callable
def submit_answers(user_input, given_word):
  print("Checking answers")
  #print([letter for letter in user_input if letter not in given_word])
  #print(occurences)
  input_words = user_input.split(" ")
  print(input_words)
  print(given_word)
  fail_conditions = {"short_words": [],
                      "invalid_chars": [],
                      "invalid_words": [],
                      "mispelled_words": []
                      }
  
  # Every fail condition is checked.
  
  # Append any word that has differentiating characters to the original
  [fail_conditions['invalid_words'].append(word) for word in input_words if not all(letter in given_word for letter in word)]
  """
  List comprehension that appends
  """
  
  # Did the user input 7 words?
  if len(input_words) != 7:
    print("Invalid Num of words!")
    fail_conditions.update({"invalid_num": len(input_words)})
  dictionary = import_dictionary()
  # Go through each word the user input
  for word in input_words:
    #print(all(letter in given_word for letter in word))
    # Is the word less than 4?
    if len(word) < 4:
      print("Invalid Length of word!")
      fail_conditions["short_words"].append(word)
    # Are there any "new"/invalid characters in the word?
    [fail_conditions["invalid_chars"].append(letter) for letter in word if letter not in given_word]
    # Check for if the word uses any extra charac
    
    occurences = occurence_dict(given_word)
    for letter in word:
      if letter in occurences:
        occurences[letter] -= 1
      if any(value < 0 for value in occurences.values()):
        fail_conditions['invalid_words'].append(word)
        
    if word not in dictionary:
      fail_conditions['mispelled_words'].append(word)
          
  print(fail_conditions)
  return fail_conditions
  
@anvil.server.callable
def import_dictionary():

  dictionary_raw = app_files.words_txt.get_bytes()
  fStr = str(dictionary_raw, "utf-8")
  fStr = fStr.split("\n")
  fSet = {line.replace("'s", "").lower() for line in fStr}
  words = sorted(fSet)[1::]
  return words
  
@anvil.server.callable
def return_top_ten():
  high_scores = app_tables.high_scores.search(tables.order_by("time",ascending=True))
  return high_scores
  print(type(high_scores))
    #.order_by("position", ascending=False)

@anvil.server.callable
def record_score(name, source_word, record_time, given_words):
  app_tables.high_scores.add_row(name=name, source_word=source_word, time=record_time,matches=given_words)
  #high_scores = app_tables.high_scores.search(tables.order_by("time", ascending=True))
  
@anvil.server.http_endpoint("/top10")
def top10():
    """
    pattern API endpoint takes an argument passed in via the :pat
    variable and creates a dictionary of the results. That is returned
    as a
    """
    Module1.top_10()
    #return anvil.http.request(anvil.server.get_app_origin(), data="top_10")    #anvil.http.request()


