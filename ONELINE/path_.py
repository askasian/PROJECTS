"""
This code is used to resize the images from dir/subdir to new directory (newdir/subdir) with its corresponding subdirectory
Original folder with it subdir:
../DATA/ORI-DIR
├─Apolo
├─Bailey
├─Bandit
├─Bella
New folder with its subdir:
    
../DATA/NEW-RESIZED-DIR
├─Apolo
├─Bailey
├─Bandit
├─Bella
"""

from PIL import Image
import glob
import os

# new folder path (may need to alter for Windows OS)
# change path to your path
ORI_PATH = '/usr/share/backgrounds/'
NEW_SIZE = 224
PATH = '../DATA/NEW-RESIZED-DIR' #the path where to save resized images

# create new folder
if not os.path.exists(PATH):
    os.makedirs(PATH)

# loop over existing images and resize
# change path to your path
for filename in glob.glob(ORI_PATH+'**/*.*'): #path of raw images with is subdirectory
    img = Image.open(filename).resize((NEW_SIZE,NEW_SIZE))
    
    # get the original location and find its subdir
    loc = os.path.split(filename)[0]
    subdir = loc.split('\\')[1]
    
    # assembly with its full new directory
    fullnew_subdir = PATH+"/"+subdir
    name = os.path.split(filename)[1]
    
    # check if the subdir is already created or not
    if not os.path.exists(fullnew_subdir):
        os.makedirs(fullnew_subdir)
    
    # save resized images to new folder with existing filename
    img.save('{}{}{}'.format(fullnew_subdir,'/',name))