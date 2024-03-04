import requests
from PIL import Image
from io import BytesIO
from math import sqrt
def get_unique_pix(url):
    image_get = requests.get(url)
    unique_pixels = {}
    if image_get.status_code == 200:
        image_pix_data = image_get.content #so as the image_get will give me a image so .content is used to get bytes 
        image_pixel = Image.open(BytesIO(image_pix_data))# by this i am storing the image data recived from the server to my RAM rather then saving it into my ROM 
        pixels = image_pixel.load()
        #total_pixels=image_pixel.size[0]*image_pixel.size[1] #this is the total number of pixel in that image
        #print(image_pixel.size[0],image_pixel.size[1])
        for i in range(image_pixel.size[0]):#width
            for j in range(image_pixel.size[1]):#height
                pixel = pixels[i, j] #spacific pixel data like lets say width is 0 and height is also 0 it will be [0,0] so it will give me the pixel data of 0,0
                unique_pixels.setdefault(str(pixel), 0)#so basixally i am making a dictionary out of every single pixes so i am making a dictionary {"pix_val":0} pix_val is pixel value and 0 is default set later i will count how many times that pixel appears in the image and then increment it by 1 
                unique_pixels[str(pixel)] += 1#incrementing the pixel appearing by 1 
        pix_total_num=[] #so it stores list of list of squres for the pixel 
        all_pix_lis=[]#stores all pixels 
        for pix,total_pre in unique_pixels.items(): #itrating over the pixel and its appearing dictionary 
        	pix_val_tuple=tuple(map(int,pix[1:-1].split(',')))#converting the string rgb to a tuble 
        	if total_pre<=2:
        		#it means that pixel should atleast appear more then 2 times or equal to 2
        		continue
        	else:
        		all_pix_lis.append(pix_val_tuple) #am appending every pixel into all_pix_lis
        		pix_total_num.append([sqrt(total_pre),sqrt(total_pre)])#so i will show that pixel in a squre
        return all_pix_lis,pix_total_num
if __name__=="__main__":
	pix_val_pix_di=get_unique_pix("https://i.ytimg.com/vi/krsBRQbOPQ4/hq720.jpg")
	print(pix_val_pix_di)
	#print(pix_val_pix_di[0])
