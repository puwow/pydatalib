#-*- coding:utf-8 -*-

import os
import wx
import wx.aui as aui
import faker
from faker import Faker
from ImageSource import ImageSource as im

EVT_FAKER_TYPE = wx.NewEventType()
EVT_FAKER = wx.PyEventBinder( EVT_FAKER_TYPE, 1 )
class FakerEvent( wx.PyCommandEvent ):
    def __init__( self, eventType, id ):
        wx.PyCommandEvent.__init__( self, eventType, id )
        self.eventData = None
    def SetEventData( self, eventData ):
        self.eventData = eventData
    def GetEventData( self ):
        return self.eventData

class EntryPanel( wx.Panel ):
    def __init__( self, parent, id=wx.ID_ANY ):
        wx.Panel.__init__( self, parent=parent, id=id )
        self.tree = wx.TreeCtrl( self, id=wx.ID_ANY, style=wx.TR_DEFAULT_STYLE|wx.TR_HAS_BUTTONS|wx.TR_LINES_AT_ROOT|wx.TR_SINGLE|wx.TR_FULL_ROW_HIGHLIGHT )
        vbox = wx.BoxSizer( wx.VERTICAL )
        vbox.Add( self.tree, 1, wx.EXPAND )
        self.SetSizer( vbox )
        wx.CallAfter( self.initTree )
        self.images=wx.ImageList(16,16)
        self.images.Add( im.get_bitmap("database") )
        self.images.Add( im.get_bitmap("address") )
        self.images.Add( im.get_bitmap("car") )
        self.images.Add( im.get_bitmap("bank") )
        self.images.Add( im.get_bitmap("qrcode") )
        self.images.Add( im.get_bitmap("color") )
        self.images.Add( im.get_bitmap("company") )
        self.images.Add( im.get_bitmap("creditcard") )
        self.images.Add( im.get_bitmap("money") )
        self.images.Add( im.get_bitmap("time") )
        self.images.Add( im.get_bitmap("file") )
        self.images.Add( im.get_bitmap("coord") )
        self.images.Add( im.get_bitmap("network") )
        self.images.Add( im.get_bitmap("book") )
        self.images.Add( im.get_bitmap("work") )
        self.images.Add( im.get_bitmap("person") )
        self.images.Add( im.get_bitmap("code") )
        self.images.Add( im.get_bitmap("phone") )
        self.images.Add( im.get_bitmap("doc") )
        self.images.Add( im.get_bitmap("pcard") )
        self.images.Add( im.get_bitmap("platform") )
        self.images.Add( im.get_bitmap("default") )
        self.tree.AssignImageList(self.images )

    def initTree( self ):
        num=21
        root = self.tree.AddRoot('????????????', 0)

        addressNode = self.tree.AppendItem( root, '?????????', 1 )
        fullAddressNode = self.tree.AppendItem( addressNode, '??????', num, data='address')
        buildingAddressNode = self.tree.AppendItem( addressNode, '??????', num, data='building_number')
        cityAddressNode = self.tree.AppendItem( addressNode, '?????????(??????)', num, data='city')
        cityNameAddressNode = self.tree.AppendItem( addressNode, '?????????', num, data='city_name')
        countryAddressNode = self.tree.AppendItem( addressNode, '?????????', num, data='country')
        countryCodeAddressNode = self.tree.AppendItem( addressNode, '????????????', num, data='country_code(representation="alpha-2")')
        districtAddressNode = self.tree.AppendItem( addressNode, '??????', num, data='district')
        postCodeAddressNode = self.tree.AppendItem( addressNode, '??????', num, data='postcode')
        provinceAddressNode = self.tree.AppendItem( addressNode, '???', num, data='province')
        streetAddressNode = self.tree.AppendItem( addressNode, '??????', num, data='street_address')
        streetNameAddressNode = self.tree.AppendItem( addressNode, '????????????', num, data='street_name')

        carNode = self.tree.AppendItem( root, '?????????', 2 )
        licensePlateCarNode = self.tree.AppendItem( carNode, '??????', num, data="license_plate" )

        bankNode = self.tree.AppendItem( root, '?????????', 3 )
        ibanBankNode = self.tree.AppendItem( bankNode, '??????????????????', num, data='iban' )
        bbanBankNode = self.tree.AppendItem( bankNode, '??????????????????', num, data='bban' )
        countryBankNode = self.tree.AppendItem( bankNode, '??????????????????', num, data='bank_country' )

        eanNode = self.tree.AppendItem( root, '????????????', 4 )

        colorNode = self.tree.AppendItem( root, '?????????', 5 )
        nameColorNode = self.tree.AppendItem( colorNode, '????????????', num, data='color_name' )
        hexColorNode = self.tree.AppendItem( colorNode, '??????(????????????)', num, data='hex_color' )
        rgbColorNode = self.tree.AppendItem( colorNode, '??????(RGB)', num, data='rgb_color' )
        rgbCssColorNode = self.tree.AppendItem( colorNode, '??????(CSS)', num, data='rgb_css_color' )
        safeNameColorNode = self.tree.AppendItem( colorNode, '?????????', num, data='safe_color_name' )
        safeHexColorNode = self.tree.AppendItem( colorNode, '?????????(????????????)', num, data='safe_hex_color' )

        companyNode = self.tree.AppendItem( root, '?????????', 6 )
        nameCompanyNode = self.tree.AppendItem( companyNode, '????????????', num, data='company' )
        namePrefixCompanyNode = self.tree.AppendItem( companyNode, '????????????(??????)', num, data='company_prefix' )
        nameSuffixCompanyNode = self.tree.AppendItem( companyNode, '????????????(??????)', num, data='company_suffix' )

        creditNode = self.tree.AppendItem( root, '????????????', 7 )
        moneyNode = self.tree.AppendItem( root, '?????????', 8 )
        dateNode = self.tree.AppendItem( root, '?????????', 9 )
        fileNode = self.tree.AppendItem( root, '?????????', 10 )
        coordNode = self.tree.AppendItem( root, '?????????', 11 )
        netNode = self.tree.AppendItem( root, '?????????', 12 )

        bookNode = self.tree.AppendItem( root, '?????????', 13 )
        sibn10BookNode = self.tree.AppendItem( bookNode, 'ISBN-10????????????', num, data='isbn10(separator="-")')
        sibn13BookNode = self.tree.AppendItem( bookNode, 'ISBN-13????????????', num, data='isbn13(separator="-")')
        workNode = self.tree.AppendItem( root, '?????????', 14, data="job" )

        personNode = self.tree.AppendItem( root, '?????????', 15 )
        firstNamePersonNode = self.tree.AppendItem( personNode, '??????', num, data='first_name')
        firstNameFemalePersonNode = self.tree.AppendItem( personNode, '??????(???)', num, data='first_name_female')
        firstNameMalePersonNode = self.tree.AppendItem( personNode, '??????(???)', num, data='first_name_male')
        firstRomanizedNamePersonNode = self.tree.AppendItem( personNode, '??????(?????????)', num, data='first_romanized_name')
        lastNamePersonNode = self.tree.AppendItem( personNode, '???', num, data='last_name')
        lastNameFemalePersonNode = self.tree.AppendItem( personNode, '???(???)', num, data='last_name_female')
        lastNameMalePersonNode = self.tree.AppendItem( personNode, '???(???)', num, data='last_name_male')
        fullNamePersonNode = self.tree.AppendItem( personNode, '??????', num, data='name')
        fullNameFemalePersonNode = self.tree.AppendItem( personNode, '??????(???)', num, data='name_female')
        romanizedNamePersonNode = self.tree.AppendItem( personNode, '??????(?????????)', num, data='romanized_name')

        codeNode = self.tree.AppendItem( root, '?????????', 16 )

        phoneNode = self.tree.AppendItem( root, '?????????', 17 )
        msiPhoneNode = self.tree.AppendItem( phoneNode, '?????????', num, data='msisdn')
        numberPhoneNode = self.tree.AppendItem( phoneNode, '?????????', num, data='phone_number')
        prefixPhoneNode = self.tree.AppendItem( phoneNode, '??????', num, data='phonenumber_prefix')

        docNode = self.tree.AppendItem( root, '?????????', 18 )
        fullDocNode = self.tree.AppendItem( docNode, '????????????', num, data="profile" )
        simpleDocNode = self.tree.AppendItem( docNode, '????????????', num, data="simple_profile" )

        cardNode = self.tree.AppendItem( root, '????????????', 19 )

        platNode = self.tree.AppendItem( root, '?????????', 20 )
        androidNode = self.tree.AppendItem( platNode, 'Android', num, data="android_platform_token" )
        chromeNode = self.tree.AppendItem( platNode, 'Chrome', num, data="chrome" )
        firefoxNode = self.tree.AppendItem( platNode, 'FireFox', num, data="firefox" )
        ieNode = self.tree.AppendItem( platNode, 'IE', num, data="internet_explorer" )
        operaNode = self.tree.AppendItem( platNode, 'Opera', num, data="opera" )
        linuxNode = self.tree.AppendItem( platNode, 'Linux', num, data="linux_platform_token" )
        windowsNode = self.tree.AppendItem( platNode, 'Windows', num, data="windows_platform_token" )
        macNode = self.tree.AppendItem( platNode, 'Mac', num, data="mac_platform_token" )
        safariNode = self.tree.AppendItem( platNode, 'Safari', num, data="safari" )
        randPlatNode = self.tree.AppendItem( platNode, '??????', num, data="user_agent" )

        self.Bind( wx.EVT_TREE_SEL_CHANGED, self.OnChange, self.tree )
        self.tree.Expand(root)
    def OnChange( self, event ):
        item = self.tree.GetSelection()
        data = self.tree.GetItemData( item )
        if data:
            win = wx.FindWindowByName("result")
            evt = FakerEvent( EVT_FAKER_TYPE, self.tree.GetId())
            evt.SetEventData( data )
            wx.PostEvent(win, evt)

