import requests

print("\n")
zip = input("Enter zip code: ")
#print("\n")
print("** JSONP results from WSDL service with SOAP request for zip " + zip + " ** ")
print("_________________________________" )
url="http://search.ams.usda.gov/farmersmarkets/v1/data.svc/zipSearch?zip=" + zip
#headers = {'content-type': 'application/soap+xml'}
headers = {'content-type': 'text/xml'}
body = """<?xml version="1.0" encoding="UTF-8"?>
         <SOAP-ENV:Envelope xmlns:ns0="http://ws.cdyne.com/WeatherWS/" xmlns:ns1="http://schemas.xmlsoap.org/soap/envelope/" 
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
            <SOAP-ENV:Header/>
              <ns1:Body><ns0:GetWeatherInformation/></ns1:Body>
         </SOAP-ENV:Envelope>"""
""" response = requests.post(url,data=body,headers=headers)
print(response.content) """

request = requests.get(url)
json = request.json()
#print("\n")
print("** Closest Local farmers market for zip code " +  zip +" **" )
print (json.get('results')[0].get("marketname"))
print("_________________________________" )
print(" ")
print("** Distance to Local farmers market in your area for zip code " +  zip +" **")
for markets in json['results']:
   print(markets['marketname'])
   #print(markets)
   spaceString = markets['marketname']
print("\n")



