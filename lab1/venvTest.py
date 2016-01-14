#!/usr/bin/env python

#get stuff from web
import requests

print requests.__version__

#print "\n"

response = requests.get('http://google.com/')

print response.status_code
#200 = okay
#200s = okay, generally good
#300s = go look somewhere else, or later
#4-500s = errors usually

print response.text
