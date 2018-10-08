import requests as api

lng = 19.61954771
lat = 40.81952034
token = 'token'

endpoint = 'https://api.under.test/'
body = {
		'lng':lng,
		'lat':lat,
		'accuracy':" ",
		'altitude':" ",
		'bearing':" ",
		'speed':" "		
		}
headers =  {
		'Content-Type': "application/json",
		'Authorization': f"Bearer {token}",
		'Cache-Control': "no-cache"
		}

responce = api.request("POST", url = endpoint, data=body, headers=headers)
print(responce.status_code, responce.text)