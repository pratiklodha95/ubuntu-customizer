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
image = Image.new('RGBA', (1000, 58),(255,0,0,0))
draw = ImageDraw.Draw(image)
txt = "Pratik"

font = ImageFont.truetype("Ubuntu-R.ttf", 50)

draw.text((0, 0), txt, font=font) # put the text on the image
image.save('name.png') # save it

# thread.start_new_thread(OSCalls)
