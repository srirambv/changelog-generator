from bs4 import BeautifulSoup
import pycurl
from io import BytesIO

buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'https://github.com/brave/browser-laptop/milestone/45?closed=1')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()

print(body.decode('iso-8859-1'))
print("now for some soup...")
decodedbody = body.decode('iso-8859-1')
soup = BeautifulSoup(body, "html.parser")

print(soup.prettify())
