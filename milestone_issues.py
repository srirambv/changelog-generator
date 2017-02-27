from bs4 import BeautifulSoup
import pycurl
from io import BytesIO

buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'https://api.github.com/repos/brave/browser-laptop/issues?milestone=50&labels=release-notes%2Finclude&state=all&per_page=100')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()

print(body.decode('iso-8859-1'))
#decodedbody = body.decode('iso-8859-1')
#soup = BeautifulSoup(body, "html.parser")

#print(soup.prettify())
