import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil.google.drive import app_files
import anvil.http
import datetime

@anvil.server.callable
def log_attempt(outcome, given_word, user_input, user_agent):
  # params: outcome, given_word, user_input
  timestamp = datetime.datetime.strptime(datetime.datetime.now().strftime("%c"), '%c')
  app_tables.user_log.add_row(outcome=outcome, given_word=given_word, words=f'{", ".join(user_input)}', ip=anvil.server.context.client.ip, browser=user_agent, date_time=timestamp)
  pass
  
      
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
  #input_words = user_input.split(" ")
  print(user_input)
  print(given_word)
  fail_conditions = {
                      "duplicates" : [],
                      "short_words": [],
                      "invalid_chars": [],
                      "invalid_words": [],
                      "mispelled_words": []
                      }
  
  # Every fail condition is checked.
  [fail_conditions['duplicates'].append(word) for word in user_input if user_input.count(word) > 1]
  # Append any word that has differentiating characters to the original
  [fail_conditions['invalid_words'].append(word) for word in user_input if not all(letter in given_word for letter in word)]
  """
  List comprehension that appends
  """
  print(fail_conditions, "\n\n\n")
  # Did the user input 7 words?
  if len(user_input) != 7:
    print("Invalid Num of words!")
    fail_conditions.update({"invalid_num": len(user_input)})
  dictionary = import_dictionary()
  # Go through each word the user input
  for word in user_input:
    #print(all(letter in given_word for letter in word))
    # Is the word less than 4?
    if len(word) < 4:
      fail_conditions["short_words"].append(word)
    # Are there any "new"/invalid characters in the word?
    [fail_conditions["invalid_chars"].append(letter) for letter in word if letter not in given_word and letter not in fail_conditions['invalid_chars']]
    print(fail_conditions['invalid_chars'])
    print(fail_conditions['invalid_words'])
    # Check for if the word uses any extra charac
    print(word not in fail_conditions['invalid_words'])
    if word not in fail_conditions['invalid_words']:
      if word in dictionary:
        occurences = occurence_dict(given_word)
        for letter in word:
          if letter in occurences:
            occurences[letter] -= 1
          if any(value < 0 for value in occurences.values()):
            fail_conditions['invalid_words'].append(word)
            if letter not in fail_conditions['invalid_chars']:
              fail_conditions['invalid_chars'].append(letter)
            break
      else:
        fail_conditions['mispelled_words'].append(word)       
          
  print(fail_conditions)
  #fail_conditions['invalid_words'] = set(fail_conditions['invalid_words'])
  #fail_conditions['invalid_words'] = list(fail_conditions['invalid_words'])

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
def return_leaderboard():
  high_scores = app_tables.high_scores.search(tables.order_by("time",ascending=True))
  return high_scores
    #.order_by("position", ascending=False)
@anvil.server.callable
def return_log():
  log = app_tables.user_log.search(tables.order_by("date_time",ascending=False))
  return log


@anvil.server.callable
def record_score(name, source_word, record_time, given_words):
  """
    When a player successfully completes the game, their game details are passed in:
    - Name
    - Source word given by program
    - Their recorded time
    - Their input
    
    The current scores are pulled in, and their position in the front-end leaderboard is
    found. The score is recorded and their position is returned to the client before navigating
    to the leaderboard with that position passed as a parameter. This way, the position doesn't need
    to be stored but the user knows *their* position via an ascending order by time search.
  """
  curr_scores = app_tables.high_scores.search(tables.order_by("time", ascending=True))
  pos = 1
  print(record_time)
  for entry in curr_scores:
    if entry['time'] > record_time:
      break;
    pos +=1
  app_tables.high_scores.add_row(name=name, source_word=source_word, time=record_time,matches=given_words)
  return pos

@anvil.server.http_endpoint('/get-user-agent')
def get_user_agent():
  return anvil.server.request.headers['user-agent']