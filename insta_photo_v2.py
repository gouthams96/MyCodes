import mechanize
import json
import urllib

browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.addheaders = [("User-agent","Firefox")]

def save_photo(image_url):
	photo = urllib.urlopen(image_url)
	photoname = image_url.split("/")
	
	try:
		output = open(photoname[(len(photoname)-1)],"wb")
		output.write(photo.read())
		output.close()
		print "done"
	except:
		print "error"

def insta_profile(profile_link):
	profile_data = browser.open(profile_link)
	temp_data = str(profile_data.read()).split("edge_owner_to_timeline_media")
	temp_jdata = str(temp_data[1]).split("edge_saved_media")
	jdata = str(temp_jdata[0])
	jsondata = json.loads(str(jdata[2:-2]))
	items = len(jsondata["edges"])
	for i in range(items):
		url =  str(jsondata["edges"][i]["node"]["display_url"])
		print url
		save_photo(url)

print "Paste Insta Profile URL"
profile_link = raw_input().strip()
insta_profile(profile_link)