class ResultPanel( wx.Panel ):
    def __init__( self, parent, id=wx.ID_ANY, name="result" ):
        wx.Panel.__init__( self, parent=parent, id=id, name=name )
        self.locale = wx.Choice( self, id=wx.ID_ANY, choices=faker.factory.AVAILABLE_LOCALES )
        self.result = wx.TextCtrl( self, id=wx.ID_ANY, style=wx.TE_MULTILINE|wx.TE_READONLY )
        vbox = wx.BoxSizer( wx.VERTICAL )
        vbox.Add( self.locale, 0, wx.EXPAND )
        vbox.Add( self.result, 1, wx.EXPAND )
        self.SetSizer( vbox )

        self.Bind( EVT_FAKER, self.OnFaker )
        self.locale.SetStringSelection('zh_CN')
    def OnFaker( self, event ):
        _locale = self.locale.GetStringSelection()
        self._fake = faker.Faker(locale=_locale)
        eventData = event.GetEventData()
        if eventData.find('(') != -1:
            self.result.SetValue((eval("self._fake.%s"%(eventData))))
        else:
            self.result.SetValue((eval("self._fake.%s()"%(eventData))))

class DemoFrame( wx.Frame ):
    def __init__( self, parent=None, title='????????????', size=(800,600) ):
        wx.Frame.__init__( self, parent=parent, title=title, size=size )

        mainPanel = wx.Panel( self, id=wx.ID_ANY )
        self._mgr = aui.AuiManager(mainPanel)
        self._mgr.SetManagedWindow(mainPanel )

        entryPanel = EntryPanel( mainPanel )
        resultPanel = ResultPanel( mainPanel )

        self._mgr.AddPane(resultPanel, aui.AuiPaneInfo().Center().
                CloseButton(False))
        self._mgr.AddPane(entryPanel, aui.AuiPaneInfo().Left().
                CloseButton(False).
                MinSize(360,-1).
                BestSize(360,-1).
                Resizable(False))
        self._mgr.Update()

        self.Bind( wx.EVT_CLOSE, self.OnClose )
    def OnClose( self, event ):
        if self._mgr:
            self._mgr.UnInit()
        event.Skip()

if __name__ == '__main__':
    app = wx.App()
    frame = DemoFrame()
    frame.CenterOnParent()
    frame.Maximize()
    frame.Show()
    app.MainLoop()
