import requests
import json
# Use a variable to get responses, for example: temp = requests.get('localhost')
request = requests.get("https://raw.githubusercontent.com/fin-github/TxtHOSTING/main/replitrequesttest.txt")
print(request)

  
# Example content processing
requestcontent = request.content
print(requestcontent)