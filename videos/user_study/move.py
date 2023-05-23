import glob
import shutil
import os
for i in range(10):
    for f in glob.glob(f'./* ({i + 1}).mp4'):
        # print(f)
        fname = f[2:]
        # print(fname)
        src = f
        dst = f'case ({i + 1})' + '\\' + fname
        # dst = os.path.join(f'case ({i + 1})', fname)
        print('src:', src)
        print('dst:', dst)
        shutil.move(src, dst)