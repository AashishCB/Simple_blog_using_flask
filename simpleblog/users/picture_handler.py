import os
# pip install pillow
from PIL import Image

from flask import url_for, current_app

def add_profile_pic(pic_upload,username,current_pic):
    filename = pic_upload.filename
    # Grab extension type .jpg or .png
    ext_type = filename.split('.')[-1]
    if current_pic == 'default_profile.png':
        storage_filename = str(username) + '_' + str(0) + '.' +ext_type
    else:
        a = current_pic.split('.')[0]
        for i in range(1,len(a)):
            if a[-i:].isdigit():
                continue
            else:
                count = a[-i+1:]
                count = int(count) + 1
                break
        storage_filename = str(username) + '_' + str(count) + '.' + ext_type
        
    filepath = os.path.join(current_app.root_path, 'static/profile_pics', storage_filename)
    if current_pic != 'default_profile.png':
        os.remove(os.path.join(current_app.root_path, 'static/profile_pics', current_pic))
    # Play Around with this size.
    output_size = (200, 200)

    # Open the picture and save it
    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)
    return storage_filename
