import mechanize
import json
import urllib

browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.addheaders = [("User-agent","Firefox")]

def getUserId(username):
	response = browser.open("https://www.instagram.com/"+username)
	profile = str(response.read())
	data = profile.split("profilePage_")
	userid = data[1].split("\"")
	userid = userid[0]
	return str(userid)

def getdp(userid):
	dplink = browser.open("https://i.instagram.com/api/v1/users/"+userid+"/info/")
	dpdata = str(dplink.read())
	jsondata = json.loads(dpdata)
	fullDpLink = str(jsondata["user"]["hd_profile_pic_url_info"]["url"])
	photo = urllib.urlopen(fullDpLink)
	photoname = fullDpLink.split("/")
	try:
		output = open(photoname[(len(photoname)-1)],"wb")
		output.write(photo.read())
		output.close()
		print "photo saved.."
	except:
		print "error while saving the photo"
	
	print "link = "+fullDpLink

	
print "Type : Instagram ID"
userid = getUserId(str(raw_input().strip()))
getdp(userid)
