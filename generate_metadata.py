#!/bin/python

#<license>MIT License</license>
#<author>Anjum Ahuja</author>
#<repo>https://github.com/jack8daniels2/pixels</repo>

import os
import urllib
import random
#from PIL import Image

colors = ['#779ECB', '#A1CAF1', '#ADDFAD', '#DEA5A4','#CB99C9', '#B39EB5']
image_types = ['jpg','tif']
top = 'images'

def generate_image_md(color, dirpath, image):
    image_path = urllib.quote(os.path.join(dirpath, image))
    # im = Image.open(image_path)
    return '\t---\n' +\
	   '<!-- .slide: data-background="{}" -->\n'.format(color) +\
	   '\t[![{0}]({1})]({1})'.format(image,image_path)
	   #'\t![{}]({})\n'.format(image, image_path)

def generate_album_md(dirpath, images):
    album = dirpath.rsplit('/', 1)[1].strip()
    color = random.choice(colors)
    return '###{}\n'.format(album) + \
	   '<!-- .slide: data-background="{}" -->\n'.format(color) +\
            ''.join([generate_image_md(color, dirpath, image) for image in images])
                         
data = os.walk(top)
data = [(dirpath, images) for dirpath,_,images in data]
data = [(dirpath, 
         filter(lambda s: not s.startswith('.') and \
  		          s.rsplit('.',1)[1] in image_types, 
	        images))
        for dirpath, images in data]
data = filter(lambda d: len(d[1]), data)
metadata = '----\n'.join([generate_album_md(dirpath, images) for dirpath, images in data])
with open('albums.md','w') as fp:
    fp.write(metadata)
