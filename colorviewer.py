import turtle
screen=turtle.Screen()
l=[char for char in "0123456789ABCDEF"]
while True:
 z=0
 c=input("""What color do you want to be displayed?
Hex and RGB supported, Formats should be:
Hex: #ffFFFf; FFFFFF
RGB: 255, 255, 255; 255,255,255
If you input an invalid color, the screen will probably become black
""").replace(" ", "").upper()
 p=[char for char in c]
 o=c.split(",")
 for i in l:
  z+=c.count(i)
 if len(o)==3:
  try:screen.bgcolor((int(o[0]),int(o[1]),int(o[2])))
  except:screen.bgcolor("#000000")
 else:
  if len(c)==6 and z==6:screen.bgcolor("#"+c)
  else:screen.bgcolor(c)
