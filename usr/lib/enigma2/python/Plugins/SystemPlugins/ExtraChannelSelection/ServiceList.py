# uncompyle6 version 3.9.3
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.13.9 (main, Oct 30 2025, 02:11:50) [GCC 13.3.0]
# Embedded file name: usr\lib\enigma2\python\Plugins\SystemPlugins\ExtraChannelSelection\ServiceList.py
# Compiled at: 2017-03-12 04:56:58
from Components.HTMLComponent import HTMLComponent
from Components.GUIComponent import GUIComponent
from enigma import iServiceInformation, eListboxServiceContent, eListbox, eServiceCenter, eServiceCenter_getInstance, eServiceReference, gFont, eRect, eEnv, eListboxPythonMultiContent, RT_WRAP, RT_VALIGN_TOP, RT_VALIGN_CENTER, RT_HALIGN_LEFT, RT_HALIGN_CENTER, RT_HALIGN_RIGHT, iServiceInformation, eEPGCache, eLabel, eSize, ePicLoad
from Tools.LoadPixmap import LoadPixmap
from Tools.Directories import resolveFilename, SCOPE_CURRENT_SKIN, fileExists, SCOPE_CURRENT_PLUGIN, SCOPE_SKIN_IMAGE
from Components.config import *
from ServiceReference import ServiceReference
from Components.MultiContent import MultiContentEntryText, MultiContentEntryPixmapAlphaBlend
from time import time, localtime
import NavigationInstance
from timer import TimerEntry
from skin import parseColor, parseFont
import Plugins.SystemPlugins.ExtraChannelSelection.plugin
from Plugins.SystemPlugins.ExtraChannelSelection.plugin import namehours, namemin
DOUBLE = False
try:
    if config.plugins.ExtraChannelSelection.listmode.value:
        DOUBLE = True
except:
    pass

DOUBL = False
try:
    if config.plugins.ExtraChannelSelection.doubmode.value:
        DOUBL = True
except:
    pass

def refreshServiceList(configElement=None):
    from Screens.InfoBar import InfoBar
    InfoBarInstance = InfoBar.instance
    if InfoBarInstance is not None:
        servicelist = InfoBarInstance.servicelist
        if servicelist:
            servicelist.setMode()
    return


