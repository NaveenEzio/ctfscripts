#source:https://github.com/lifebow/EFIENSCTF_ROUND2_RE_WRITEUP/blob/master/README.md

from PIL import Image

im= Image.open('te.png')
pix=im.load()        #load image
print(im.size)       #dimension
print(pix[0,0])
a=[]
b=[]
c=[]
d=[]
for i in range(im.size[1]):
    a.append(chr(pix[0,i][3]))
    b.append(chr(pix[0,i][0]))
    c.append(chr(pix[0,i][1]))
    d.append(chr(pix[0,i][2]))


print("".join(a))
print("\n")
print("".join(b))
print("\n")
print("".join(c))
print("\n")
print("".join(d))
print("\n")