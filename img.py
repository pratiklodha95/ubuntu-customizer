import ImageFont, ImageDraw, Image, thread
import os

def OSCalls():
    os.system('sudo mv name.png ubuntu-customiser/ubuntu_logo.png')
    os.system('sudo cp -r -f ubuntu-customiser /lib/plymouth/themes/ubuntu-customiser')
    os.system('sudo cp -f /etc/alternatives/default.plymouth default_backup.plymouth')
    os.system('sudo cp -f default.plymouth /etc/alternatives/default.plymouth')
    os.system('sudo update-initramfs -u ')
    os.system('echo "Successfully changed the boot logo :D" ');


# def runscript(txt):
image = Image.new('RGBA', (1000, 58),(0,0,0,0))
draw = ImageDraw.Draw(image)
txt = "Abhijit Tomar"
fontsize = 1  # starting font size

# portion of image width you want text width to be
img_fraction = 0.89

font = ImageFont.truetype("Ubuntu-R.ttf", fontsize)
while font.getsize(txt)[1] < img_fraction*image.size[1]:
# iterate until the text size is just larger than the criteria
    fontsize += 1
    font = ImageFont.truetype("Ubuntu-R.ttf", fontsize)

# optionally de-increment to be sure it is less than criteria
fontsize -= 3
font = ImageFont.truetype("Ubuntu-R.ttf", fontsize)

width=font.getsize(txt)[0]
print width
image=image.crop((0, 0, width+38,58 ))

print 'final font size',fontsize
draw.text((0, 0), txt, font=font) # put the text on the image

#mergin with the logo
if(1>2)
    ubuntu_logo=Image.open('ubuntu_logo.png')
    image.paste(ubuntu_logo,(width,0),ubuntu_logo);
else
    kubuntu_logo=Image.open('kubuntu_logo.png)
    image.paste(kubuntu_logo,(width,0),kubuntu_logo);

image.save('name.png') # save it
# thread.start_new_thread(OSCalls)
