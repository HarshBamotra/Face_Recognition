from PIL import Image , ImageFont , ImageDraw

img=Image.open('ss.png')
board=ImageDraw.Draw(img)
fnt=ImageFont.truetype("Myfont-Regular.ttf" , 60)
board.text((250 , 650) , "This is a fucking screenshot" , font=fnt , fill=(0,0,0))
img.show()
