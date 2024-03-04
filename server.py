from flask import Flask,request,render_template,redirect,url_for
from urllib.parse import quote_plus
from read_pixel_data import get_unique_pix
from return_yt_thumbnail_url import get_img_url
app=Flask(__name__)
@app.route("/imageData/<path:url_img_na>")
def main_page(url_img_na):
	url_img=get_img_url(url_img_na)#url_img_na is the url of the yt video that was entered in the uploadUrl page and get_img_url is function that will return the image url 
	print(url_img,"thumbnail url")
	photo_data=get_unique_pix(url_img)# this will return the img pix data
	if photo_data==None:
		#photo_data is None that means that photos 720 version doesent exist so i will use the default hqdefault of that thumbnail 
		url_img=url_img.replace("hq720","hqdefault")
		photo_data=get_unique_pix(url_img)#now trying to get the data out of the default quality thumbnail image
	pix_val=photo_data[0]
	box_wi_hi=photo_data[1]
	#photo_data[0] would give me 
	return render_template('index.html',pixel_val_box=pix_val,box_width_height=box_wi_hi,url_img=url_img)
	
@app.route("/UploadUrl")
def upload_url_page():
	"""in this page you will submit your youtube video url"""
	return render_template("UploadUrl.html")
	
@app.route("/submit",methods=['POST'])
def submit_url():
	"""and the url will be redirected to this page and then sended to main_page """
	text_url=request.form["url-inp"]
	return redirect(url_for('main_page',url_img_na=text_url))

if __name__=="__main__":
	app.run(port=8000,debug=True)