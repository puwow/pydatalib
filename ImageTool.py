#-*- coding:utf-8 -*-
#AUTH: QiaoGS
#DATE: 2021-03-11
#DESC: Generate Picture Data

import os
import re
import json
import base64
class ImageTool:
    def __init__( self, path ):
        self.path = path
    def GeneratePictureData( self ):
        data={}
        if os.path.exists( self.path ):
            for root,dirs,files in os.walk( self.path ):
                for f in files:
                    if re.match( r'.*.png', f ):
                        key = os.path.splitext(f)[0]
                        with open( os.path.join( root, f ), 'rb' ) as fp:
                            data[key]=base64.b64encode(fp.read())
        return data

if __name__ == '__main__':
    it=ImageTool('/home/qiaogs/pydatalib/images')
    data = it.GeneratePictureData()
    with open("ImageSource.py", "w") as fp:
        fp.write('''
#-*- coding:utf-8 -*-
import wx
import base64
class ImageSource:
    images=%s
    @classmethod
    def get_bitmap( cls, key ):
        return wx.Bitmap().FromPNGData( base64.b64decode(cls.images.get(key)))
if __name__ == '__main__':
    print(ImageSource.get_bitmap("car"))
        '''%(data))
                
