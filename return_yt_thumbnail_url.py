import requests
from bs4 import BeautifulSoup

def get_img_url(video_url):
	"""using this function in Feb 26 2024 i am able to retrive the yt thumbnail from the yt video url and this code is still functional to retrive any yt video thumbnail  maybe it may not work cause yt is constanty updating but its working while i am writting this today Feb 26 2024"""
	respons=requests.get(video_url)#so this get function sends an HTTP GET request to the video_url and retrieve the response 
	if respons.status_code==200:
		#so if it sends an 200 status code that means everything is fine 
		data_text=respons.text #response.text retrives entire text based content like html css js
		soup = BeautifulSoup(data_text, 'html.parser') #now this will only parse the html code
		i=1
		for line in soup.prettify().split('\n'):
			#so by \n i am itrating line by line
			if "img" in line and "player-placeholder" in line: #so if any line had img which means it has image and player-placeholder which is i think so a class name or a id name so if any line has this two text means that it has the thumbnail img url
				start=line.find("url('")+len("url('")#so now just using some slicing i am retreving the thumbnail url
				end=line.find("')")
				non_hd_url=line[start:end]
				hd_url=non_hd_url.replace("hqdefault", "hq720")
				return hd_url
	else:
		return None

if __name__=="__main__":
	print(get_img_url("https://youtu.be/Tx-f30mwcVk?si=k2AIXs9sKvB2qbxO"))
