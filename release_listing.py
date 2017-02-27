from bs4 import BeautifulSoup
from io import BytesIO
import json
import pycurl
import re

buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'https://api.github.com/repos/brave/browser-laptop/releases')
c.setopt(pycurl.USERPWD, 'alexwykoff:')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
decodedbody = None

print(body.decode('iso-8859-1'))
#print("now for some soup...")
decodedbody = json.loads(body.decode('iso-8859-1'))
#soup = BeautifulSoup(body, "html.parser")

#print(soup.prettify())

if decodedbody is not None:
  for p in decodedbody:
    print(p['tag_name'])
      #number_pattern = re.compile('\d+')
      #issue_link_number = number_pattern.search(p['url']).group()
      #output_line = ' - [ ] ' + p['title'] + ' ' + '([#' + issue_link_number + '](https://github.com/brave/browser-laptop/issues/' + issue_link_number + '))'
      #print(output_line)
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
