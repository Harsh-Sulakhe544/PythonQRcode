import qrcode as qr #(created a alias (nickname))
# make() will help to generate the qrcode  and save() will save the code in a png file (image file ) 

img=qr.make("https://docs.python.org/3/")  # pass in the url of the website or any text (simple -> "hello")
img.save("python_docs_chrome.png") # to generate an img we use .png