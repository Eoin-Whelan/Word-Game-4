import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#

def say_hello():
  print("Hello, world")
  
  

@anvil.server.http_endpoint("/top10")
def top10():
    """
    pattern API endpoint takes an argument passed in via the :pat
    variable and creates a dictionary of the results. That is returned
    as a
    """
    
    #anvil.http.request()
    return open_form("Top_10")

@anvil.server.callable
def top_ten_form():
  print('Hello')
  anvil.server.
  if anvil.server.context("https://c00164354-wordgame4.anvil.app/_/api/top10"):
    print("Came from Endpoint")
    return True
  else:
    return False