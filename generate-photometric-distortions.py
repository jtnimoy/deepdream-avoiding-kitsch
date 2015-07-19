import sys,os,random

base_dir = './wga.hu'

images = []

def recursiveList(path):
    global images
    for i in os.listdir(path):
        if i[-4:]=='.jpg':
            images += ['%s/%s' % (path, i)]
        elif i=='.DS_Store' or i[-5:]=='.html':
            os.system('rm %s/%s' % (path,i)) # <-------------- IMPORTANT: this deletes .DS_Store and .html files. Be careful.
        else:
            recursiveList(path+'/'+i)

recursiveList(base_dir)

counter = 0
for i in images:
    bareFile = i[:-4]

    for j in xrange(10):
        crop_w = random.random()*50+25
        crop_h = random.random()*50+25
        resize_w = random.random()*125+25
        resize_h = random.random()*125+25
        cmd= 'convert %s -crop %i%%x%i%% -resize %i%%x%i%% %s_%i.jpg' % (i,crop_w,crop_h,resize_w,resize_h,bareFile,j)
        os.system( cmd )
    print s