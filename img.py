import ImageFont, ImageDraw, Image
import os
def runscript(txt):
    image = Image.new('RGBA', (300, 120),(255,0,0,0))
    draw = ImageDraw.Draw(image)
    #txt = "Pratik"
    fontsize = 1  # starting font size

    # portion of image width you want text width to be
    img_fraction = 1

    font = ImageFont.truetype("Ubuntu-B.ttf", fontsize)
    while font.getsize(txt)[0] < img_fraction*image.size[0]:
	# iterate until the text size is just larger than the criteria
	fontsize += 1
	font = ImageFont.truetype("Ubuntu-B.ttf", fontsize)

    # optionally de-increment to be sure it is less than criteria
    fontsize -= 1
    font = ImageFont.truetype("Ubuntu-B.ttf", fontsize)

    print 'final font size',fontsize
    draw.text((0, 0), txt, font=font) # put the text on the image
    image.save('name.png') # save it
    
    os.system('sudo mv name.png /lib/plymouth/themes/ubuntu-logo/ubuntu_logo.png')
    os.system('sudo update-initramfs -u ')
    os.system('echo "Successfully Changed The Boot Logo with great difficulties" '); 