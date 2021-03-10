

image1=open("image1.jpg",'r')
image2=open("image.jpg",'w')
image2.copy(image1)
image1.close()
image2.close()
