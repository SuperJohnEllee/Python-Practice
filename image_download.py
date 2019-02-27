import random
import requests

get = str(input("Enter url of image to download: "))

def download_image(url):
	print("Downloading...")
	name = random.randrange(1, 1000)
	full_name = str(name) + ".jpg"
	r = requests.get(url, stream=True)
	#save file as binary because its not text
	with open(full_name, 'wb') as f:
		f.write(r.content)
	return "download compeleted. saved as name: " + full_name
print(download_image(get))