import mechanize
from bs4 import BeautifulSoup
import urllib

browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.addheaders = [("User-agent","Firefox")]

print "Paste Insta Photo URL"
photolink = raw_input().strip()

response = browser.open(photolink)
soup = BeautifulSoup(str(response.read()),'html5lib')
link = str(soup.find('meta',attrs={"property":"og:image"})['content'])

photo = urllib.urlopen(str(link))
photoname = link.split("/")
try:
	output = open(photoname[(len(photoname)-1)],"wb")
	output.write(photo.read())
	output.close()
	print "done"
except:
	print "error"
