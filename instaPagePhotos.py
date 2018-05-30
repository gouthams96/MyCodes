import mechanize
from bs4 import BeautifulSoup
import urllib
import json



browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.addheaders = [("User-agent","Firefox")]

def photoDownloader(srclink):

	photo = urllib.urlopen(str(srclink))
	photoname = srclink.split("/")
	
	try:
		output = open(photoname[(len(photoname)-1)],"wb")
		output.write(photo.read())
		output.close()
		print "done"
	except:
		print "error"


def linkfinder(link):
	response = browser.open(link)
	soup = BeautifulSoup(str(response.read()),'html5lib')
	instadata = str(soup)
	data = instadata.split("window._sharedData")
	jdata = str([data[1]]).split(";<")
	jsond =  str(jdata[0])
	jsonFinal = str(jsond[5:])

	jsondata = json.loads(jsonFinal)

	photosize =  len(jsondata["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"])

	for i in range(photosize):
		src = jsondata["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][i]["node"]["display_url"]
		photoDownloader(str(src))


print "Paste Insta Profile URL"
link = raw_input().strip()
linkfinder(link)
