import pil
  
# open the image 
Image1 = Image.open('image1\image.jpg')
  
# make a copy the image so that the  
# original image does not get affected 
Image1copy = Image1.copy() 

# paste image giving dimensions 
Image1copy.paste(Image2copy, (0, 0)) 
  
# save the image  
Image1copy.save('image2\pasted2.jpg')
