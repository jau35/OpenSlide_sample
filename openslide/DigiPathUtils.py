import os
from PIL import Image
from openslide import OpenSlide, open_slide

def save_img(slide, col, row, delta, dir, size=None, lvl=0, JPEG=True):
    width, height = slide.level_dimensions[lvl]
    if(row < 0 or row + delta > height):
        return None
    if(col < 0 or col + delta > width):
        return None
    
    try:
        filename = '%d_%d.%s' % ( col, row, 'jpg' if JPEG else 'png')
        filename = os.path.join(dir, filename)

        img = slide.read_region((col,row), lvl, (delta, delta))
        
        if(size): # resize
            img.thumbnail(size, Image.ANTIALIAS)
        if(JPEG): # convert for JPG
            img = img.convert('RGB')

        img.save(filename)

        return filename
    except:
        return None


def decompose_file(filename, delta, begin=[0,0], n=[None,None], out_dir='./', JPEG=True, size=None):
    slide = open_slide(filename)
    end = list(slide.dimensions)
    print(end)
    
    if(n[0]):
        end[0] = begin[0] + n[0]*delta
    if(n[1]):
        end[1] = begin[1] + n[1]*delta
    
    file = os.path.splitext(os.path.basename(filename))[0]
    dir = os.path.join(out_dir, file, str(delta))
    if(not os.path.isdir(dir)):
        os.makedirs(dir)
    
    for c in range(begin[0], end[0], delta):
        for r in range(begin[1], end[1], delta):
            imgfile = save_img(
                slide=slide,
                col=c,
                row=r, 
                delta=delta, 
                dir=dir,
                JPEG=JPEG,
                size=size
                )
            if(imgfile is None):
                print('Failed: c=%d, r=%d' % (c, r))
                slide = open_slide(filename)
    
    slide.close()