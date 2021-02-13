import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil.google.drive import app_files


class Dictionary:
   words = []
   def __init__(self,):
      dictionary_raw = app_files.word_game_dictionary.get_bytes()
      fStr = str(dictionary_raw, "utf-8")
      fStr = fStr.split("\n")
      fSet = {line.replace("'s", "").lower() for line in fStr}
      words = sorted(fSet)[1::]
      
      
word_list = Dictionary()
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
  fail_conditions = {"short_words": [],
                      "invalid_chars": [],
                      "invalid_words": [],
                      }
  # Every fail condition is checked.
  
  # Did the user input 7 words?
  if len(input_words) != 7:
    print("Invalid Num of words!")
    fail_conditions.extend("invalid_num", len(input_words))
  # Go through each word the user input
  for word in user_input:
    # Is the word less than 4?
    if len(word) < 4:
      fail_conditions.extend("short_words", word)
    # Are there any "new"/invalid characters in the word?
    fail_conditions.extend("invalid_chars", letter for letter in word if letter not in given_word)
    
    # Check for if the word uses any extra charac
    occurences = occurence_dict(given_word)

      for letter in word:
          if letter in occurences:
            occurences[letter] -= 1
            print(occurences)
      if any(value < 0 for value in occurences.values()):
        print("Ran out of letters for ", word)
        
    else:
      print("fail!")
      break
  #print(occurences, '\n' ,user_input, given_word)
  
  
@anvil.server.callable
def import_dictionary():
    """
    Imports the words_txt file through the Anvil Google Drive API.
    It then converts to bytes and casts to a string
    before applying the string-relevant functions to
    transform and return it as a list.
    """
    fStr = app_files.words_txt.get_bytes()
    fStr = str(fStr, "utf-8")
    fStr = fStr.split("\n")
    fSet = {line.replace("'s", "").lower() for line in fStr}
    fSet = sorted(fSet)[1::]
    return fSet
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

