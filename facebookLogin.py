import mechanize

browser  = mechanize.Browser()
browser.set_handle_robots(False)
browser.addheaders = [('User-agent','Firefox')]
browser.open("https://www.facebook.com/")
browser.select_form(id="login_form")
browser["email"] = ""
browser["pass"] = ""
response = browser.submit()

print response.geturl()
