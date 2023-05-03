import requests
import xml.etree.ElementTree as ET

celcius = '20'

url = 'https://www.w3schools.com/xml/tempconvert.asmx'

SOAPEnvelope = f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <CelsiusToFahrenheit xmlns="https://www.w3schools.com/xml/">
      <Celsius>{celcius}</Celsius>
    </CelsiusToFahrenheit>
  </soap:Body>
</soap:Envelope>"""

options = {"Content-Type": "text/xml; charset=utf-8"}

response = requests.post(url, data=SOAPEnvelope, headers=options)
root = ET.fromstring(response.text)
for node in root.iter('{https://www.w3schools.com/xml/}CelsiusToFahrenheitResult'):
    print(node.text)
