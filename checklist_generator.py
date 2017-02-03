from bs4 import BeautifulSoup
import re 

body = open("milestone131.output", "r", encoding="utf-8")

print("now for some soup...")
soup = BeautifulSoup(body, "html.parser")

issue_links = soup.find_all("a", class_="Box-row-link")

for link in issue_links:
  issue_link_actual = link.get('href').strip()
  number_pattern = re.compile('\d+')
  issue_link_number = number_pattern.search(issue_link_actual).group()
  output_line = ' - [ ] ' + link.string.strip() + ' ' + '([#' + issue_link_number + '](https://github.com' + issue_link_actual + '))'
  print(output_line)
