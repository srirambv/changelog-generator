from bs4 import BeautifulSoup
import re
import json

#body = open("milestone.13.2.output", "r", encoding="utf-8")

#print("now for some soup...")
#soup = BeautifulSoup(body, "html.parser")

#print("find me some links of class js-navigation-open...")
#issue_links = soup.find_all("a", class_="link-gray-dark no-underline h4 js-navigation-open")

with open('13.2.output') as json_file:
  data = None
  try:
    data = json.load(json_file)
  except ValueError:
    print('JSON is dumb')

  if data is not None:
    for p in data:
      #print(p['url'])
      number_pattern = re.compile('\d+')
      issue_link_number = number_pattern.search(p['url']).group()
      output_line = ' - [ ] ' + p['title'] + ' ' + '([#' + issue_link_number + '](https://github.com/brave/browser-laptop/issues/' + issue_link_number + '))'
      print(output_line)
  else:
    print('json went poopy')

i = 1
#print(issue_links.length)
#for link in issue_links:
#  issue_link_actual = link.get('href').strip()
#  number_pattern = re.compile('\d+')
#  issue_link_number = number_pattern.search(issue_link_actual).group()
#  output_line = ' - [ ] ' + link.string.strip() + ' ' + '([#' + issue_link_number + '](https://github.com' + issue_link_actual + '))'
#  print(i)
#  i = i+1
#  print(output_line)
