#!/usr/bin/python3

import requests # behave like a bowser
               #now connecting a web-browser

webdata = requests.get("https://www.fb.com")
print(webdata)

#now locking for html data

html_data = webdata.text #get front end code
print(webdata.text)
f=open("hello.txt",'w')
f.write(html_data)
f.close()
