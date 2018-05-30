from bs4 import BeautifulSoup
import mechanize

schoolCode = []

def schoolCodeGenerator():
	for i in range(41001,41099):
		schoolCode.append(int(i))

browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.addheaders = [("User-agent","Firefox")]

schoolCodeGenerator()
startCode = schoolCode[0]
endCode =  schoolCode[len(schoolCode)-1]
for code in range(startCode,endCode):
	browser.open("http://103.251.43.113/sslcresult/schoolwiseresulthome.php")
	browser.select_form(name="frmResult")
	browser["schoolCoe"] = str(code)
	response = browser.submit()
	url = str(response.geturl())
	if "schoolwiseResult" in url:
		soup = BeautifulSoup(str(response.read()),'html5lib')
		data = soup.find_all("strong")
		info = " "
		for i in range(len(data)):
			info += str(data[i].getText())+" "

		print info
		
