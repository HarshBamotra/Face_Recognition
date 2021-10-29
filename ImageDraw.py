from PIL import Image , ImageDraw

img=Image.open('ss.png')
img.show()

board=ImageDraw.Draw(img)
board.rectangle((0 , 0 , 700 , 700) , outline=(0,0,0) , width=10)   #here outline is for color
board.line((0 , 0 , 700 , 700) , fill=(255 , 0 , 0) , width=5)      #here fill is for color
img.show()