class ServiceList(HTMLComponent, GUIComponent):
    if config.plugins.ExtraChannelSelection.piconpathmode.value == '0':
        PiconPaths = (
         '/usr/share/enigma2/picon/', '/media/cf/picon/', '/media/usb/picon/', '/media/ba/picon/', '/media/hdd/picon/', '/picon/')
    elif config.plugins.ExtraChannelSelection.piconpathmode.value == '1':
        PiconPaths = (
         '/media/usb/transparentpicon/',)
    elif config.plugins.ExtraChannelSelection.piconpathmode.value == '2':
        PiconPaths = (
         '/media/usb/blackpicon/',)
    elif config.plugins.ExtraChannelSelection.piconpathmode.value == '3':
        PiconPaths = (
         '/media/usb/whitepicon/',)
    elif config.plugins.ExtraChannelSelection.piconpathmode.value == '4':
        PiconPaths = (
         '/media/usb/colorpicon/',)
    elif config.plugins.ExtraChannelSelection.piconpathmode.value == '5':
        PiconPaths = (
         '/media/hdd/transparentpicon/',)
    elif config.plugins.ExtraChannelSelection.piconpathmode.value == '6':
        PiconPaths = (
         '/media/hdd/blackpicon/',)
    elif config.plugins.ExtraChannelSelection.piconpathmode.value == '7':
        PiconPaths = (
         '/media/hdd/whitepicon/',)
    elif config.plugins.ExtraChannelSelection.piconpathmode.value == '8':
        PiconPaths = (
         '/media/hdd/colorpicon/',)
    MODE_NORMAL = 0
    MODE_FAVOURITES = 1

    def __init__(self, serviceList):
        self.serviceList = serviceList
        GUIComponent.__init__(self)
        self.picFolder = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/folder.png'))
        self.picMarker = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/marker.png'))
        self.picDVB_S = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/ico_dvb_s-fs8.png'))
        self.picDVB_T = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/ico_dvb_t-fs8.png'))
        self.picDVB_C = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/ico_dvb_c-fs8.png'))
        self.picStream = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/ico_stream-fs8.png'))
        self.picServiceGroup = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/ico_service_group-fs8.png'))
        self.picCrypt = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt.png'))
        self.picCrypt2 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt2.png'))
        self.picCrypt3 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt3.png'))
        self.picCrypt4 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt4.png'))
        self.picCrypt5 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt5.png'))
        self.picCrypt6 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt6.png'))
        self.picCrypt7 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt7.png'))
        self.picCrypt8 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt8.png'))
        self.picCrypt9 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt9.png'))
        self.picCrypt10 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt10.png'))
        self.picCrypt11 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt11.png'))
        self.picCrypt12 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt12.png'))
        self.picCrypt13 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt13.png'))
        self.picCrypt14 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt14.png'))
        self.picCrypt15 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt15.png'))
        self.picRecord = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/record.png'))
        self.Bar = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/longbar5.png'))
        self.Bar1 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/longbar1.png'))
        self.Bar2 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/longbar2.png'))
        self.Bar3 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/longbar3.png'))
        self.Bar4 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/longbar4.png'))
        self.Bar5 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/longbar5.png'))
        self.Bar6 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/longbar6.png'))
        self.Bar7 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/longbar7.png'))
        self.Bar8 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/longbar8.png'))
        self.Bar9 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/longbar9.png'))
        self.Bar10 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/longbar10.png'))
        self.Bar11 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/longbar11.png'))
        self.picBar = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog9.png'))
        self.picBar1 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog1.png'))
        self.picBar2 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog2.png'))
        self.picBar3 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog3.png'))
        self.picBar4 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog4.png'))
        self.picBar5 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog5.png'))
        self.picBar6 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog6.png'))
        self.picBar7 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog7.png'))
        self.picBar8 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog8.png'))
        self.picBar9 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog9.png'))
        self.picBar10 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog10.png'))
        self.picBar11 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog11.png'))
        self.timerclock = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/clock.png'))
        self.markedForeground = 15774720
        self.markedBackground = 624318628
        self.markedForegroundSelected = 9437216
        self.markedBackgroundSelected = 624318628
        self.serviceNotAvail = 6710886
        self.eventForeground = 10519808
        self.eventForegroundSelected = 65535
        self.serviceNameForeground = 16777215
        self.serviceNameForegroundSelected = 16776960
        self.eventborderForeground = None
        self.serviceEventProgressbarColor = 5622089
        self.serviceEventProgressbarColorSelected = 4772300
        self.serviceEventProgressbarBorderColor = 6710886
        self.serviceEventProgressbarBorderColorSelected = 8421631
        self.l = eListboxPythonMultiContent()
        self.S = eListboxServiceContent()
        self.l.setBuildFunc(self.buildServiceList)
        self.l.setFont(0, gFont('Regular', 22))
        self.l.setFont(1, gFont('Regular', 18))
        self.l.setFont(2, gFont('Regular', 22))
        self.ServiceNameFont = gFont('Regular', 22)
        self.l.setFont(3, gFont('Regular', 20))
        self.l.setFont(4, gFont('Regular', 22))
        self.l.setFont(5, gFont('Regular', 20))
        self.l.setFont(6, gFont('Regular', 20))
        self.l.setFont(10, gFont('Regular', 17))
        self.l.setFont(7, gFont('Regular', 28))
        self.l.setFont(8, gFont('Regular', 18))
        self.l.setFont(9, gFont('Regular', 8))
        self.l.setFont(11, gFont('Regular', 20))
        self.l.setFont(12, gFont('Regular', 18))
        self.l.setFont(13, gFont('Regular', 21))
        self.list = []
        self.size = 0
        self.service_center = eServiceCenter.getInstance()
        self.numberoffset = 0
        self.is_playable_ignore = eServiceReference()
        self.current_marked = False
        self.marked = []
        self.marker_list = []
        self.l.lookupService = self.lookupService
        self.root = None
        self.mode = self.MODE_NORMAL
        if DOUBLE:
            self.ItemHeight = 60 if DOUBL else 48
        else:
            self.ItemHeight = 32
        self.l.setItemHeight(self.ItemHeight)
        self.onSelectionChanged = []
        return

    def checkRecording(self):
        self.waitrecordingServices = []
        if config.plugins.ExtraChannelSelection.recordmode.value != '0':
            if len(NavigationInstance.instance.RecordTimer.timer_list) != 0:
                for timer in NavigationInstance.instance.RecordTimer.timer_list:
                    if timer.state == TimerEntry.StateWaiting:
                        self.waitrecordingServices.append(str(timer.service_ref))
                    elif timer.state == TimerEntry.StatePrepared:
                        self.waitrecordingServices.append(str(timer.service_ref))

        return

    def findPicon(self, service=None):
        if config.plugins.ExtraChannelSelection.piconmode.value:
            if service is not None:
                import os, re, unicodedata
                from Tools.Alternatives import GetWithAlternative
                service = service.toString()
                service = ('_').join(GetWithAlternative(service).split(':', 10)[:10])
                for path in self.PiconPaths:
                    pngname = path + service + '.png'
                    if fileExists(pngname):
                        return pngname

                if not pngname:
                    fields = service.split('_', 3)
                    if len(fields) > 2:
                        if fields[0] != '1':
                            fields[0] = '1'
                            for path in self.PiconPaths:
                                pngname = path + ('_').join(fields) + '.png'
                                if fileExists(pngname):
                                    return pngname

                        if not pngname and fields[2] != '2':
                            fields[2] = '1'
                            for path in self.PiconPaths:
                                pngname = path + ('_').join(fields) + '.png'
                                if fileExists(pngname):
                                    return pngname

                if not pngname:
                    name = ServiceReference(service).getServiceName()
                    if isinstance(name, bytes):
                        name = name.decode('utf_8', errors='ignore')
                    name = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore').decode('ASCII')
                    name = re.sub('[^a-z0-9]', '', name.replace('&', 'and').replace('+', 'plus').replace('*', 'star').lower())
                    if name:
                        for path in self.PiconPaths:
                            pngname = path + name + '.png'
                            if fileExists(pngname):
                                return pngname
                            if not pngname and len(name) > 2 and name.endswith('hd'):
                                pngname = path + name[:-2] + '.png'
                                if fileExists(pngname):
                                    return pngname

        return

    def buildServiceList(self, service, **args):
        piconmode = config.plugins.ExtraChannelSelection.piconmode.value
        if piconmode:
            self.picon = ePicLoad()
            picon = self.findPicon(service)
            if picon is None:
                tmp = resolveFilename(SCOPE_CURRENT_SKIN, 'picon_default.png')
                picon = tmp if fileExists(tmp) else resolveFilename(SCOPE_SKIN_IMAGE, 'skin_default/picon_default.png')
            if DOUBLE:
                piconWidth = 100 if DOUBL else 75
                piconHeight = 60 if DOUBL else 45
            else:
                piconWidth = 50
                piconHeight = 30
            self.picon.setPara((piconWidth, piconHeight, 1, 1, False, 1, '#000f0f0f'))
            self.picon.startDecode(picon, 0, 0, False)
            picon2 = self.picon.getData()
        width = self.l.getItemSize().width()
        selected = True
        try:
            selected = args['selected']
        except:
            pass

        res = [
         None]
        service_info = self.service_center.info(service)
        isMarker = service.flags & eServiceReference.isMarker
        isPlayable = not (service.flags & eServiceReference.isDirectory or isMarker)
        recording = False
        pixmap = None
        pixico = None
        fontnum = config.plugins.ExtraChannelSelection.fontnum.value
        fontperc = config.plugins.ExtraChannelSelection.fontperc.value
        fontname = config.plugins.ExtraChannelSelection.fontname.value
        fontevent = config.plugins.ExtraChannelSelection.fontevent.value
        fontend = config.plugins.ExtraChannelSelection.fontend.value
        fontrem = config.plugins.ExtraChannelSelection.fontrem.value
        fonttxt = config.plugins.ExtraChannelSelection.fonttxt.value
        fontsat = config.plugins.ExtraChannelSelection.fontsat.value
        self.sizedict = {'1': 14, 
           '2': 15, 
           '3': 16, 
           '4': 17, 
           '5': 18, 
           '6': 19, 
           '7': 20, 
           '8': 21, 
           '9': 22, 
           '10': 23, 
           '11': 24, 
           '12': 25, 
           '13': 26, 
           '14': 27, 
           '15': 28, 
           '16': 29, 
           '17': 30, 
           '18': 31, 
           '19': 32}
        self.l.setFont(0, gFont('Regular', self.sizedict[fontnum])) if fontnum in self.sizedict else self.l.setFont(0, gFont('Regular', 22))
        self.l.setFont(1, gFont('Regular', self.sizedict[fontperc])) if fontperc in self.sizedict else self.l.setFont(1, gFont('Regular', 18))
        self.l.setFont(2, gFont('Regular', self.sizedict[fontname])) if fontname in self.sizedict else self.l.setFont(2, gFont('Regular', 22))
        self.ServiceNameFont = gFont('Regular', self.sizedict[fontname]) if fontname in self.sizedict else gFont('Regular', 22)
        self.l.setFont(3, gFont('Regular', self.sizedict[fontevent])) if fontevent in self.sizedict else self.l.setFont(3, gFont('Regular', 20))
        self.l.setFont(4, gFont('Regular', self.sizedict[fontend])) if fontend in self.sizedict else self.l.setFont(4, gFont('Regular', 22))
        self.l.setFont(5, gFont('Regular', self.sizedict[fontrem])) if fontrem in self.sizedict else self.l.setFont(5, gFont('Regular', 20))
        self.l.setFont(6, gFont('Regular', self.sizedict[fonttxt])) if fonttxt in self.sizedict else self.l.setFont(6, gFont('Regular', 20))
        self.l.setFont(10, gFont('Regular', self.sizedict[fontsat])) if fontsat in self.sizedict else self.l.setFont(10, gFont('Regular', 17))
        showline = config.plugins.ExtraChannelSelection.showline.value
        colshowline = config.plugins.ExtraChannelSelection.colshowline.value
        usagemode = config.plugins.ExtraChannelSelection.progress.value
        iconmode = config.plugins.ExtraChannelSelection.iconmode.value
        crypticonmode = config.plugins.ExtraChannelSelection.crypticonmode.value
        barmode = config.plugins.ExtraChannelSelection.barmode.value
        percmode = config.plugins.ExtraChannelSelection.percmode.value
        barpercmode = config.plugins.ExtraChannelSelection.barpercmode.value
        percshow = config.plugins.ExtraChannelSelection.percshow.value
        percpos = config.plugins.ExtraChannelSelection.percpos.value
        nummode = config.plugins.ExtraChannelSelection.nummode.value
        coltext = config.plugins.ExtraChannelSelection.coltext.value
        colnum = config.plugins.ExtraChannelSelection.colnum.value
        colselnum = config.plugins.ExtraChannelSelection.colselnum.value
        colend = config.plugins.ExtraChannelSelection.colend.value
        colselend = config.plugins.ExtraChannelSelection.colselend.value
        colremain = config.plugins.ExtraChannelSelection.colremain.value
        colselremain = config.plugins.ExtraChannelSelection.colselremain.value
        colsat = config.plugins.ExtraChannelSelection.colsat.value
        colselsat = config.plugins.ExtraChannelSelection.colselsat.value
        colbar = config.plugins.ExtraChannelSelection.colbar.value
        colbarsel = config.plugins.ExtraChannelSelection.colbarsel.value
        picbar = config.plugins.ExtraChannelSelection.picbar.value
        colborder = config.plugins.ExtraChannelSelection.colborder.value
        colbordersel = config.plugins.ExtraChannelSelection.colbordersel.value
        colname = config.plugins.ExtraChannelSelection.colname.value
        colnamesel = config.plugins.ExtraChannelSelection.colnamesel.value
        colperc = config.plugins.ExtraChannelSelection.colperc.value
        colpercsel = config.plugins.ExtraChannelSelection.colpercsel.value
        colevent = config.plugins.ExtraChannelSelection.colevent.value
        coleventsel = config.plugins.ExtraChannelSelection.coleventsel.value
        text = config.plugins.ExtraChannelSelection.text.value
        pixbar2 = config.plugins.ExtraChannelSelection.picbar.value
        self.colordict = {'1': 5636889, 
           '2': 1401021, 
           '3': 8421504, 
           '4': 3100495, 
           '5': 32896, 
           '6': 65535, 
           '7': 1644912, 
           '8': 4620980, 
           '9': 65280, 
           '10': 12632256, 
           '11': 36080, 
           '12': 16776960, 
           '13': 16711680, 
           '14': 16711935, 
           '15': 16777215, 
           '16': 255, 
           '17': 9127187, 
           '18': 14423100, 
           '19': 6908265, 
           '20': 13808780, 
           '21': 3050327, 
           '22': 16761035, 
           '23': 12211667, 
           '24': 13458524, 
           '25': 16444375, 
           '26': 65407, 
           '27': 4915330, 
           '28': 25600, 
           '29': 5597999, 
           '31': 0, 
           '32': 4144959, 
           '33': 1182351, 
           '34': 5003366, 
           '35': 1651533, 
           '36': 1709375, 
           '37': 2966878, 
           '38': 15053379, 
           '39': 33375, 
           '40': 4718847, 
           '41': 1472370, 
           '42': 10066329, 
           '43': 1138786, 
           '44': 2840687, 
           '45': 12213083, 
           '46': 3767640, 
           '47': 16034048}
        self.picdict = {'1': (self.picBar), 
           '2': (self.picBar11), 
           '3': (self.picBar1), 
           '4': (self.picBar2), 
           '5': (self.picBar3), 
           '6': (self.picBar4), 
           '7': (self.picBar5), 
           '8': (self.picBar6), 
           '9': (self.picBar7), 
           '10': (self.picBar8), 
           '11': (self.picBar9), 
           '12': (self.picBar10)}
        self.pixdict = {'1': (self.Bar), 
           '2': (self.Bar11), 
           '3': (self.Bar1), 
           '4': (self.Bar2), 
           '5': (self.Bar3), 
           '6': (self.Bar4), 
           '7': (self.Bar5), 
           '8': (self.Bar6), 
           '9': (self.Bar7), 
           '10': (self.Bar8), 
           '11': (self.Bar9), 
           '12': (self.Bar10)}
        if DOUBLE:
            if DOUBL:
                if pixbar2 in self.pixdict:
                    pixlong = self.pixdict[pixbar2]
        if text:
            txtColor = self.colordict[coltext] if coltext in self.colordict else self.markedForeground
        if barmode == '1':
            barColor = self.colordict[colbar] if colbar in self.colordict else self.serviceEventProgressbarColor
            barColorSel = self.colordict[colbarsel] if colbarsel in self.colordict else self.serviceEventProgressbarColorSelected
        elif barmode == '2':
            if picbar in self.picdict:
                pixbar = self.picdict[picbar]
            borderColorSel = self.colordict[colbordersel] if colbordersel in self.colordict else self.serviceEventProgressbarBorderColorSelected
        showlineColor = self.colordict[colshowline] if colshowline in self.colordict else 8421504
        borderColor = self.colordict[colborder] if colborder in self.colordict else self.serviceEventProgressbarBorderColor
        satColor = self.colordict[colsat] if colsat in self.colordict else 16444375
        satColorSel = self.colordict[colselsat] if colselsat in self.colordict else 16444375
        if not config.plugins.ExtraChannelSelection.colormode.value:
            numColor = self.colordict[colnum] if colnum in self.colordict else self.eventForeground
            numColorSel = self.colordict[colselnum] if colselnum in self.colordict else self.eventForegroundSelected
            nameColor = self.colordict[colname] if colname in self.colordict else self.serviceNameForeground
            nameColorSel = self.colordict[colnamesel] if colnamesel in self.colordict else self.serviceNameForegroundSelected
            percColor = self.colordict[colperc] if colperc in self.colordict else self.eventForeground
            percColorSel = self.colordict[colpercsel] if colpercsel in self.colordict else self.eventForegroundSelected
            eventColor = self.colordict[colevent] if colevent in self.colordict else self.eventForeground
            eventColorSel = self.colordict[coleventsel] if coleventsel in self.colordict else self.eventForegroundSelected
            if config.plugins.ExtraChannelSelection.listmode.value:
                endColor = self.colordict[colend] if colend in self.colordict else self.eventForeground
                endColorSel = self.colordict[colselend] if colselend in self.colordict else self.eventForegroundSelected
                remColor = self.colordict[colremain] if colremain in self.colordict else self.markedForeground
                remColorSel = self.colordict[colselremain] if colselremain in self.colordict else self.markedForegroundSelected
        else:
            numColor = self.eventForeground
            numColorSel = self.eventForegroundSelected
            endColor = self.eventForeground
            endColorSel = self.eventForegroundSelected
            remColor = self.markedForeground
            remColorSel = self.markedForegroundSelected
            nameColor = self.serviceNameForeground
            nameColorSel = self.serviceNameForegroundSelected
            percColor = self.eventForeground
            percColorSel = self.eventForegroundSelected
            eventColor = self.eventForeground
            eventColorSel = self.eventForegroundSelected
        notChannelMode = False
        if service.flags & eServiceReference.isMarker:
            pixmap = self.picMarker
            notChannelMode = True
            selected = False
        elif service.flags & eServiceReference.isGroup:
            pixmap = self.picServiceGroup
            notChannelMode = True
        elif service.flags & eServiceReference.isDirectory:
            pixmap = self.picFolder
            notChannelMode = True
        else:
            refstr = service.toString()
            if '%3a//' in refstr or refstr.startswith('4097:'):
                pixico = self.picStream
            if pixico != self.picStream:
                orbpos = service.getUnsignedData(4) >> 16
                if orbpos == 65535:
                    pixico = self.picDVB_C
                elif orbpos == 61166:
                    pixico = self.picDVB_T
                elif orbpos == 0:
                    pixico = self.picDVB_T
                else:
                    pixico = self.picDVB_S
        height = self.l.getItemSize().height()
        yDouble = height / 2
        marked = 0
        if self.current_marked and selected:
            marked = 2
        elif self.isMarked(service):
            if selected:
                marked = 2
            else:
                marked = 1
        if marked == 1:
            backgroundColor = backgroundColorSel = None
        elif marked == 2:
            numColorSel = nameColorSel = percColorSel = eventColorSel = endColorSel = remColorSel = foregroundColorSel = self.markedForegroundSelected
            backgroundColorSel = self.markedBackgroundSelected
            foregroundColor = serviceDescriptionColor = backgroundColor = None
        else:
            backgroundColor = backgroundColorSel = None
        if marked == 0 and isPlayable and service_info and self.is_playable_ignore.valid() and not service_info.isPlayable(service, self.is_playable_ignore):
            numColor = numColorSel = nameColor = nameColorSel = percColor = percColorSel = eventColor = eventColorSel = endColor = endColorSel = remColor = remColorSel = txtColor = self.serviceNotAvail
        addingResText = lambda a, b, c, d, e, f, g, h, o, p, r: res.append((eListboxPythonMultiContent.TYPE_TEXT, a, b, c, d, e, f, g, h, o, p, r))
        addingResPix = lambda a, b, c, d, e: res.append((eListboxPythonMultiContent.TYPE_PIXMAP_ALPHATEST, a, b, c, d, e))
        addingResPr = lambda a, b, c, d, e, f, g, h, o, p: res.append((eListboxPythonMultiContent.TYPE_PROGRESS, a, b, c, d, e, f, g, h, o, p))
        addingResPrPix = lambda a, b, c, d, e, f, g, h, o: res.append((eListboxPythonMultiContent.TYPE_PROGRESS_PIXMAP, a, b, c, d, e, f, g, h, o))
        rthr = RT_HALIGN_RIGHT
        rthcrtvc = RT_HALIGN_CENTER | RT_VALIGN_CENTER
        rthrrtvc = RT_HALIGN_RIGHT | RT_VALIGN_CENTER
        rthlrtvc = RT_HALIGN_LEFT | RT_VALIGN_CENTER
        if marked > 0:
            addingResText(0, 0, width, height, 1, rthr, '', foregroundColor, foregroundColorSel, backgroundColor, backgroundColorSel)
        info = self.service_center.info(service)
        serviceName = info.getName(service) or ServiceReference(service).getServiceName() or ''
        event = info.getEvent(service)
        index = self.getCurrentIndex()
        xPos = 4
        xPos1 = 4
        xPos2 = 4
        picomode = config.plugins.ExtraChannelSelection.picomode.value
        remmode = config.plugins.ExtraChannelSelection.remmode.value
        bordermode = config.plugins.ExtraChannelSelection.bordermode.value
        recordmode = config.plugins.ExtraChannelSelection.recordmode.value
        endmode = config.plugins.ExtraChannelSelection.endmode.value
        piccryptmode = config.plugins.ExtraChannelSelection.picicocrypt.value
        timericonmode = config.plugins.ExtraChannelSelection.timericonmode.value
        isCrypted = False
        if crypticonmode == '0':
            isCrypted = False
        else:
            isCrypted = service_info.isCrypted()
        isRecorded = False
        if recordmode == '0':
            isRecorded = False
        else:
            getrecord = eListboxServiceContent()
            isRecorded = isPlayable & getrecord.checkServiceIsRecorded(service)
        isWaitingTimer = False
        if timericonmode == '0':
            isWaitingTimer = False
        else:
            self.checkRecording()
            if service.toString() in self.waitrecordingServices:
                isWaitingTimer = True
        if pixmap is not None:
            pixmap_size = pixmap.size()
            yPos = (height - pixmap_size.height()) / 2
            pix_width = pixmap_size.width()
            pix_height = pixmap_size.height()
            addingResPix(xPos, yPos, pix_width, pix_height, pixmap)
            xPos += pix_width + 5
            xPos1 += pix_width + 5
        if pixico is not None:
            if iconmode == '1':
                pixico_size = pixico.size()
                yP = (height - pixico_size.height()) / 2
                pic_width = pixico_size.width()
                pic_height = pixico_size.height()
                addingResPix(xPos, yP, 30, pic_height, pixico)
                xPos += 30
                xPos1 += 30
                xPos2 = xPos
        if not nummode:
            pass
        elif self.mode != self.MODE_NORMAL:
            if not service.flags & eServiceReference.isMarker:
                markers_before = 0
                for markers in self.marker_list:
                    if index > markers:
                        markers_before += 1
                    else:
                        break

                num = '%d' % (self.numberoffset + index + 1 - markers_before)
                numCol = 16711680 if isRecorded else numColor
                numColSel = 16711680 if isRecorded else numColorSel
                if DOUBLE:
                    if recordmode == '3':
                        addingResText(xPos, 0, 60, height, 7, rthcrtvc, num, numCol, numColSel, backgroundColor, backgroundColorSel)
                        xPos += 63
                        xPos1 = xPos
                        xPos2 = xPos
                    else:
                        addingResText(xPos, 0, 60, height, 7, rthcrtvc, num, numColor, numColorSel, backgroundColor, backgroundColorSel)
                        xPos += 63
                        xPos1 = xPos
                        xPos2 = xPos
                elif recordmode == '3':
                    addingResText(xPos, 0, 45, height, 0, rthcrtvc, num, numCol, numColSel, backgroundColor, backgroundColorSel)
                    xPos += 50
                    xPos1 = xPos
                    xPos2 = xPos
                else:
                    addingResText(xPos, 0, 45, height, 0, rthcrtvc, num, numColor, numColorSel, backgroundColor, backgroundColorSel)
                    xPos += 50
                    xPos1 = xPos
                    xPos2 = xPos
        if piccryptmode == '1':
            icocrypt = self.picCrypt
        elif piccryptmode == '2':
            icocrypt = self.picCrypt2
        elif piccryptmode == '3':
            icocrypt = self.picCrypt3
        elif piccryptmode == '4':
            icocrypt = self.picCrypt4
        elif piccryptmode == '5':
            icocrypt = self.picCrypt5
        elif piccryptmode == '6':
            icocrypt = self.picCrypt6
        elif piccryptmode == '7':
            icocrypt = self.picCrypt7
        elif piccryptmode == '8':
            icocrypt = self.picCrypt8
        elif piccryptmode == '9':
            icocrypt = self.picCrypt9
        elif piccryptmode == '10':
            icocrypt = self.picCrypt10
        elif piccryptmode == '11':
            icocrypt = self.picCrypt11
        elif piccryptmode == '12':
            icocrypt = self.picCrypt12
        elif piccryptmode == '13':
            icocrypt = self.picCrypt13
        elif piccryptmode == '14':
            icocrypt = self.picCrypt14
        else:
            icocrypt = self.picCrypt15
        if not notChannelMode:
            bar = 0
            perc = ''
            if event and isPlayable:
                i = 100 * (int(time()) - event.getBeginTime()) / event.getDuration()
                if i < 101:
                    bar = i
                    perc = str(i) + '%' if percmode == '1' else '(' + str(i) + '%' + ')'
            if DOUBLE:
                if piconmode:
                    if picomode == '1':
                        a = xPos
                        e = 105 if DOUBL else 80
                    else:
                        a = width - 101 if DOUBL else width - 76
                        e = 0
                    if not DOUBL:
                        wt = 75
                        ht = 45
                        ot = 1
                    else:
                        wt = 100
                        ht = 60
                        ot = 0
                    addingResPix(a, ot, wt, ht, picon2)
                    xPos += e
                    xPos1 += e
                    xPos2 += e
                remain = ''
                if isPlayable:
                    self.renderLabel.setFont(self.ServiceNameFont)
                    self.renderLabel.setText(serviceName)
                    length = self.renderLabel.calculateSize().width() + 10
                    if remmode == '1' and event:
                        r = (event.getBeginTime() + event.getDuration()) / 60 - int(time() / 60)
                        remain = '(+' + str(r) + ' ' + namemin() + ')'
                    if remmode == '2' and event:
                        r = (event.getBeginTime() + event.getDuration()) / 60 - int(time() / 60)
                        rh = r / 60
                        rm = r - rh * 60
                        remain = '(+' + str(rh) + namehours() + str(rm) + namemin() + ')'
                    if not DOUBL:
                        if showline:
                            addingResText(0, height - 1, width, 1, 1, rthrrtvc, '', None, None, showlineColor, None)
                        if barmode == '1':
                            addingResPr(xPos, 8, 52, 8, bar, 1, barColor, barColorSel, backgroundColor, backgroundColorSel)
                            xPos += 57
                        else:
                            addingResPrPix(xPos, 8, 52, 8, bar, pixbar, 1, borderColor, borderColorSel)
                            xPos += 57
                        if percshow:
                            addingResText(xPos, 0, 60, height / 2, 1, rthcrtvc, perc, percColor, percColorSel, backgroundColor, backgroundColorSel)
                            xPos += 63
                        if crypticonmode == '1':
                            if isCrypted:
                                cryptpixmap_size = icocrypt.size()
                                pixx_width = cryptpixmap_size.width()
                                pixx_height = cryptpixmap_size.height()
                                if pixx_height < height / 2:
                                    ppp = (height / 2 - pixx_height) / 2
                                    ttt = pixx_height
                                else:
                                    ppp = 0
                                    ttt = height / 2
                                addingResPix(xPos, ppp, pixx_width, ttt, icocrypt)
                                xPos += pixx_width + 5
                        if timericonmode == '1':
                            if isWaitingTimer:
                                timerpixmap_size = self.timerclock.size()
                                pixtimer_width = timerpixmap_size.width()
                                pixtimer_height = timerpixmap_size.height()
                                if pixtimer_height < height / 2:
                                    jjk = (height / 2 - pixtimer_height) / 2
                                    hhj = pixtimer_height
                                else:
                                    jjk = 0
                                    hhj = height / 2
                                addingResPix(xPos, jjk, pixtimer_width, hhj, self.timerclock)
                                xPos += pixtimer_width + 10
                        if recordmode == '1':
                            if isRecorded:
                                recpixmap_size = self.picRecord.size()
                                pixrec_width = recpixmap_size.width()
                                pixrec_height = recpixmap_size.height()
                                if pixrec_height < height / 2:
                                    jjk = (height / 2 - pixrec_height) / 2
                                    hhj = pixrec_height
                                else:
                                    jjk = 0
                                    hhj = height / 2
                                addingResPix(xPos, jjk, pixrec_width, hhj, self.picRecord)
                                xPos += pixrec_width + 5
                        nameCol = 16711680 if isRecorded else nameColor
                        nameColSel = 16711680 if isRecorded else nameColorSel
                        addingResText(xPos, 0, length, yDouble, 2, rthlrtvc, serviceName, nameCol, nameColSel, backgroundColor, backgroundColorSel)
                        xPos += length
                        if pixico is not None:
                            if iconmode == '2':
                                pixico_size = pixico.size()
                                pic_width = pixico_size.width()
                                pic_height = pixico_size.height()
                                if pic_height < height / 2:
                                    lgh = (height / 2 - pic_height) / 2
                                    igj = pic_height
                                else:
                                    lgh = 0
                                    igj = height / 2
                                addingResPix(xPos, lgh, 30, igj, pixico)
                                xPos += 30
                        if crypticonmode == '2':
                            if isCrypted:
                                cryptpixmap_size = icocrypt.size()
                                pixx_width = cryptpixmap_size.width()
                                pixx_height = cryptpixmap_size.height()
                                if pixx_height < height / 2:
                                    iii = (height / 2 - pixx_height) / 2
                                    eee = pixx_height
                                else:
                                    iii = 0
                                    eee = height / 2
                                addingResPix(xPos, iii, pixx_width, eee, icocrypt)
                                xPos += pixx_width + 5
                        if timericonmode == '2':
                            if isWaitingTimer:
                                timerpixmap_size = self.timerclock.size()
                                pixtimer_width = timerpixmap_size.width()
                                pixtimer_height = timerpixmap_size.height()
                                if pixtimer_height < height / 2:
                                    jjk = (height / 2 - pixtimer_height) / 2
                                    hhj = pixtimer_height
                                else:
                                    jjk = 0
                                    hhj = height / 2
                                addingResPix(xPos + 2, jjk, pixtimer_width, hhj, self.timerclock)
                                xPos += pixtimer_width + 12
                        if recordmode == '2':
                            addingResText(xPos, 0, length, yDouble, 2, rthlrtvc, serviceName, nameColor, nameColorSel, backgroundColor, backgroundColorSel)
                            xPos += length
                            if isRecorded:
                                recpixmap_size = self.picRecord.size()
                                pixrec_width = recpixmap_size.width()
                                pixrec_height = recpixmap_size.height()
                                if pixrec_height < height / 2:
                                    jjk = (height / 2 - pixrec_height) / 2
                                    hhj = pixrec_height
                                else:
                                    jjk = 0
                                    hhj = height / 2
                                addingResPix(xPos, jjk, pixrec_width, hhj, self.picRecord)
                                xPos += pixrec_width + 5
                        if (remmode == '1' or remmode == '2') and event:
                            addingResText(xPos1, yDouble, 110, yDouble, 5, rthcrtvc, remain, remColor, remColorSel, None, None)
                            xPos1 += 115
                        if endmode and event:
                            begin = localtime(event.getBeginTime())
                            end = localtime(event.getBeginTime() + event.getDuration())
                            if piconmode:
                                ff = width - xPos if picomode == '1' else width - xPos - 85
                            else:
                                ff = width - xPos
                            addingResText(xPos, 3, ff, yDouble - 3, 4, rthlrtvc, '%02d.%02d - %02d.%02d' % (begin[3], begin[4], end[3], end[4]), endColor, endColorSel, backgroundColor, backgroundColorSel)
                    else:
                        if piconmode:
                            if picomode == '1':
                                cc = width - xPos
                                jj = length if length < width - xPos else width - xPos - 5
                            else:
                                cc = width - xPos - 101
                                jj = length if length < width - xPos - 105 else width - xPos - 105
                        else:
                            jj = length
                            cc = width - xPos
                        bd = 1 if bordermode else 0
                        addingResPrPix(xPos, 53, cc, 6, bar, pixlong, bd, None, None)
                        if remmode == '1' or remmode == '2':
                            addingResText(xPos1, 27, 110, 27, 5, rthcrtvc, remain, remColor, remColorSel, None, None)
                            xPos1 += 115
                        if crypticonmode == '1':
                            if isCrypted:
                                cryptpixmap_size = icocrypt.size()
                                pixx_width = cryptpixmap_size.width()
                                pixx_height = cryptpixmap_size.height()
                                if pixx_height < 27:
                                    ggg = (27 - pixx_height) / 2
                                    hhh = pixx_height
                                else:
                                    ggg = 0
                                    hhh = 27
                                addingResPix(xPos, ggg, pixx_width, hhh, icocrypt)
                                xPos += pixx_width + 5
                        self.renderLabel.setFont(self.ServiceNameFont)
                        self.renderLabel.setText(serviceName)
                        length = self.renderLabel.calculateSize().width() + 10
                        if timericonmode == '1':
                            if isWaitingTimer:
                                timerpixmap_size = self.timerclock.size()
                                pixtimer_width = timerpixmap_size.width()
                                pixtimer_height = timerpixmap_size.height()
                                if pixtimer_height < height / 2:
                                    jjk = (height / 2 - pixtimer_height) / 2
                                    hhj = pixtimer_height
                                else:
                                    jjk = 0
                                    hhj = height / 2
                                addingResPix(xPos + 2, jjk, pixtimer_width, hhj, self.timerclock)
                                xPos += pixtimer_width + 12
                        if recordmode == '1':
                            if isRecorded:
                                recpixmap_size = self.picRecord.size()
                                pixrec_width = recpixmap_size.width()
                                pixrec_height = recpixmap_size.height()
                                if pixrec_height < 27:
                                    jjk = (27 - pixrec_height) / 2
                                    hhj = pixrec_height
                                else:
                                    jjk = 0
                                    hhj = 27
                                addingResPix(xPos, jjk, pixrec_width, hhj, self.picRecord)
                                xPos += pixrec_width + 5
                        nameCol = 16711680 if isRecorded else nameColor
                        nameColSel = 16711680 if isRecorded else nameColorSel
                        addingResText(xPos, 0, jj, 27, 2, rthlrtvc, serviceName, nameCol, nameColSel, backgroundColor, backgroundColorSel)
                        xPos += jj + 5
                        if pixico is not None:
                            if iconmode == '2':
                                pixico_size = pixico.size()
                                pic_width = pixico_size.width()
                                pic_height = pixico_size.height()
                                if pic_height < height / 2:
                                    lgh = (height / 2 - pic_height) / 2
                                    igj = pic_height
                                else:
                                    lgh = 0
                                    igj = height / 2
                                addingResPix(xPos, lgh, 30, igj, pixico)
                                xPos += 30
                        if crypticonmode == '2':
                            if isCrypted:
                                cryptpixmap_size = icocrypt.size()
                                pixx_width = cryptpixmap_size.width()
                                pixx_height = cryptpixmap_size.height()
                                if pixx_height < height / 2:
                                    iii = (height / 2 - pixx_height) / 2
                                    eee = pixx_height
                                else:
                                    iii = 0
                                    eee = height / 2
                                addingResPix(xPos, iii, pixx_width, eee, icocrypt)
                                xPos += pixx_width + 5
                        if timericonmode == '2':
                            if isWaitingTimer:
                                timerpixmap_size = self.timerclock.size()
                                pixtimer_width = timerpixmap_size.width()
                                pixtimer_height = timerpixmap_size.height()
                                if pixtimer_height < height / 2:
                                    jjk = (height / 2 - pixtimer_height) / 2
                                    hhj = pixtimer_height
                                else:
                                    jjk = 0
                                    hhj = height / 2
                                addingResPix(xPos + 2, jjk, pixtimer_width, hhj, self.timerclock)
                                xPos += pixtimer_width + 12
                        if recordmode == '2' and isRecorded:
                            recpixmap_size = self.picRecord.size()
                            pixrec_width = recpixmap_size.width()
                            pixrec_height = recpixmap_size.height()
                            if pixrec_height < height / 2:
                                jjk = (height / 2 - pixrec_height) / 2
                                hhj = pixrec_height
                            else:
                                jjk = 0
                                hhj = height / 2
                            addingResPix(xPos, jjk, pixrec_width, hhj, self.picRecord)
                            xPos += pixrec_width + 5
                if endmode and event:
                    if piconmode:
                        if picomode == '1':
                            tnt = width - xPos if width - xPos > 0 else 0
                        else:
                            tnt = width - xPos - 105 if width - xPos - 105 > 0 else 0
                    else:
                        tnt = width - xPos
                    begin = localtime(event.getBeginTime())
                    end = localtime(event.getBeginTime() + event.getDuration())
                    addingResText(xPos, 2, tnt, 27, 4, rthlrtvc, '%02d.%02d - %02d.%02d' % (begin[3], begin[4], end[3], end[4]), endColor, endColorSel, backgroundColor, backgroundColorSel)
        elif isPlayable:
            self.renderLabel.setFont(self.ServiceNameFont)
            self.renderLabel.setText(serviceName)
            length = self.renderLabel.calculateSize().width() + 10
            if showline:
                addingResText(0, height - 1, width, 1, 1, rthrrtvc, '', None, None, showlineColor, None)
            if piconmode:
                ee = 0
                ss = 0
                if picomode == '1':
                    oo = xPos
                    pp = 1
                    ss = 60
                else:
                    oo = width - 47
                    pp = 2
                addingResPix(oo, pp, 50, 30, picon2)
                xPos += ss
                if barmode == '1' and usagemode != 'no':
                    if usagemode != 'barright':
                        qq = xPos
                        if not barpercmode:
                            ee = 57
                    else:
                        qq = width - 55 if picomode == '1' else width - 110
                    if not barpercmode:
                        ww = (height - 8) / 2 if 1 else height - 9
                        addingResPr(qq, ww, 52, 8, bar, 1, barColor, barColorSel, backgroundColor, backgroundColorSel)
                        xPos += ee
                    elif barmode == '2' and usagemode != 'no':
                        if usagemode != 'barright':
                            qq = xPos
                            if not barpercmode:
                                ee = 57
                        else:
                            qq = width - 55 if picomode == '1' else width - 110
                        ww = height - 9 if barpercmode else (height - 8) / 2
                        addingResPrPix(qq, ww, 52, 8, bar, pixbar, 1, borderColor, borderColorSel)
                        xPos += ee
                    if percshow:
                        ii = 0
                        if not barpercmode:
                            yy = height
                            uu = 1
                            if percpos == '1':
                                ii = 60
                                rr = xPos
                            elif picomode == '1':
                                if usagemode != 'barright':
                                    rr = width - 60
                                elif usagemode == 'barright':
                                    rr = width - 115
                            elif usagemode != 'barright':
                                rr = width - 115
                            elif usagemode == 'barright':
                                rr = width - 170
                        else:
                            yy = height - 12
                            uu = 8
                            if percpos == '1':
                                rr = xPos
                                ii = 60
                            else:
                                rr = width - 60 if picomode == '1' else width - 115
                        addingResText(rr, 0, 55, yy, uu, rthcrtvc, perc, percColor, percColorSel, backgroundColor, backgroundColorSel)
                        xPos += ii
                    if crypticonmode == '1':
                        if isCrypted:
                            cryptpixmap_size = icocrypt.size()
                            pixx_width = cryptpixmap_size.width()
                            pixx_height = cryptpixmap_size.height()
                            www = (height - pixx_height) / 2
                            addingResPix(xPos, www, pixx_width, pixx_height, icocrypt)
                            xPos += pixx_width + 5
                        else:
                            cryptpixmap_size = icocrypt.size()
                            pixx_width = cryptpixmap_size.width()
                            xPos += pixx_width + 5
                    if timericonmode == '1':
                        if isWaitingTimer:
                            timerpixmap_size = self.timerclock.size()
                            pixtimer_width = timerpixmap_size.width()
                            pixtimer_height = timerpixmap_size.height()
                            www = (height - pixtimer_height) / 2
                            addingResPix(xPos + 2, www, pixtimer_width, pixtimer_height, self.timerclock)
                            xPos += pixtimer_width + 12
                    if recordmode == '1':
                        if isRecorded:
                            recpixmap_size = self.picRecord.size()
                            pixrec_width = recpixmap_size.width()
                            pixrec_height = recpixmap_size.height()
                            kjj = (height - pixrec_height) / 2
                            addingResPix(xPos, kjj, pixrec_width, pixrec_height, self.picRecord)
                            xPos += pixrec_width + 5
                else:
                    ee = 0
                    if barmode == '1' and usagemode != 'no':
                        if usagemode != 'barright':
                            qq = xPos
                            if not barpercmode:
                                ee = 57
                        else:
                            qq = width - 55
                        ww = height - 9 if barpercmode else (height - 8) / 2
                        addingResPr(qq, ww, 52, 8, bar, 1, barColor, barColorSel, backgroundColor, backgroundColorSel)
                        xPos += ee
                    elif barmode == '2' and usagemode != 'no':
                        if usagemode != 'barright':
                            qq = xPos
                            if not barpercmode:
                                ee = 57
                        else:
                            qq = width - 55
                        ww = height - 9 if barpercmode else (height - 8) / 2
                        addingResPrPix(qq, ww, 52, 8, bar, pixbar, 1, borderColor, borderColorSel)
                        xPos += ee
                    if percshow:
                        ii = 0
                        if not barpercmode:
                            tt = 0
                            yy = height
                            uu = 1
                            if percpos == '1':
                                ii = 60
                                rr = xPos
                            elif usagemode != 'barright':
                                rr = width - 60
                            elif usagemode == 'barright':
                                rr = width - 115
                        else:
                            tt = 2
                            yy = height - 12
                            uu = 8
                            if percpos == '1':
                                rr = xPos
                                ii = 60
                            else:
                                rr = width - 60
                        addingResText(rr, tt, 55, yy, uu, rthcrtvc, perc, percColor, percColorSel, backgroundColor, backgroundColorSel)
                        xPos += ii
                    if crypticonmode == '1':
                        if isCrypted:
                            cryptpixmap_size = icocrypt.size()
                            pixx_width = cryptpixmap_size.width()
                            pixx_height = cryptpixmap_size.height()
                            www = (height - pixx_height) / 2
                            addingResPix(xPos, www, pixx_width, pixx_height, icocrypt)
                            xPos += pixx_width + 5
                        else:
                            cryptpixmap_size = icocrypt.size()
                            pixx_width = cryptpixmap_size.width()
                            xPos += pixx_width + 5
                    if timericonmode == '1':
                        if isWaitingTimer:
                            timerpixmap_size = self.timerclock.size()
                            pixtimer_width = timerpixmap_size.width()
                            pixtimer_height = timerpixmap_size.height()
                            www = (height - pixtimer_height) / 2
                            addingResPix(xPos + 2, www, pixtimer_width, pixtimer_height, self.timerclock)
                            xPos += pixtimer_width + 12
                    if recordmode == '1':
                        if isRecorded:
                            recpixmap_size = self.picRecord.size()
                            pixrec_width = recpixmap_size.width()
                            pixrec_height = recpixmap_size.height()
                            kjj = (height - pixrec_height) / 2
                            addingResPix(xPos, kjj, pixrec_width, pixrec_height, self.picRecord)
                            xPos += pixrec_width + 5
                nameCol = 16711680 if isRecorded else nameColor
                nameColSel = 16711680 if isRecorded else nameColorSel
                addingResText(xPos + 4, 0, length, height, 2, rthlrtvc, serviceName, nameCol, nameColSel, backgroundColor, backgroundColorSel)
                xPos += length
                if pixico is not None:
                    if iconmode == '2':
                        pixico_size = pixico.size()
                        yPos = (height - pixico_size.height()) / 2
                        pix_width = pixico_size.width()
                        addingResPix(xPos, yPos, 30, height, pixico)
                        xPos += 30
                if crypticonmode == '2':
                    if isCrypted:
                        cryptpixmap_size = icocrypt.size()
                        pixx_width = cryptpixmap_size.width()
                        pixx_height = cryptpixmap_size.height()
                        www = (height - pixx_height) / 2
                        addingResPix(xPos, www, pixx_width, pixx_height, icocrypt)
                        xPos += pixx_width + 5
                if timericonmode == '2':
                    if isWaitingTimer:
                        timerpixmap_size = self.timerclock.size()
                        pixtimer_width = timerpixmap_size.width()
                        pixtimer_height = timerpixmap_size.height()
                        www = (height - pixtimer_height) / 2
                        addingResPix(xPos + 2, www, pixtimer_width, pixtimer_height, self.timerclock)
                        xPos += pixtimer_width + 12
                if recordmode == '2':
                    if isRecorded:
                        recpixmap_size = self.picRecord.size()
                        pixrec_width = recpixmap_size.width()
                        pixrec_height = recpixmap_size.height()
                        kjj = (height - pixrec_height) / 2
                        addingResPix(xPos, kjj, pixrec_width, pixrec_height, self.picRecord)
                        xPos += pixrec_width + 5
        if event and isPlayable:
            begin = localtime(event.getBeginTime())
            end = localtime(event.getBeginTime() + event.getDuration())
            eventmode = config.plugins.ExtraChannelSelection.eventmode.value
            percpos = config.plugins.ExtraChannelSelection.percpos.value
            if eventmode == '1':
                eventname = '%s' % event.getEventName()
            elif eventmode == '2':
                eventname = '(%s)' % event.getEventName()
            elif eventmode == '3':
                eventname = '-%s' % event.getEventName()
            if DOUBLE:
                if not DOUBL:
                    if piconmode:
                        hh = width - xPos1 - 5 if picomode == '1' else width - xPos1 - 85
                    else:
                        hh = width - xPos1 - 5
                    addingResText(xPos1, yDouble, hh, yDouble, 3, rthlrtvc, eventname, eventColor, eventColorSel, backgroundColor, backgroundColorSel)
                else:
                    if piconmode:
                        bn = width - xPos1 - 5 if picomode == '1' else width - xPos1 - 105
                    else:
                        bn = width - xPos1 - 5
                    addingResText(xPos1, 27, bn, 27, 3, rthlrtvc, eventname, eventColor, eventColorSel, backgroundColor, backgroundColorSel)
            elif usagemode == 'barright':
                if percshow:
                    if not barpercmode:
                        if percpos == '1':
                            if piconmode:
                                kk = width - xPos - 60 if picomode == '1' else width - xPos - 120
                            else:
                                kk = width - xPos - 60
                        elif piconmode:
                            kk = width - xPos - 120 if picomode == '1' else width - xPos - 175
                        else:
                            kk = width - xPos - 120
                    elif piconmode:
                        kk = width - xPos - 60 if picomode == '1' else width - xPos - 120
                    else:
                        kk = width - xPos - 60
                elif piconmode:
                    kk = width - xPos - 60 if picomode == '1' else width - xPos - 120
                else:
                    kk = width - xPos - 60
            if usagemode != 'barright':
                if percshow:
                    if not barpercmode:
                        if percpos == '1':
                            if piconmode:
                                kk = width - xPos if picomode == '1' else width - xPos - 60
                            else:
                                kk = width - xPos
                        elif piconmode:
                            kk = width - xPos - 60 if picomode == '1' else width - xPos - 115
                        else:
                            kk = width - xPos - 60
                    elif piconmode:
                        kk = width - xPos if picomode == '1' else width - xPos - 60
                    else:
                        kk = width - xPos
                elif piconmode:
                    kk = width - xPos - 60 if picomode == '1' else width - xPos - 120
                else:
                    kk = width - xPos - 60
            addingResText(xPos, 0, kk, height, 3, rthlrtvc, eventname, eventColor, eventColorSel, backgroundColor, backgroundColorSel)
        elif DOUBLE:
            notEpg = _('No EPG data available')
            if notChannelMode:
                addingResText(xPos + 5, 5, width - xPos - 10, height, 10, rthlrtvc, serviceName, satColor, satColorSel, backgroundColor, backgroundColorSel)
            elif text:
                if DOUBL:
                    nn = 27
                    if piconmode:
                        mm = width - xPos2 if picomode == '1' else width - xPos - 105
                    else:
                        mm = width - xPos2
                    qw = 27
                    we = 6
                else:
                    nn = 22
                    if piconmode:
                        mm = width - xPos2 if picomode == '1' else width - xPos2 - 105
                    else:
                        mm = width - xPos2
                    qw = 20
                    we = 12
                addingResText(xPos2, nn, mm, qw, we, rthlrtvc, notEpg, txtColor, 16444375, backgroundColor, backgroundColorSel)
        else:
            self.renderLabel.setFont(self.ServiceNameFont)
            self.renderLabel.setText(serviceName)
            length = self.renderLabel.calculateSize().width() + 10
            notEpg = _('No EPG data available')
            if notChannelMode:
                addingResText(xPos + 5, 0, width - xPos - 10, height, 10, rthlrtvc, serviceName, satColor, satColorSel, backgroundColor, backgroundColorSel)
            elif DOUBLE:
                if not DOUBL:
                    if text:
                        if piconmode:
                            er = width - xPos2 - 5 if picomode == '1' else width - xPos2 - 65
                        else:
                            width - xPos2 - 5
                        addingResText(xPos2, yDouble, er, yDouble, 6, rthlrtvc, notEpg, txtColor, 16444375, backgroundColor, backgroundColorSel)
                elif text:
                    if piconmode:
                        rt = width - xPos1 if picomode == '1' else width - xPos1 - 105
                    else:
                        rt = width - xPos1
                    addingResText(xPos1, 27, rt, 27, 6, rthlrtvc, notEpg, txtColor, 16444375, backgroundColor, backgroundColorSel)
            elif text:
                if usagemode == 'barright':
                    if percshow:
                        if not barpercmode:
                            if percpos == '1':
                                if piconmode:
                                    ty = width - xPos - 60 if picomode == '1' else width - xPos - 120
                                else:
                                    ty = width - xPos - 60
                            elif piconmode:
                                ty = width - xPos - 120 if picomode == '1' else width - xPos - 175
                            else:
                                ty = width - xPos - 120
                        elif piconmode:
                            ty = width - xPos - 60 if picomode == '1' else width - xPos - 120
                        else:
                            ty = width - xPos - 60
                    elif piconmode:
                        ty = width - xPos - 60 if picomode == '1' else width - xPos - 120
                    else:
                        ty = width - xPos - 60
                if usagemode != 'barright':
                    if percshow:
                        if not barpercmode:
                            if percpos == '1':
                                if piconmode:
                                    ty = width - xPos if picomode == '1' else width - xPos - 60
                                else:
                                    ty = width - xPos
                            elif piconmode:
                                ty = width - xPos - 60 if picomode == '1' else width - xPos - 115
                            else:
                                ty = width - xPos - 60
                        elif piconmode:
                            ty = width - xPos if picomode == '1' else width - xPos - 60
                        else:
                            ty = width - xPos
                    elif piconmode:
                        ty = width - xPos - 60 if picomode == '1' else width - xPos - 120
                    else:
                        ty = width - xPos - 60
                addingResText(xPos, 0, ty, height, 6, rthlrtvc, notEpg, txtColor, 16444375, backgroundColor, backgroundColorSel)
        return res

    def applySkin(self, desktop, parent):
        attribs = []
        if self.skinAttributes is not None:
            attribs = []
            for attrib, value in self.skinAttributes:
                if attrib == 'foregroundColorMarked':
                    self.markedForeground = parseColor(value).argb()
                elif attrib == 'foregroundColorMarkedSelected':
                    self.markedForegroundSelected = parseColor(value).argb()
                elif attrib == 'backgroundColorMarked':
                    self.markedBackground = parseColor(value).argb()
                elif attrib == 'backgroundColorMarkedSelected':
                    self.markedBackgroundSelected = parseColor(value).argb()
                elif attrib == 'foregroundColorServiceNotAvail':
                    self.serviceNotAvail = parseColor(value).argb()
                elif attrib == 'foregroundColorEvent' or attrib == 'colorServiceDescription':
                    self.eventForeground = parseColor(value).argb()
                elif attrib == 'foregroundColorEventSelected' or attrib == 'colorServiceDescriptionSelected':
                    self.eventForegroundSelected = parseColor(value).argb()
                elif attrib == 'foregroundColorEventborder':
                    pass
                elif attrib == 'foregroundColorEventborderSelected':
                    pass
                elif attrib == 'colorEventProgressbar':
                    self.colorEventProgressbar = parseColor(value).argb()
                elif attrib == 'colorEventProgressbarSelected':
                    self.serviceEventProgressbarColorSelected = parseColor(value).argb()
                elif attrib == 'colorEventProgressbarBorder':
                    self.serviceEventProgressbarBorderColor = parseColor(value).argb()
                elif attrib == 'colorEventProgressbarBorderSelected':
                    self.serviceEventProgressbarBorderColorSelected = parseColor(value).argb()
                elif attrib == 'colorServiceRecorded':
                    pass
                elif attrib == 'colorFallbackItem':
                    pass
                elif attrib == 'colorServiceSelectedFallback':
                    pass
                elif attrib == 'colorServiceDescriptionFallback':
                    pass
                elif attrib == 'colorServiceDescriptionSelectedFallback':
                    pass
                elif attrib == 'picServiceEventProgressbar':
                    self.picBar = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_SKIN, value))
                elif attrib == 'serviceItemHeight':
                    if DOUBLE:
                        if DOUBL:
                            self.ItemHeight = 60
                        else:
                            self.ItemHeight = 48
                    else:
                        self.ItemHeight = int(value)
                elif attrib == 'serviceNameFont':
                    try:
                        fontname = config.plugins.ExtraChannelSelection.fontname.value
                        fontend = config.plugins.ExtraChannelSelection.fontend.value
                        if fontname == '11':
                            self.l.setFont(2, parseFont(value, ((1, 1), (1, 1))))
                            self.ServiceNameFont = parseFont(value, ((1, 1), (1, 1)))
                        if fontend == '11':
                            self.l.setFont(4, parseFont(value, ((1, 1), (1, 1))))
                    except:
                        pass

                elif attrib == 'serviceInfoFont':
                    try:
                        fontevent = config.plugins.ExtraChannelSelection.fontevent.value
                        fontrem = config.plugins.ExtraChannelSelection.fontrem.value
                        fonttxt = config.plugins.ExtraChannelSelection.fonttxt.value
                        if fontevent == '11':
                            self.l.setFont(3, parseFont(value, ((1, 1), (1, 1))))
                        if fontrem == '11':
                            self.l.setFont(5, parseFont(value, ((1, 1), (1, 1))))
                        if fonttxt == '11':
                            self.l.setFont(6, parseFont(value, ((1, 1), (1, 1))))
                    except:
                        pass

                elif attrib == 'serviceNumberFont':
                    fontnum = config.plugins.ExtraChannelSelection.fontnum.value
                    if fontnum == '11':
                        self.l.setFont(0, parseFont(value, ((1, 1), (1, 1))))
                    fontperc = config.plugins.ExtraChannelSelection.fontperc.value
                    if fontperc == '11':
                        self.l.setFont(1, parseFont(value, ((1, 1), (1, 1))))
                elif attrib == 'progressbarHeight':
                    pass
                elif attrib == 'progressbarBorderWidth':
                    pass
                elif attrib == 'progressBarWidth':
                    pass
                elif attrib == 'progressPercentWidth':
                    pass
                elif attrib == 'fieldMargins':
                    pass
                elif attrib == 'nonplayableMargins':
                    pass
                elif attrib == 'itemsDistances':
                    pass
                else:
                    attribs.append((attrib, value))

            self.skinAttributes = attribs
        return GUIComponent.applySkin(self, desktop, parent)

    def connectSelChanged(self, fnc):
        if fnc not in self.onSelectionChanged:
            self.onSelectionChanged.append(fnc)
        return

    def disconnectSelChanged(self, fnc):
        if fnc in self.onSelectionChanged:
            self.onSelectionChanged.remove(fnc)
        return

    def selectionChanged(self):
        for i in self.onSelectionChanged:
            i()

        return

    def setCurrent(self, ref, adjust=True):
        index = 0
        x = 0
        for i in self.list:
            if i[0] == ref:
                index = x
                break
            x += 1

        self.instance.moveSelectionTo(index)
        return

    def getCurrent(self):
        r = eServiceReference()
        cur = self.l.getCurrentSelection()
        return cur and cur[0] or r

    def getPrev(self):
        return

    def getNext(self):
        return

    def setFontsize(self):
        return

    def setItemsPerPage(self):
        return

    def atBegin(self):
        if self.list:
            return self.instance.atBegin()
        else:
            return True

        return

    def atEnd(self):
        if self.list:
            return self.instance.atEnd()
        else:
            return True

        return

    def servicePageUp(self):
        cur = None
        if self.current_marked:
            cur = self.l.getCurrentSelection()
        self.instance.moveSelection(self.instance.pageUp)
        if self.current_marked:
            self.changePage(cur)
        return

    def servicePageDown(self):
        cur = None
        if self.current_marked:
            cur = self.l.getCurrentSelection()
        self.instance.moveSelection(self.instance.pageDown)
        if self.current_marked:
            self.changePage(cur)
        return

    def changePage(self, cur):
        if cur and cur[0]:
            index = self.getCurrentIndex()
            self.list.remove(cur)
            self.list.insert(index, cur)
            self.buildMarkerList()
            self.l.invalidate()
        return

    def moveUp(self):
        if self.current_marked:
            cur = self.l.getCurrentSelection()
            if cur and cur[0]:
                index = self.list.index(cur)
                newindex = index - 1
                if newindex < 0:
                    self.list.remove(cur)
                    self.list.append(cur)
                    self.buildMarkerList()
                else:
                    self.updateList(index, newindex)
        self.instance.moveSelection(self.instance.moveUp)
        return

    def moveDown(self):
        if self.current_marked:
            cur = self.l.getCurrentSelection()
            if cur and cur[0]:
                index = self.list.index(cur)
                newindex = index + 1
                list_size = len(self.list) - 1
                if newindex > list_size:
                    self.list.remove(cur)
                    self.list.insert(0, cur)
                    self.buildMarkerList()
                else:
                    self.updateList(index, newindex)
        self.instance.moveSelection(self.instance.moveDown)
        return

    def updateList(self, index, newindex):
        service1 = self.list[index][0]
        service2 = self.list[newindex][0]
        tmp = self.list[index]
        self.list[index] = self.list[newindex]
        self.list[newindex] = tmp
        if service1.flags & eServiceReference.isMarker or service2.flags & eServiceReference.isMarker:
            self.buildMarkerList()
        return

    def getNextBeginningWithChar(self, char):
        found = False
        index = 0
        for i in self.list:
            service = i[0]
            info = self.service_center.info(service)
            serviceName = info.getName(service) or ServiceReference(service).getServiceName() or ''
            if serviceName != '':
                idx = 0
                length = len(serviceName) - 1
                while idx <= length:
                    sn = serviceName[idx]
                    if ord(sn) >= 33 and ord(sn) < 127:
                        if sn == char:
                            found = True
                        break
                    idx += 1

            if found:
                break
            else:
                index += 1

        return index

    def moveToChar(self, char):
        print('Next char: ')
        index = self.getNextBeginningWithChar(char)
        indexup = self.getNextBeginningWithChar(char.upper())
        if indexup != 0:
            if index > indexup or index == 0:
                index = indexup
        self.instance.moveSelectionTo(index)
        print('Moving to character ' + str(char))
        return

    def moveToNextMarker(self):
        index = self.getCurrentIndex()
        idx = self.size - 1
        for marker in self.marker_list:
            if index < marker:
                idx = marker
                break

        self.instance.moveSelectionTo(idx)
        return

    def moveToPrevMarker(self):
        index = self.getCurrentIndex()
        idx = 0
        for marker in reversed(self.marker_list):
            if index > marker:
                idx = marker
                break

        self.instance.moveSelectionTo(idx)
        return

    def moveToIndex(self, index):
        self.instance.moveSelectionTo(index)
        return

    def getCurrentIndex(self):
        return self.instance.getCurrentIndex()

    GUI_WIDGET = eListbox

    def postWidgetCreate(self, instance):
        instance.setWrapAround(True)
        instance.setContent(self.l)
        instance.selectionChanged.get().append(self.selectionChanged)
        self.setMode(self.mode)
        self.renderLabel = eLabel(self.instance)
        self.renderLabel.resize(eSize(450, 0))
        self.renderLabel.hide()
        return

    def preWidgetRemove(self, instance):
        instance.setContent(None)
        instance.selectionChanged.get().remove(self.selectionChanged)
        return

    def getRoot(self):
        return self.root

    def getRootServices(self):
        serviceHandler = eServiceCenter.getInstance()
        list = serviceHandler.list(self.root)
        dest = []
        if list is not None:
            while 1:
                y = list.getNext()
                if not y.valid():
                    break
                dest.append(y.toString())

        return dest

    def setNumberOffset(self, offset):
        self.numberoffset = offset
        return

    def setPlayableIgnoreService(self, ref):
        self.is_playable_ignore = ref
        return

    def setRoot(self, root, justSet=False):
        self.root = root
        self.list = []
        if justSet:
            self.l.setList(self.list)
            self.size = 0
            return
        serviceref = root.toString()
        self.marker_list = []
        list = self.service_center.list(self.root)
        list = list.getContent('R', True)
        index = 0
        for i in list:
            self.list.append((i,))
            if i.flags & eServiceReference.isMarker:
                self.marker_list.append(index)
            index += 1

        self.finishFill(sort=False)
        self.selectionChanged()
        return

    def resetRoot(self):
        self.s = eListboxServiceContent()
        index = self.instance.getCurrentIndex()
        self.s.setRoot(self.root, False)
        self.s.sort()
        self.instance.moveSelectionTo(index)
        return

    def removeCurrent(self):
        if self.list:
            cur = self.l.getCurrentSelection()
            if cur and cur[0]:
                self.list.remove(cur)
                self.size -= 1
                self.buildMarkerList()
                self.l.invalidate()
        return

    def buildMarkerList(self):
        index = 0
        self.marker_list = []
        for service in self.list:
            if service[0].flags & eServiceReference.isMarker:
                self.marker_list.append(index)
            index += 1

        return

    def addService(self, service, beforeCurrent=False):
        if beforeCurrent and self.size:
            index = self.getCurrentIndex()
            self.list.insert(index, (service,))
        else:
            self.list.append((service,))
        self.buildMarkerList()
        self.size += 1
        self.l.invalidate()
        return

    def finishFill(self, sort=True):
        self.renderLabel.setFont(self.ServiceNameFont)
        self.size = len(self.list)
        if sort:
            self.list.sort(self.sortList)
        self.l.setList(self.list)
        self.instance.moveSelectionTo(0)
        return

    def sortList(self, a, b):
        return cmp(a[0].getUnsignedData(4), b[0].getUnsignedData(4))

    def clearMarks(self):
        self.marked = []
        return

    def isMarked(self, ref):
        try:
            index = self.marked.index(ref)
            return True
        except ValueError:
            return False

        return

    def addMarked(self, ref):
        self.marked.append(ref)
        self.l.invalidateEntry(self.getCurrentIndex())
        return

    def removeMarked(self, ref):
        self.marked.remove(ref)
        self.l.invalidateEntry(self.getCurrentIndex())
        return

    def getMarked(self):
        return [marks.toString() for marks in self.marked]

    def lookupService(self, ref):
        index = 0
        for i in self.list:
            if i[0] == ref:
                return index
            index += 1

        return index

    def setCurrentMarked(self, state):
        prev = self.current_marked
        self.current_marked = state
        if state != prev:
            if not state:
                list = self.service_center.list(self.root)
                if list is not None:
                    mutableList = list.startEdit()
                    if mutableList:
                        position = self.getCurrentIndex()
                        cur = self.l.getCurrentSelection()
                        if cur and cur[0]:
                            mutableList.moveService(cur[0], position)
            self.l.invalidateEntry(self.getCurrentIndex())
        return

    def setMode(self, mode):
        self.mode = mode
        self.l.setItemHeight(self.ItemHeight)
        return

