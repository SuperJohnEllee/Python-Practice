from urllib.request import urlopen
from bs4 import BeautifulSoup

class IPLocationFinder:
	def __init__(self):
		self.keycdn = "https://tools.keycdn.com/geo?host="

	def findIPLocation(self, ipaddr):
		self.keycdn = self.keycdn + ipaddr
		html_page = urlopen(self.keycdn)
		soup = BeautifulSoup(html_page, 'html.parser')

		jsonData = soup.find("table").text.strip()
		jsonData = jsonData.splitlines()

		dataLength = len(jsonData) - 1;
		for x in range(0, dataLength, 2):
			if jsonData[x] and jsonData[x+1]:
				data = jsonData[x] + " = " + jsonData[x+1]
				print(data)

	def startApp(self, ipaddr):
		if not ipaddr:
			print("Please enter valid ip address!")
		else:
			self.findIPLocation(ipaddr)

if __name__ == '__main__':
	ipLoc = IPLocationFinder()
	ipLoc.startApp("182.18.202.206") #Example Only

#IP Adress Examples

#124.107.129.182 --> my.cpu.edu.ph
#182.18.202.206 --> CPU Henry Luce Library III
#198.57.186.238 --> CPU Web Site