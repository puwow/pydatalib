#-*- coding:utf-8 -*-

import wx

class DemoFrame( wx.Frame ):
    def __init__( self, parent=None, title='数据仓库', size=(800,600) ):
        wx.Frame.__init__( self, parent=parent, title=title, size=size )

if __name__ == '__main__':
    app = wx.App()
    frame = DemoFrame()
    frame.Show()
    app.MainLoop()
