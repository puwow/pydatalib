#-*- coding:utf-8 -*-

import wx
import wx.aui as aui
import faker
from faker import Faker

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
    def initTree( self ):
        root = self.tree.AddRoot('数据仓库')

        addressNode = self.tree.AppendItem( root, '地址类' )
        fullAddressNode = self.tree.AppendItem( addressNode, '地址', data='address')
        buildingAddressNode = self.tree.AppendItem( addressNode, '楼号', data='building_number')
        cityAddressNode = self.tree.AppendItem( addressNode, '城市名(完整)', data='city')
        cityNameAddressNode = self.tree.AppendItem( addressNode, '城市名', data='city_name')
        countryAddressNode = self.tree.AppendItem( addressNode, '国家名', data='country')
        countryCodeAddressNode = self.tree.AppendItem( addressNode, '国家编码', data='country_code(representation="alpha-2")')
        districtAddressNode = self.tree.AppendItem( addressNode, '地区', data='district')
        postCodeAddressNode = self.tree.AppendItem( addressNode, '邮编', data='postcode')
        provinceAddressNode = self.tree.AppendItem( addressNode, '省', data='province')
        streetAddressNode = self.tree.AppendItem( addressNode, '街道', data='street_address')
        streetNameAddressNode = self.tree.AppendItem( addressNode, '街道名称', data='street_name')

        carNode = self.tree.AppendItem( root, '汽车类' )
        licensePlateCarNode = self.tree.AppendItem( carNode, '车牌', data="license_plate" )

        bankNode = self.tree.AppendItem( root, '银行类' )
        ibanBankNode = self.tree.AppendItem( bankNode, '国际银行代码', data='iban' )
        bbanBankNode = self.tree.AppendItem( bankNode, '基本银行账号', data='bban' )
        countryBankNode = self.tree.AppendItem( bankNode, '银行所属国家', data='bank_country' )

        eanNode = self.tree.AppendItem( root, '条形码类' )

        colorNode = self.tree.AppendItem( root, '颜色类' )
        nameColorNode = self.tree.AppendItem( colorNode, '颜色名称', data='color_name' )
        hexColorNode = self.tree.AppendItem( colorNode, '颜色(十六进制)', data='hex_color' )
        rgbColorNode = self.tree.AppendItem( colorNode, '颜色(RGB)', data='rgb_color' )
        rgbCssColorNode = self.tree.AppendItem( colorNode, '颜色(CSS)', data='rgb_css_color' )
        safeNameColorNode = self.tree.AppendItem( colorNode, '安全色', data='safe_color_name' )
        safeHexColorNode = self.tree.AppendItem( colorNode, '安全色(十六进制)', data='safe_hex_color' )

        companyNode = self.tree.AppendItem( root, '公司类' )
        nameCompanyNode = self.tree.AppendItem( companyNode, '公司名称', data='company' )
        namePrefixCompanyNode = self.tree.AppendItem( companyNode, '公司名称(前缀)', data='company_prefix' )
        nameSuffixCompanyNode = self.tree.AppendItem( companyNode, '公司名称(后缀)', data='company_suffix' )

        creditNode = self.tree.AppendItem( root, '信用卡类' )
        moneyNode = self.tree.AppendItem( root, '货币类' )
        dateNode = self.tree.AppendItem( root, '时间类' )
        fileNode = self.tree.AppendItem( root, '文件类' )
        coordNode = self.tree.AppendItem( root, '坐标类' )
        netNode = self.tree.AppendItem( root, '网络类' )

        bookNode = self.tree.AppendItem( root, '图书类' )
        sibn10BookNode = self.tree.AppendItem( bookNode, 'ISBN-10图书编号', data='isbn10(separator="-")')
        sibn13BookNode = self.tree.AppendItem( bookNode, 'ISBN-13图书编号', data='isbn13(separator="-")')
        workNode = self.tree.AppendItem( root, '职业类', data='job' )

        personNode = self.tree.AppendItem( root, '人物类' )
        firstNamePersonNode = self.tree.AppendItem( personNode, '名字', data='first_name')
        firstNameFemalePersonNode = self.tree.AppendItem( personNode, '名字(女)', data='first_name_female')
        firstNameMalePersonNode = self.tree.AppendItem( personNode, '名字(男)', data='first_name_male')
        firstRomanizedNamePersonNode = self.tree.AppendItem( personNode, '名字(罗马文)', data='first_romanized_name')
        lastNamePersonNode = self.tree.AppendItem( personNode, '姓', data='last_name')
        lastNameFemalePersonNode = self.tree.AppendItem( personNode, '姓(女)', data='last_name_female')
        lastNameMalePersonNode = self.tree.AppendItem( personNode, '姓(女)', data='last_name_male')
        fullNamePersonNode = self.tree.AppendItem( personNode, '姓名', data='name')
        fullNameFemalePersonNode = self.tree.AppendItem( personNode, '姓名(女)', data='name_female')
        romanizedNamePersonNode = self.tree.AppendItem( personNode, '称谓(罗马文)', data='romanized_name')

        codeNode = self.tree.AppendItem( root, '编码类' )

        phoneNode = self.tree.AppendItem( root, '电话类' )
        msiPhoneNode = self.tree.AppendItem( phoneNode, '手机号', data='msisdn')
        numberPhoneNode = self.tree.AppendItem( phoneNode, '手机号', data='phone_number')
        prefixPhoneNode = self.tree.AppendItem( phoneNode, '区号', data='phonenumber_prefix')

        docNode = self.tree.AppendItem( root, '档案类' )
        fullDocNode = self.tree.AppendItem( docNode, '完整档案', data="profile" )
        simpleDocNode = self.tree.AppendItem( docNode, '简单档案', data="simple_profile" )

        cardNode = self.tree.AppendItem( root, '身份证类' )

        platNode = self.tree.AppendItem( root, '平台类' )
        androidNode = self.tree.AppendItem( platNode, 'Android', data="android_platform_token" )
        chromeNode = self.tree.AppendItem( platNode, 'Chrome', data="chrome" )
        firefoxNode = self.tree.AppendItem( platNode, 'FireFox', data="firefox" )
        ieNode = self.tree.AppendItem( platNode, 'IE', data="internet_explorer" )
        operaNode = self.tree.AppendItem( platNode, 'Opera', data="opera" )
        linuxNode = self.tree.AppendItem( platNode, 'Linux', data="linux_platform_token" )
        windowsNode = self.tree.AppendItem( platNode, 'Windows', data="windows_platform_token" )
        macNode = self.tree.AppendItem( platNode, 'Mac', data="mac_platform_token" )
        safariNode = self.tree.AppendItem( platNode, 'Safari', data="safari" )
        randPlatNode = self.tree.AppendItem( platNode, '随机', data="user_agent" )

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
        self.result = wx.TextCtrl( self, id=wx.ID_ANY, style=wx.TE_MULTILINE|wx.TE_READONLY )
        vbox = wx.BoxSizer( wx.VERTICAL )
        vbox.Add( self.result, 1, wx.EXPAND )
        self.SetSizer( vbox )
        self._fake = faker.Faker(local='zh_CN')

        self.Bind( EVT_FAKER, self.OnFaker )
    def OnFaker( self, event ):
        eventData = event.GetEventData()
        if eventData.find('(') != -1:
            self.result.SetValue((eval("self._fake.%s"%(eventData))))
        else:
            self.result.SetValue((eval("self._fake.%s()"%(eventData))))

class DemoFrame( wx.Frame ):
    def __init__( self, parent=None, title='数据仓库', size=(800,600) ):
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
