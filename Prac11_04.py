from PIL import Image 
m = Image.open("C:\\Users\\400T6B\\Downloads\\italy-1587287_1920.jpg")
m.show()

from matplotlib.pyplot import imshow
imshow(m)

m.save("C:\\Users\\400T6B\\Downloads\\italy-1587287_1920.gif")
mygif=Image.open("C:\\Users\\400T6B\\Downloads\\italy-1587287_1920.gif")

from matplotlib.pyplot import imshow
imshow(mygif)