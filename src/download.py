# import typing elements
import string
from typing import Dict

# import lib to do HTTP requests
import requests



def download_csv_to_dict(url: string) -> Dict:
  """Download a csv from a URL and transform it to dict.
  return the Dict with the data or None if operation was
  not successful

  Args:
      url (string): url where the dict should be found

  Returns:
      Dict: an object containing data from the csv
  """
  # This is a HTTP Get call
  response = requests.get(url)
  
  if response.status_code != 200:
    print(f'GET {url} failed with {response.status_code}')
    return None
  
  print(response.content)
  
  
  
