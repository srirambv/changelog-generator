from bs4 import BeautifulSoup
import pycurl
from io import BytesIO

buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'https://github.com/brave/browser-laptop/issues?q=is%3Aissue+label%3Arelease-notes%2Finclude+is%3Aclosed+milestone%3A0.13.2')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()

print(body.decode('iso-8859-1'))
print("now for some soup...")
decodedbody = body.decode('iso-8859-1')
soup = BeautifulSoup(body, "html.parser")

print(soup.prettify())
