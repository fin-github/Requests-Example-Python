# Import requests to be able to use the requests part of code.
import requests


# This uses a variable to get responses/error codes (Not content!)!
request = requests.get("https://raw.githubusercontent.com/fin-github/TxtHOSTING/main/replitrequesttest.txt")
print(request)

#This uses a simple if block to detect if it is a 404 or a 200 and print the results
if request == 200:
    print("Success! This has successfully got the response from the server.")  
elif request == 404:
  # "Elif" Is a shortened term of "else if"
    print("The server returned a 404 error. Sorry, make sure that you can access the URL.")
  
# Example content processing
requestcontent = request.content
print(requestcontent)