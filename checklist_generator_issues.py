from bs4 import BeautifulSoup
import re
import json

with open('0.13.5p3rni.output') as json_file:
  data = None
  try:
    data = json.load(json_file)
  except ValueError:
    print('JSON is dumb')

  if data is not None:
    for p in data:
      number_pattern = re.compile('\d+')
      issue_link_number = number_pattern.search(p['url']).group()
      output_line = ' - [ ] ' + p['title'] + ' ' + '([#' + issue_link_number + '](https://github.com/brave/browser-laptop/issues/' + issue_link_number + '))'
      print(output_line)
  else:
    print('json went poopy')

