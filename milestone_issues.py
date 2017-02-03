from bs4 import BeautifulSoup
import pycurl
from io import BytesIO

buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'https://api.github.com/repos/brave/browser-laptop/issues?milestone=49&state=all&per_page=1000')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.setopt(c.URL, 'https://api.github.com/repos/brave/browser-laptop/issues?milestone=49&state=all&per_page=1000&page=2')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()

print(body.decode('iso-8859-1'))
#decodedbody = body.decode('iso-8859-1')
#soup = BeautifulSoup(body, "html.parser")

#print(soup.prettify())
