# import typing elements
import string
from typing import Dict, List

# import lib to do HTTP requests
import requests

def get_dict_from_csv_string(csv_string: string) -> List[Dict]:
  """function to convert csv string to dict

  Args:
      csv_string (string): the raw csv

  Returns:
      List[Dict]: list containing the rows encoded in the csv as dicts
  """
  rows = csv_string.split('\n')
  header_raw = rows[0]
  rows = rows[1:]
  dict_keys = header_raw.replace(" ", "").split(',')
  
  the_table = []
  for row in rows:
    values=row.replace(" ", "").split(',')
    dict_row = {}
    for key, value in zip(dict_keys, values):
      dict_row[key] = float(value)
    the_table.append(dict_row)
    
  return the_table

def download_csv_to_dict(url: string) -> List[Dict]:
  """Download a csv from a URL and transform it to dict.
  return the Dict with the data or None if operation was
  not successful

  Args:
      url (string): url where the dict should be found

  Returns:
    List[Dict]: list containing the rows encoded in the csv as dicts

  """
  # This is a HTTP Get call
  response = requests.get(url)
  
  if response.status_code != 200:
    print(f'GET {url} failed with {response.status_code}')
    return None
  
  content_string = response.content.decode()
  
  try:
    return get_dict_from_csv_string(content_string)
  except:
    print(f'dict from {url} could not be converted')
    return None
    
  
  
  
