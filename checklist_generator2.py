from bs4 import BeautifulSoup
import re

body = open("0.13.3.output", "r", encoding="utf-8")

print("now for some soup...")
soup = BeautifulSoup(body, "html.parser")

print("find me some links of class js-navigation-open...")
issue_links = soup.find_all("a", class_="link-gray-dark no-underline h4 js-navigation-open")

i = 1
#print(issue_links.length)
for link in issue_links:
  issue_link_actual = link.get('href').strip()
  number_pattern = re.compile('\d+')
  issue_link_number = number_pattern.search(issue_link_actual).group()
  output_line = ' - ' + link.string.strip() + ' ' + '([#' + issue_link_number + '](https://github.com' + issue_link_actual + '))'
  #print(i)
  i = i+1
  print(output_line)
