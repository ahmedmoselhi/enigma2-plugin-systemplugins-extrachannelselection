# uncompyle6 version 3.9.3
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.13.9 (main, Oct 30 2025, 02:11:50) [GCC 13.3.0]
# Embedded file name: /usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/TestScreen.py
# Compiled at: 2019-08-31 08:36:44
from enigma import eListboxPythonMultiContent, RT_HALIGN_RIGHT, RT_VALIGN_CENTER, gFont, RT_HALIGN_LEFT, ePicLoad, RT_HALIGN_CENTER, getDesktop, gRGB
from Tools.LoadPixmap import LoadPixmap
from Tools.Directories import resolveFilename, SCOPE_CURRENT_SKIN, fileExists, SCOPE_CURRENT_PLUGIN, SCOPE_SKIN_IMAGE, SCOPE_PLUGINS
from Components.MenuList import MenuList
from Components.MultiContent import MultiContentEntryText, MultiContentEntryPixmapAlphaTest, MultiContentEntryProgress, MultiContentEntryProgressPixmap
from Components.config import *
import Plugins.SystemPlugins.ExtraChannelSelection.plugin
from Components.Language import language
from skin import parseColor
from xml.dom.minidom import parse, Element
import os, gettext
PluginLanguageDomain = 'ExtraChannelSelection'
PluginLanguagePath = 'SystemPlugins/ExtraChannelSelection/locale'

def localeInit():
    gettext.bindtextdomain(PluginLanguageDomain, resolveFilename(SCOPE_PLUGINS, PluginLanguagePath))
    return


def _(txt):
    if gettext.dgettext(PluginLanguageDomain, txt):
        return gettext.dgettext(PluginLanguageDomain, txt)
    else:
        print '[' + PluginLanguageDomain + '] fallback to default translation for ' + txt
        return gettext.gettext(txt)

    return


language.addCallback(localeInit())

class TestScreenList(MenuList):

    def __init__(self, list, enableWrapAround=False):
        MenuList.__init__(self, list, enableWrapAround, eListboxPythonMultiContent)
        sizeSkin = getDesktop(0).size().width()
        if sizeSkin == 1920:
            self.l.setItemHeight(180)
            self.l.setFont(0, gFont('Regular', 32))
            self.l.setFont(1, gFont('Regular', 27))
            self.l.setFont(2, gFont('Regular', 32))
            self.l.setFont(3, gFont('Regular', 33))
            self.l.setFont(4, gFont('Regular', 32))
            self.l.setFont(5, gFont('Regular', 30))
            self.l.setFont(6, gFont('Regular', 30))
            self.l.setFont(10, gFont('Regular', 29))
        else:
            self.l.setItemHeight(120)
            self.l.setFont(0, gFont('Regular', 22))
            self.l.setFont(1, gFont('Regular', 18))
            self.l.setFont(2, gFont('Regular', 22))
            self.l.setFont(3, gFont('Regular', 22))
            self.l.setFont(4, gFont('Regular', 20))
            self.l.setFont(5, gFont('Regular', 22))
            self.l.setFont(6, gFont('Regular', 20))
            self.l.setFont(10, gFont('Regular', 18))
        return


def TestScreenListEntry(enabled, endmode, text, nummode, bordermode, barpercmode, iconmode, crypticonmode, doubmode, progress, percpos, remmode, showline, colshowline, coltext, colormode, piconmode, picomode, bigpicomode, listmode, barmode, picbar, picicocrypt, linemode, percshow, percmode, eventmode, recordmode, colremain, colselremain, colnum, colselnum, colend, colselend, colbar, colbarsel, colborder, colbordersel, colname, colnamesel, colperc, colpercsel, colevent, coleventsel, colsat, colselsat):
    name = _('CHASSE et PECHE')
    name2 = _('CNN')
    name3 = _('Cinemax')
    sizeSkin = getDesktop(0).size().width()
    if sizeSkin == 1920:
        picDVB_S = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/ico_dvb_s-fs8hd.png'))
        picBar = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog99.png'))
        picBar1 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog111.png'))
        picBar2 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog22.png'))
        picBar3 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog33.png'))
        picBar4 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog44.png'))
        picBar5 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog55.png'))
        picBar6 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog66.png'))
        picBar7 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog77.png'))
        picBar8 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog88.png'))
        picBar9 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog99.png'))
        picBar10 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog100.png'))
        picBar11 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog1111.png'))
    else:
        picDVB_S = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/ico_dvb_s-fs8.png'))
        picBar = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog9.png'))
        picBar1 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog1.png'))
        picBar2 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog2.png'))
        picBar3 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog3.png'))
        picBar4 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog4.png'))
        picBar5 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog5.png'))
        picBar6 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog6.png'))
        picBar7 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog7.png'))
        picBar8 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog8.png'))
        picBar9 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog9.png'))
        picBar10 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog10.png'))
        picBar11 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/bar_prog11.png'))
    picCrypt = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt.png'))
    picCrypt2 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt2.png'))
    picCrypt3 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt3.png'))
    picCrypt4 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt4.png'))
    picCrypt5 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt5.png'))
    picCrypt6 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt6.png'))
    picCrypt7 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt7.png'))
    picCrypt8 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt8.png'))
    picCrypt9 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt9.png'))
    picCrypt10 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt10.png'))
    picCrypt11 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt11.png'))
    picCrypt12 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt12.png'))
    picCrypt13 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt13.png'))
    picCrypt14 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt14.png'))
    picCrypt15 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/icon_crypt15.png'))
    pixico = picDVB_S
    Bar = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/longbar5.png'))
    Bar1 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/longbar1.png'))
    Bar2 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/longbar2.png'))
    Bar3 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/longbar3.png'))
    Bar4 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/longbar4.png'))
    Bar5 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/longbar5.png'))
    Bar6 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/longbar6.png'))
    Bar7 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/longbar7.png'))
    Bar8 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/longbar8.png'))
    Bar9 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/longbar9.png'))
    Bar10 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/longbar10.png'))
    Bar11 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/longbar11.png'))
    picstrel = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_PLUGIN, 'SystemPlugins/ExtraChannelSelection/images/strel.png'))
    enabled = enabled
    endmode = endmode
    text = text
    nummode = nummode
    bordermode = bordermode
    barpercmode = barpercmode
    iconmode = iconmode
    crypticonmode = crypticonmode
    doubmode = doubmode
    progress = progress
    percpos = percpos
    remmode = remmode
    showline = showline
    colshowline = colshowline
    coltext = coltext
    colormode = colormode
    piconmode = piconmode
    picomode = picomode
    bigpicomode = bigpicomode
    listmode = listmode
    barmode = barmode
    picbar = picbar
    pixbar2 = picbar
    picicocrypt = picicocrypt
    linemode = linemode
    percshow = percshow
    percmode = percmode
    eventmode = eventmode
    recordmode = recordmode
    colremain = colremain
    colselremain = colselremain
    colnum = colnum
    colselnum = colselnum
    colend = colend
    colselend = colselend
    colbar = colbar
    colbarsel = colbarsel
    colborder = colborder
    colbordersel = colbordersel
    colname = colname
    colnamesel = colnamesel
    colperc = colperc
    colpercsel = colpercsel
    colevent = colevent
    coleventsel = coleventsel
    colsat = colsat
    colselsat = colselsat
    picons = ePicLoad()
    picons2 = ePicLoad()
    picons3 = ePicLoad()
    pico = '/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/images/pico1.png'
    pico2 = '/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/images/pico2.png'
    pico3 = '/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/images/pico3.png'
    if picicocrypt == '1':
        icocrypt = picCrypt
    elif picicocrypt == '2':
        icocrypt = picCrypt2
    elif picicocrypt == '3':
        icocrypt = picCrypt3
    elif picicocrypt == '4':
        icocrypt = picCrypt4
    elif picicocrypt == '5':
        icocrypt = picCrypt5
    elif picicocrypt == '6':
        icocrypt = picCrypt6
    elif picicocrypt == '7':
        icocrypt = picCrypt7
    elif picicocrypt == '8':
        icocrypt = picCrypt8
    elif picicocrypt == '9':
        icocrypt = picCrypt9
    elif picicocrypt == '10':
        icocrypt = picCrypt10
    elif picicocrypt == '11':
        icocrypt = picCrypt11
    elif picicocrypt == '12':
        icocrypt = picCrypt12
    elif picicocrypt == '13':
        icocrypt = picCrypt13
    elif picicocrypt == '14':
        icocrypt = picCrypt14
    else:
        icocrypt = picCrypt15
    if sizeSkin == 1920:
        if listmode:
            if bigpicomode == '2':
                picons.setPara((150,
                 90,
                 1,
                 1,
                 False,
                 1,
                 '#000f0f0f'))
                picons2.setPara((150,
                 90,
                 1,
                 1,
                 False,
                 1,
                 '#000f0f0f'))
                picons3.setPara((150,
                 90,
                 1,
                 1,
                 False,
                 1,
                 '#000f0f0f'))
            elif bigpicomode == '1':
                picons.setPara((100,
                 60,
                 1,
                 1,
                 False,
                 1,
                 '#000f0f0f'))
                picons2.setPara((100,
                 60,
                 1,
                 1,
                 False,
                 1,
                 '#000f0f0f'))
                picons3.setPara((100,
                 60,
                 1,
                 1,
                 False,
                 1,
                 '#000f0f0f'))
        elif linemode == '1':
            picons.setPara((100,
             60,
             1,
             1,
             False,
             1,
             '#000f0f0f'))
            picons2.setPara((100,
             60,
             1,
             1,
             False,
             1,
             '#000f0f0f'))
            picons3.setPara((100,
             60,
             1,
             1,
             False,
             1,
             '#000f0f0f'))
        elif linemode == '2':
            picons.setPara((80,
             48,
             1,
             1,
             False,
             1,
             '#000f0f0f'))
            picons2.setPara((80,
             48,
             1,
             1,
             False,
             1,
             '#000f0f0f'))
            picons3.setPara((80,
             48,
             1,
             1,
             False,
             1,
             '#000f0f0f'))
    elif listmode:
        if doubmode:
            picons.setPara((100,
             60,
             1,
             1,
             False,
             1,
             '#000f0f0f'))
            picons2.setPara((100,
             60,
             1,
             1,
             False,
             1,
             '#000f0f0f'))
            picons3.setPara((100,
             60,
             1,
             1,
             False,
             1,
             '#000f0f0f'))
        else:
            picons.setPara((75,
             45,
             1,
             1,
             False,
             1,
             '#000f0f0f'))
            picons2.setPara((75,
             45,
             1,
             1,
             False,
             1,
             '#000f0f0f'))
            picons3.setPara((75,
             45,
             1,
             1,
             False,
             1,
             '#000f0f0f'))
    else:
        picons.setPara((50,
         30,
         1,
         1,
         False,
         1,
         '#000f0f0f'))
        picons2.setPara((50,
         30,
         1,
         1,
         False,
         1,
         '#000f0f0f'))
        picons3.setPara((50,
         30,
         1,
         1,
         False,
         1,
         '#000f0f0f'))
    picons.startDecode(pico, 0, 0, False)
    picons2.startDecode(pico2, 0, 0, False)
    picons3.startDecode(pico3, 0, 0, False)
    picon = picons.getData()
    picon2 = picons2.getData()
    picon3 = picons3.getData()
    colordict = {'1': 1813988, '2': 1401021, 
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
       '32': 10263708, 
       '33': 10329501, 
       '34': 8553090, 
       '35': 1651533, 
       '36': 1913674, 
       '37': 3493235, 
       '38': 15706442, 
       '39': 33646, 
       '40': 6684927, 
       '41': 1540205, 
       '42': 10263708, 
       '43': 13421823, 
       '44': 2778232, 
       '45': 12344664, 
       '46': 4227693, 
       '47': 16034048}
    picdict = {'1': picBar, '2': picBar11, 
       '3': picBar1, 
       '4': picBar2, 
       '5': picBar3, 
       '6': picBar4, 
       '7': picBar5, 
       '8': picBar6, 
       '9': picBar7, 
       '10': picBar8, 
       '11': picBar9, 
       '12': picBar10}
    pixdict = {'1': Bar, '2': Bar11, 
       '3': Bar1, 
       '4': Bar2, 
       '5': Bar3, 
       '6': Bar4, 
       '7': Bar5, 
       '8': Bar6, 
       '9': Bar7, 
       '10': Bar8, 
       '11': Bar9, 
       '12': Bar10}
    if listmode:
        if doubmode:
            if pixbar2 in pixdict:
                pixlong = pixdict[pixbar2]
    markedForeground = 15774720
    markedForegroundSelected = 9437216
    eventForeground = 10519808
    eventForegroundSelected = 65535
    serviceEventProgressbarColor = 5622089
    serviceEventProgressbarColorSelected = 4772300
    serviceEventProgressbarBorderColor = 6710886
    serviceEventProgressbarBorderColorSelected = 8421631
    nameForeground = 16777215
    nameForegroundSelected = 16776960
    colo = '/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/colors.xml'
    coloo = parse(colo)
    coloor = coloo.getElementsByTagName('colors')
    for ele in coloor:
        widgets = ele.getElementsByTagName('color')
        for el in widgets:
            if el.getAttribute('name') == '1':
                eventForeg = el.getAttribute('value')
                if not eventForeg == '':
                    eventForeground = parseColor(eventForeg).argb()
            elif el.getAttribute('name') == '2':
                eventForegSel = el.getAttribute('value')
                if not eventForegSel == '':
                    eventForegroundSelected = parseColor(eventForegSel).argb()

    if text:
        txtColor = colordict[coltext] if coltext in colordict else markedForeground
    if barmode == '1':
        barColor = colordict[colbar] if colbar in colordict else serviceEventProgressbarColor
        barColorSel = colordict[colbarsel] if colbarsel in colordict else serviceEventProgressbarColorSelected
    elif barmode == '2':
        if picbar in picdict:
            pixbar = picdict[picbar]
        borderColorSel = colordict[colbordersel] if colbordersel in colordict else serviceEventProgressbarBorderColorSelected
    showlineColor = colordict[colshowline] if colshowline in colordict else 8421504
    borderColor = colordict[colborder] if colborder in colordict else serviceEventProgressbarBorderColor
    satColor = colordict[colsat] if colsat in colordict else 16444375
    satColorSel = colordict[colselsat] if colselsat in colordict else 16444375
    if not colormode:
        numColor = colordict[colnum] if colnum in colordict else eventForeground
        numColorSel = colordict[colselnum] if colselnum in colordict else eventForegroundSelected
        nameColor = colordict[colname] if colname in colordict else nameForeground
        nameColorSel = colordict[colnamesel] if colnamesel in colordict else nameForegroundSelected
        percColor = colordict[colperc] if colperc in colordict else eventForeground
        percColorSel = colordict[colpercsel] if colpercsel in colordict else eventForegroundSelected
        eventColor = colordict[colevent] if colevent in colordict else eventForeground
        eventColorSel = colordict[coleventsel] if coleventsel in colordict else eventForegroundSelected
        if listmode:
            endColor = colordict[colend] if colend in colordict else eventForeground
            endColorSel = colordict[colselend] if colselend in colordict else eventForegroundSelected
            remColor = colordict[colremain] if colremain in colordict else markedForeground
            remColorSel = colordict[colselremain] if colselremain in colordict else markedForegroundSelected
    else:
        numColor = eventForeground
        numColorSel = eventForegroundSelected
        endColor = eventForeground
        endColorSel = eventForegroundSelected
        remColor = markedForeground
        remColorSel = markedForegroundSelected
        nameColor = nameForeground
        nameColorSel = nameForegroundSelected
        percColor = eventForeground
        percColorSel = eventForegroundSelected
        eventColor = eventForeground
        eventColorSel = eventForegroundSelected
    res = [
     name]
    xPos = 4
    xPos1 = 4
    xPos2 = 4
    x2Pos = 4
    x2Pos1 = 4
    x2Pos2 = 4
    x3Pos = 4
    x3Pos1 = 4
    x3Pos2 = 4
    rthl = RT_HALIGN_LEFT
    rthcrtvc = RT_HALIGN_CENTER | RT_VALIGN_CENTER
    rthlrtvc = RT_HALIGN_LEFT | RT_VALIGN_CENTER
    addingText = lambda a, b, c, d, e, f, g, h: res.append(MultiContentEntryText(pos=(a, b), size=(c, d), flags=e, font=f, text=g, backcolor=h))
    addingText2 = lambda a, b, c, d, e, f, g, h, l: res.append(MultiContentEntryText(pos=(a, b), size=(c, d), flags=e, font=f, text=g, color=h, color_sel=l))
    addingPix = lambda a, b, c, d, e: res.append(MultiContentEntryPixmapAlphaTest(pos=(a, b), size=(c, d), png=e))
    addingPr = lambda a, b, c, d, e, f, g: res.append(MultiContentEntryProgress(pos=(a, b), size=(c, d), percent=e, borderWidth=f, foreColor=g))
    addingPrPix = lambda a, b, c, d, e, f, g, h: res.append(MultiContentEntryProgressPixmap(pos=(a, b), size=(c, d), percent=e, pixmap=f, borderWidth=g, foreColor=h))
    if showline:
        if sizeSkin == 1920:
            if listmode:
                addingText(0, 89, 1110, 1, rthl, 0, '', showlineColor)
            elif linemode != '2':
                addingText(0, 59, 1110, 1, rthl, 0, '', showlineColor)
                addingText(0, 119, 1110, 1, rthl, 0, '', showlineColor)
            else:
                addingText(0, 47, 1110, 1, rthl, 0, '', showlineColor)
                addingText(0, 95, 1110, 1, rthl, 0, '', showlineColor)
                addingText(0, 143, 1110, 1, rthl, 0, '', showlineColor)
        elif listmode:
            if doubmode:
                addingText(0, 59, 740, 1, rthl, 0, '', showlineColor)
            else:
                addingText(0, 47, 740, 1, rthl, 0, '', showlineColor)
                addingText(0, 95, 740, 1, rthl, 0, '', showlineColor)
        else:
            addingText(0, 31, 740, 1, rthl, 0, '', showlineColor)
            addingText(0, 63, 740, 1, rthl, 0, '', showlineColor)
    if iconmode == '1':
        pixico_size = pixico.size()
        pic_width = pixico_size.width()
        pic_height = pixico_size.height()
        if sizeSkin == 1920:
            if listmode:
                yP = (90 - pixico_size.height()) / 2
                addingPix(xPos + 10, yP, 35, pic_height, pixico)
                addingPix(x2Pos + 10, yP + 90, 35, pic_height, pixico)
            elif linemode != '2':
                yP = (60 - pixico_size.height()) / 2
                addingPix(xPos + 10, yP, 35, pic_height, pixico)
                addingPix(x2Pos + 10, yP + 60, 35, pic_height, pixico)
                addingPix(x3Pos + 10, yP + 120, 35, pic_height, pixico)
            else:
                yP = (48 - pixico_size.height()) / 2
                addingPix(xPos + 10, yP, 35, pic_height, pixico)
                addingPix(x2Pos + 10, yP + 48, 35, pic_height, pixico)
                addingPix(x3Pos + 10, yP + 96, 35, pic_height, pixico)
            xPos += 55
            xPos1 += 55
            xPos2 += 55
            x2Pos += 55
            x2Pos1 += 55
            x2Pos2 += 55
            x3Pos += 55
            x3Pos1 += 55
            x3Pos2 += 55
        else:
            if listmode:
                if doubmode:
                    yP = (60 - pixico_size.height()) / 2
                    addingPix(xPos, yP, 30, pic_height, pixico)
                    addingPix(x2Pos, yP + 60, 30, pic_height, pixico)
                else:
                    yP = (48 - pixico_size.height()) / 2
                    addingPix(xPos, yP, 30, pic_height, pixico)
                    addingPix(x2Pos, yP + 48, 30, pic_height, pixico)
            else:
                yP = (32 - pixico_size.height()) / 2
                addingPix(xPos, yP, 30, pic_height, pixico)
                addingPix(x2Pos, yP + 32, 30, pic_height, pixico)
                addingPix(x2Pos, yP + 64, 30, pic_height, pixico)
            xPos += 35
            xPos1 += 35
            xPos2 += 35
            x2Pos += 35
            x2Pos1 += 35
            x2Pos2 += 35
            x3Pos += 35
            x3Pos1 += 35
            x3Pos2 += 35
    if nummode:
        if sizeSkin == 1920:
            if listmode:
                addingText2(xPos, 0, 55, 90, rthcrtvc, 0, '1', numColor, numColorSel)
                addingText2(x2Pos, 90, 55, 90, rthcrtvc, 0, '2', numColorSel, numColorSel)
            elif linemode != '2':
                addingText2(xPos, 0, 55, 60, rthcrtvc, 0, '1', numColor, numColorSel)
                addingText2(x2Pos, 60, 55, 60, rthcrtvc, 0, '2', numColorSel, numColorSel)
                addingText2(x3Pos, 120, 55, 60, rthcrtvc, 0, '3', numColor, numColorSel)
            else:
                addingText2(xPos, 0, 55, 48, rthcrtvc, 0, '1', numColor, numColorSel)
                addingText2(x2Pos, 48, 55, 48, rthcrtvc, 0, '2', numColorSel, numColorSel)
                addingText2(x3Pos, 96, 55, 48, rthcrtvc, 0, '3', numColor, numColorSel)
            xPos += 65
            xPos1 += 65
            xPos2 += 65
            x2Pos += 65
            x2Pos1 += 65
            x2Pos2 += 65
            x3Pos += 65
            x3Pos1 += 65
            x3Pos2 += 65
        else:
            if listmode:
                if doubmode:
                    addingText2(xPos, 0, 45, 60, rthcrtvc, 0, '1', numColor, numColorSel)
                    addingText2(x2Pos, 60, 45, 60, rthcrtvc, 0, '2', numColorSel, numColorSel)
                else:
                    addingText2(xPos, 0, 45, 48, rthcrtvc, 0, '1', numColor, numColorSel)
                    addingText2(x2Pos, 48, 45, 48, rthcrtvc, 0, '2', numColorSel, numColorSel)
            else:
                addingText2(xPos, 0, 45, 32, rthcrtvc, 0, '1', numColor, numColorSel)
                addingText2(x2Pos, 32, 45, 32, rthcrtvc, 0, '2', numColorSel, numColorSel)
                addingText2(x3Pos, 64, 45, 32, rthcrtvc, 0, '3', numColor, numColorSel)
            xPos += 50
            xPos1 += 50
            xPos2 += 50
            x2Pos += 50
            x2Pos1 += 50
            x2Pos2 += 50
            x3Pos += 50
            x3Pos1 += 50
            x3Pos2 += 50
    if sizeSkin == 1920:
        if listmode:
            selec = _('This is selected channel')
            addingPix(1150, 120, 42, 32, picstrel)
            addingText2(1210, 120, 530, 32, rthlrtvc, 0, selec, numColor, numColorSel)
            if piconmode:
                if bigpicomode == '1':
                    wt = 100
                    ht = 60
                    a = xPos if picomode == '1' else 1009
                    e = 110 if picomode == '1' else 0
                    ot = 14
                    addingPix(a, ot, wt, ht, picon)
                    addingPix(a, ot + 90, wt, ht, picon2)
                    xPos += e
                    xPos1 += e
                    xPos2 += e
                    x2Pos += e
                    x2Pos1 += e
                    x2Pos2 += e
                    x3Pos += e
                    x3Pos1 += e
                    x3Pos2 += e
                elif bigpicomode == '2':
                    wtt = 150
                    htt = 90
                    att = xPos if picomode == '1' else 959
                    ett = 160 if picomode == '1' else 0
                    ott = 0
                    addingPix(att, ott, wtt, htt, picon)
                    addingPix(att, ott + 90, wtt, htt, picon2)
                    xPos += ett
                    xPos1 += ett
                    xPos2 += ett
                    x2Pos += ett
                    x2Pos1 += ett
                    x2Pos2 += ett
                    x3Pos += ett
                    x3Pos1 += ett
                    x3Pos2 += ett
            if not doubmode:
                if barmode == '1':
                    addingPr(xPos + 3, 17, 75, 12, 53, 1, barColor)
                    addingPr(x2Pos + 3, 110, 75, 12, 37, 1, barColorSel)
                    xPos += 85
                    x2Pos += 85
                else:
                    addingPrPix(xPos + 3, 17, 75, 12, 53, pixbar, 1, borderColor)
                    addingPrPix(x2Pos + 3, 110, 75, 12, 37, pixbar, 1, borderColorSel)
                    xPos += 85
                    x2Pos += 85
                if percshow:
                    if percmode == '1':
                        i = '53%'
                        ii = '37%'
                        poi = 95
                    else:
                        i = '(53%)'
                        ii = '(37%)'
                        poi = 105
                    addingText2(xPos + 5, 0, poi, 45, rthcrtvc, 1, i, percColor, None)
                    addingText2(x2Pos + 5, 95, poi, 45, rthcrtvc, 1, ii, percColorSel, None)
                    xPos += poi + 10
                    x2Pos += poi + 10
                if crypticonmode == '1':
                    cryptpixmap_size = icocrypt.size()
                    pixx_width = cryptpixmap_size.width()
                    pixx_height = cryptpixmap_size.height()
                    if pixx_height < 45:
                        ppp = (45 - pixx_height) / 2
                        ttt = pixx_height
                    else:
                        ppp = 0
                        ttt = 45
                    addingPix(xPos + 5, ppp, pixx_width, ttt, icocrypt)
                addingText2(xPos, 3, 300, 40, rthlrtvc, 2, name, nameColor, None)
                addingText2(x2Pos, 93, 80, 40, rthlrtvc, 2, name2, nameColorSel, None)
                xPos += 310
                x2Pos += 90
                if iconmode == '2':
                    pixico_size = pixico.size()
                    pic_width = pixico_size.width()
                    pic_height = pixico_size.height()
                    if pic_height < 45:
                        lgh = (45 - pic_height) / 2
                        igj = pic_height
                    else:
                        lgh = 0
                        igj = 45
                    addingPix(xPos + 10, lgh, 45, pic_height, pixico)
                    addingPix(x2Pos + 10, lgh + 90, 45, pic_height, pixico)
                    xPos += 65
                    x2Pos += 65
                if remmode != '3':
                    if remmode == '1':
                        remain = '(+47 ' + _('min') + ')'
                        remai = '(+63 ' + _('min') + ')'
                    if remmode == '2':
                        remain = '(+0' + _('h') + '47' + _('min') + ')'
                        remai = '(+1' + _('h') + '3' + _('min') + ')'
                    addingText2(xPos1, 45, 180, 45, rthcrtvc, 5, remain, remColor, None)
                    addingText2(x2Pos1, 135, 180, 45, rthcrtvc, 5, remai, remColorSel, None)
                    xPos1 += 195
                    xPos2 += 195
                    x2Pos1 += 195
                    x2Pos2 += 195
                if crypticonmode == '2':
                    cryptpixmap_size = icocrypt.size()
                    pixx_width = cryptpixmap_size.width()
                    pixx_height = cryptpixmap_size.height()
                    if pixx_height < 45:
                        iii = (45 - pixx_height) / 2
                        eee = pixx_height
                    else:
                        iii = 0
                        eee = 45
                    addingPix(xPos + 5, iii, pixx_width, eee, icocrypt)
                    xPos += pixx_width + 15
                if endmode:
                    if piconmode:
                        if picomode == '1':
                            ff = 1110 - xPos
                            ffj = 1110 - x2Pos
                        elif bigpicomode == '1':
                            if 1000 - xPos > 0:
                                ff = 1000 - xPos
                                ffj = 1000 - x2Pos
                            else:
                                ff = 0
                        elif bigpicomode == '2':
                            if 950 - xPos > 0:
                                ff = 950 - xPos
                                ffj = 950 - x2Pos
                            else:
                                ff = 0
                    else:
                        ff = 1110 - xPos
                        ffj = 1110 - x2Pos
                    addingText2(xPos, 2, ff, 41, rthlrtvc, 4, '12.30 - 14.10', endColor, None)
                    addingText2(x2Pos, 92, ffj, 41, rthlrtvc, 4, '12.46 - 14.26', endColorSel, None)
                if eventmode == '1':
                    eventname = _('EventName testing')
                elif eventmode == '2':
                    eventname = _('(EventName testing)')
                elif eventmode == '3':
                    eventname = _('-EventName testing')
                if piconmode:
                    if picomode == '1':
                        hh = 1095 - xPos1
                        hhf = 1095 - x2Pos1
                    elif bigpicomode == '1':
                        hh = 995 - xPos1
                        hhf = 995 - x2Pos1
                    elif bigpicomode == '2':
                        hh = 945 - xPos1
                        hhf = 945 - x2Pos1
                else:
                    hh = 1105 - xPos1
                    hhf = 1105 - x2Pos1
                addingText2(xPos1, 45, hh, 45, rthlrtvc, 3, eventname, eventColor, None)
                addingText2(x2Pos1, 135, hhf, 45, rthlrtvc, 3, eventname, eventColorSel, None)
            else:
                if piconmode:
                    cc = 1110 - xPos if picomode == '1' else 1009 - xPos
                else:
                    cc = 1110 - xPos
                bd = 1 if bordermode else 0
                addingPrPix(xPos, 80, cc, 9, 53, pixlong, bd, None)
                addingPrPix(xPos, 170, cc, 9, 37, pixlong, bd, None)
                if remmode != '3':
                    if remmode == '1':
                        remain = '(+47 ' + _('min') + ')'
                        remai = '(+63 ' + _('min') + ')'
                    if remmode == '2':
                        remain = '(+0' + _('h') + '47' + _('min') + ')'
                        remai = '(+1' + _('h') + '3' + _('min') + ')'
                    addingText2(xPos1, 42, 180, 36, rthcrtvc, 5, remain, remColor, None)
                    addingText2(x2Pos1, 132, 180, 36, rthcrtvc, 5, remai, remColorSel, None)
                xPos1 += 185
                xPos2 += 185
                x2Pos1 += 185
                x2Pos2 += 185
                if crypticonmode == '1':
                    cryptpixmap_size = icocrypt.size()
                    pixx_width = cryptpixmap_size.width()
                    pixx_height = cryptpixmap_size.height()
                    if pixx_height < 38:
                        ggg = (38 - pixx_height) / 2
                        hhh = pixx_height
                    else:
                        ggg = 2
                        hhh = 36
                    addingPix(xPos + 10, ggg, pixx_width, hhh, icocrypt)
                    xPos += pixx_width + 15
                addingText2(xPos + 10, 2, 300, 40, rthlrtvc, 2, name, nameColor, None)
                addingText2(x2Pos + 10, 92, 80, 40, rthlrtvc, 2, name2, nameColorSel, None)
                xPos += 310
                x2Pos += 90
                if iconmode == '2':
                    pixico_size = pixico.size()
                    pic_width = pixico_size.width()
                    pic_height = pixico_size.height()
                    if pic_height < 45:
                        lgh = (45 - pic_height) / 2
                        igj = pic_height
                    else:
                        lgh = 0
                        igj = 45
                    addingPix(xPos + 17, lgh - 1, 45, igj - 2, pixico)
                    addingPix(x2Pos + 17, lgh + 90, 45, igj - 2, pixico)
                    xPos += 62
                    x2Pos += 62
                if crypticonmode == '2':
                    cryptpixmap_size = icocrypt.size()
                    pixx_width = cryptpixmap_size.width()
                    pixx_height = cryptpixmap_size.height()
                    if pixx_height < 45:
                        iii = (45 - pixx_height) / 2
                        eee = pixx_height
                    else:
                        iii = 0
                        eee = 45
                    addingPix(xPos + 8, iii - 1, pixx_width, eee - 2, icocrypt)
                    xPos += pixx_width + 15
                if endmode:
                    if piconmode:
                        if picomode == '1':
                            tnt = 1110 - xPos if 1110 - xPos > 0 else 0
                        elif bigpicomode == '1':
                            tnt = 1000 - xPos if 1000 - xPos > 0 else 0
                        elif bigpicomode == '2':
                            tnt = 950 - xPos if 950 - xPos > 0 else 0
                    else:
                        tnt = 1110 - xPos
                    addingText2(xPos + 15, 3, tnt, 35, rthlrtvc, 4, '12.30 - 14.10', endColor, None)
                    addingText2(x2Pos + 18, 93, tnt, 35, rthlrtvc, 4, '12.46 - 14.26', endColorSel, None)
                if eventmode == '1':
                    eventname = _('EventName testing')
                elif eventmode == '2':
                    eventname = _('(EventName testing)')
                elif eventmode == '3':
                    eventname = _('--EventName testing')
                if piconmode:
                    if picomode == '1':
                        bn = 1095 - xPos1
                        bnf = 1095 - x2Pos1
                    else:
                        bn = 1095 - xPos1 if bigpicomode == '1' else 945 - xPos1
                        bnf = 1095 - xPos1 if bigpicomode == '1' else 945 - xPos1
                else:
                    bn = 1095 - xPos1
                    bnf = 1095 - x2Pos1
                addingText2(xPos1 + 15, 42, bn, 36, rthlrtvc, 3, eventname, eventColor, None)
                addingText2(x2Pos1 + 15, 132, bnf, 36, rthlrtvc, 3, eventname, eventColorSel, None)
        else:
            selec = _('This is selected channel')
            sely = 69 if linemode == '1' else 51
            addingPix(1150, sely, 42, 32, picstrel)
            addingText2(1210, sely, 530, 32, rthlrtvc, 0, selec, numColor, numColorSel)
            if piconmode:
                ss = 5
                if linemode == '1':
                    if picomode == '1':
                        oo = xPos
                        ss = 106
                    else:
                        oo = 1005
                    lr = 100
                    li = 60
                    ooo = 60
                    oop = 120
                else:
                    if picomode == '1':
                        oo = xPos
                        ss = 90
                    else:
                        oo = 1025
                    lr = 80
                    li = 48
                    ooo = 48
                    oop = 96
                addingPix(oo, 0, lr, li, picon)
                addingPix(oo, ooo, lr, li, picon2)
                addingPix(oo, oop, lr, li, picon3)
                xPos += ss
                x2Pos += ss
                x3Pos += ss
                if barmode == '1' and progress != 'no':
                    if progress != 'barright':
                        qq = xPos + 5
                        ee = 0 if barpercmode else 80
                    else:
                        ee = 0
                        if linemode == '1':
                            qq = 1030 if picomode == '1' else 925
                        else:
                            qq = 1030 if picomode == '1' else 940
                    if not barpercmode:
                        if linemode == '1':
                            ww = 24
                            ww2 = 84
                            ww3 = 144
                        else:
                            ww = 18
                            ww2 = 66
                            ww3 = 114
                    elif linemode == '1':
                        ww = 44
                        ww2 = 104
                        ww3 = 164
                    else:
                        ww = 32
                        ww2 = 80
                        ww3 = 128
                    addingPr(qq, ww, 75, 12, 53, 1, barColor)
                    addingPr(qq, ww2, 75, 12, 37, 1, barColorSel)
                    addingPr(qq, ww3, 75, 12, 45, 1, barColor)
                    xPos += ee + 5
                    x2Pos += ee + 5
                    x3Pos += ee + 5
                elif barmode == '2' and progress != 'no':
                    if progress != 'barright':
                        qq = xPos + 5
                        ee = 0 if barpercmode else 80
                    else:
                        ee = 0
                        if linemode == '1':
                            qq = 1030 if picomode == '1' else 925
                        else:
                            qq = 1030 if picomode == '1' else 940
                    if not barpercmode:
                        if linemode == '1':
                            ww = 24
                            ww2 = 84
                            ww3 = 144
                        else:
                            ww = 18
                            ww2 = 66
                            ww3 = 114
                    elif linemode == '1':
                        ww = 44
                        ww2 = 104
                        ww3 = 164
                    else:
                        ww = 32
                        ww2 = 80
                        ww3 = 128
                    addingPrPix(qq, ww, 75, 12, 53, pixbar, 1, borderColor)
                    addingPrPix(qq, ww2, 75, 12, 37, pixbar, 1, borderColorSel)
                    addingPrPix(qq, ww3, 75, 12, 45, pixbar, 1, borderColor)
                    xPos += ee + 5
                    x2Pos += ee + 5
                    x3Pos += ee + 5
                if percshow:
                    ii = 0
                    if not barpercmode:
                        tt = 0
                        uu = 1
                        tt2 = 60 if linemode == '1' else 48
                        tt3 = 120 if linemode == '1' else 96
                        if percpos == '1':
                            rr = xPos + 5
                            if linemode == '1':
                                yy = 60
                                ii = 100
                                tr = 95
                            else:
                                yy = 48
                                ii = 90
                                tr = 85
                        elif linemode == '1':
                            yy = 60
                            tr = 95
                            if picomode == '1':
                                if progress != 'barright':
                                    rr = 1025
                                elif progress == 'barright':
                                    rr = 945
                            elif progress != 'barright':
                                rr = 920
                            elif progress == 'barright':
                                rr = 835
                        yy = 48
                        tr = 85
                        if picomode == '1':
                            if progress != 'barright':
                                rr = 1035
                            elif progress == 'barright':
                                rr = 955
                        elif progress != 'barright':
                            rr = 925
                        elif progress == 'barright':
                            rr = 845
                    else:
                        tt = 2
                        tt2 = 62 if linemode == '1' else 50
                        tt3 = 122 if linemode == '1' else 98
                        yy = 42 if linemode == '1' else 30
                        uu = 8
                        if linemode == '1':
                            tr = 75
                            if percpos == '1':
                                rr = xPos - 5
                                ii = 85
                            else:
                                rr = 1030 if picomode == '1' else 925
                        else:
                            tr = 75
                            if percpos == '1':
                                rr = xPos
                                ii = 75
                            else:
                                rr = 1035 if picomode == '1' else 950
                    if percmode == '1':
                        p = '53%'
                        pp = '37%'
                        ppp = '45%'
                    else:
                        p = '(53%)'
                        pp = '(37%)'
                        ppp = '(45%)'
                    addingText2(rr, tt, tr, yy, rthcrtvc, 1, p, percColor, None)
                    addingText2(rr, tt2, tr, yy, rthcrtvc, 1, pp, percColorSel, None)
                    addingText2(rr, tt3, tr, yy, rthcrtvc, 1, ppp, percColor, None)
                    xPos += ii
                    x2Pos += ii
                    x3Pos += ii
                if crypticonmode == '1':
                    cryptpixmap_size = icocrypt.size()
                    pixx_width = cryptpixmap_size.width()
                    pixx_height = cryptpixmap_size.height()
                    if linemode == '1':
                        www = (60 - pixx_height) / 2
                        www3 = www + 120
                    else:
                        www = (48 - pixx_height) / 2
                        www3 = www + 96
                    addingPix(xPos, www, pixx_width, pixx_height, icocrypt)
                    addingPix(x3Pos, www3, pixx_width, pixx_height, icocrypt)
                    xPos += pixx_width + 5
                    x2Pos += pixx_width + 5
                    x3Pos += pixx_width + 5
            else:
                ee = 0
                if barmode == '1' and progress != 'no':
                    if progress != 'barright':
                        qq = xPos
                        if not barpercmode:
                            ee = 85
                    else:
                        qq = 1025
                    if not barpercmode:
                        if linemode == '1':
                            ww = 24
                            ww2 = 84
                            ww3 = 144
                        else:
                            ww = 18
                            ww2 = 66
                            ww3 = 114
                    elif linemode == '1':
                        ww = 44
                        ww2 = 104
                        ww3 = 164
                    else:
                        ww = 32
                        ww2 = 80
                        ww3 = 128
                    addingPr(qq, ww, 75, 12, 53, 1, barColor)
                    addingPr(qq, ww2, 75, 12, 37, 1, barColorSel)
                    addingPr(qq, ww3, 75, 12, 45, 1, barColor)
                    xPos += ee + 5
                    x2Pos += ee + 5
                    x3Pos += ee + 5
                elif barmode == '2' and progress != 'no':
                    if progress != 'barright':
                        qq = xPos
                        if not barpercmode:
                            ee = 85
                    else:
                        qq = 1025
                    if not barpercmode:
                        if linemode == '1':
                            ww = 23
                            ww2 = 83
                            ww3 = 143
                        else:
                            ww = 17
                            ww2 = 65
                            ww3 = 113
                    elif linemode == '1':
                        ww = 44
                        ww2 = 104
                        ww3 = 164
                    else:
                        ww = 32
                        ww2 = 80
                        ww3 = 128
                    addingPrPix(qq, ww, 75, 12, 53, pixbar, 1, borderColor)
                    addingPrPix(qq, ww2, 75, 12, 37, pixbar, 1, borderColorSel)
                    addingPrPix(qq, ww3, 75, 12, 45, pixbar, 1, borderColor)
                    xPos += ee + 5
                    x2Pos += ee + 5
                    x3Pos += ee + 5
                if percshow:
                    ii = 0
                    if not barpercmode:
                        tr = 85
                        tt = 0
                        if linemode == '1':
                            tt2 = 60
                            tt3 = 120
                            yy = 60
                        else:
                            tt2 = 48
                            tt3 = 96
                            yy = 48
                        uu = 1
                        if percpos == '1':
                            ii = 85
                            rr = xPos
                        elif progress != 'barright':
                            rr = 1025
                        elif progress == 'barright':
                            rr = 940
                    else:
                        tr = 75
                        tt = 2
                        if linemode == '1':
                            tt2 = 62
                            tt3 = 122
                            yy = 42
                        else:
                            tt2 = 50
                            tt3 = 98
                            yy = 30
                        uu = 8
                        if percpos == '1':
                            rr = xPos
                            ii = 80
                        else:
                            rr = 1030
                    if percmode == '1':
                        p = '53%'
                        pp = '37%'
                        ppp = '45%'
                    else:
                        p = '(53%)'
                        pp = '(37%)'
                        ppp = '(45%)'
                    addingText2(rr, tt, tr, yy, rthcrtvc, 1, p, percColor, None)
                    addingText2(rr, tt2, tr, yy, rthcrtvc, 1, pp, percColorSel, None)
                    addingText2(rr, tt3, tr, yy, rthcrtvc, 1, ppp, percColor, None)
                    xPos += ii
                    x2Pos += ii
                    x3Pos += ii
                if crypticonmode == '1':
                    cryptpixmap_size = icocrypt.size()
                    pixx_width = cryptpixmap_size.width()
                    pixx_height = cryptpixmap_size.height()
                    if linemode == '1':
                        www = (60 - pixx_height) / 2
                        www3 = www + 120
                    else:
                        www = (48 - pixx_height) / 2
                        www3 = www + 96
                    addingPix(xPos, www, pixx_width, pixx_height, icocrypt)
                    addingPix(x3Pos, www3, pixx_width, pixx_height, icocrypt)
                    xPos += pixx_width + 5
                    x2Pos += pixx_width + 5
                    x3Pos += pixx_width + 5
            if linemode == '1':
                jl = xPos + 5
                jl2 = xPos + 5
                jl3 = xPos + 5
                dfg = 0
                dfg2 = 60
                dfg3 = 120
                ysizen = 60
            else:
                jl = xPos + 16
                jl2 = xPos + 16
                jl3 = xPos + 16
                dfg = 0
                dfg2 = 48
                dfg3 = 96
                ysizen = 48
            addingText2(jl, dfg, 300, ysizen, rthlrtvc, 2, name, nameColor, None)
            addingText2(jl2, dfg2, 80, ysizen, rthlrtvc, 2, name2, nameColorSel, None)
            addingText2(jl3, dfg3, 170, ysizen, rthlrtvc, 2, name3, nameColor, None)
            xPos += 310
            x2Pos += 90
            x3Pos += 180
            if iconmode == '2':
                pixico_size = pixico.size()
                pix_width = pixico_size.width()
                pic_height = pixico_size.height()
                if linemode == '1':
                    if pic_height < 60:
                        lgh = (60 - pic_height) / 2
                        lgh2 = lgh + 60
                        lgh3 = lgh + 120
                        igj = pic_height
                    else:
                        lgh = 0
                        igj = 45
                elif pic_height < 48:
                    lgh = (48 - pic_height) / 2
                    lgh2 = lgh + 48
                    lgh3 = lgh + 96
                    igj = pic_height
                else:
                    lgh = 0
                    igj = 45
                addingPix(xPos + 10, lgh, 45, igj - 2, pixico)
                addingPix(x2Pos + 10, lgh2, 45, igj - 2, pixico)
                addingPix(x3Pos + 10, lgh3, 45, igj - 2, pixico)
                xPos += 50
                x2Pos += 50
                x3Pos += 50
            if crypticonmode == '2':
                cryptpixmap_size = icocrypt.size()
                pixx_width = cryptpixmap_size.width()
                pixx_height = cryptpixmap_size.height()
                if linemode == '1':
                    www = (60 - pixx_height) / 2
                    www3 = www + 120
                else:
                    www = (48 - pixx_height) / 2
                    www3 = www + 96
                addingPix(xPos, www, pixx_width, pixx_height, icocrypt)
                addingPix(x3Pos, www3, pixx_width, pixx_height, icocrypt)
                xPos += pixx_width
                x3Pos += pixx_width
            if linemode == '1':
                le = xPos + 10
                le2 = x2Pos + 10
                le3 = x3Pos + 10
                ypo = 0
                ypo2 = 60
                ypo3 = 120
                hei = 60
            else:
                le = xPos + 20
                le2 = x2Pos + 20
                le3 = x3Pos + 20
                ypo = 0
                ypo2 = 48
                ypo3 = 96
                hei = 48
            if progress == 'barright':
                if percshow:
                    if not barpercmode:
                        if percpos == '1':
                            if piconmode:
                                if picomode == '1':
                                    kk = 1025 - xPos
                                    kk2 = 1025 - x2Pos
                                    kk3 = 1025 - x3Pos
                                else:
                                    kk = 930 - xPos
                                    kk2 = 930 - x2Pos
                                    kk3 = 930 - x3Pos
                            else:
                                kk = 1025 - xPos
                                kk2 = 1025 - x2Pos
                                kk3 = 1025 - x3Pos
                        elif piconmode:
                            if picomode == '1':
                                kk = 940 - xPos
                                kk2 = 940 - x2Pos
                                kk3 = 940 - x3Pos
                            else:
                                kk = 835 - xPos
                                kk2 = 835 - x2Pos
                                kk3 = 835 - x3Pos
                        else:
                            kk = 940 - xPos
                            kk2 = 940 - x2Pos
                            kk3 = 940 - x3Pos
                    elif piconmode:
                        if picomode == '1':
                            kk = 1025 - xPos
                            kk2 = 1025 - x2Pos
                            kk3 = 1025 - x3Pos
                        else:
                            kk = 915 - xPos
                            kk2 = 915 - x2Pos
                            kk3 = 915 - x3Pos
                    else:
                        kk = 1025 - xPos
                        kk2 = 1025 - x2Pos
                        kk3 = 1025 - x3Pos
                elif piconmode:
                    if picomode == '1':
                        kk = 1025 - xPos
                        kk2 = 1025 - x2Pos
                        kk3 = 1025 - x3Pos
                    else:
                        kk = 945 - xPos
                        kk2 = 945 - x2Pos
                        kk3 = 945 - x3Pos
                else:
                    kk = 1025 - xPos
                    kk2 = 1025 - x2Pos
                    kk3 = 1025 - x3Pos
            if progress != 'barright':
                if percshow:
                    if not barpercmode:
                        if percpos == '1':
                            if piconmode:
                                if picomode == '1':
                                    kk = 1110 - xPos
                                    kk2 = 1110 - x2Pos
                                    kk3 = 1110 - x3Pos
                                else:
                                    kk = 1000 - xPos
                                    kk2 = 1000 - x2Pos
                                    kk3 = 1000 - x3Pos
                            else:
                                kk = 1110 - xPos
                                kk2 = 1110 - x2Pos
                                kk3 = 1110 - x3Pos
                        elif piconmode:
                            if picomode == '1':
                                kk = 1025 - xPos
                                kk2 = 1025 - x2Pos
                                kk3 = 1025 - x3Pos
                            else:
                                kk = 910 - xPos
                                kk2 = 910 - x2Pos
                                kk3 = 910 - x3Pos
                        else:
                            kk = 1025 - xPos
                            kk2 = 1025 - x2Pos
                            kk3 = 1025 - x3Pos
                    elif piconmode:
                        if picomode == '1':
                            kk = 1110 - xPos
                            kk2 = 1110 - x2Pos
                            kk3 = 1110 - x3Pos
                        elif linemode == '1':
                            kk = 1000 - xPos
                            kk2 = 1000 - x2Pos
                            kk3 = 1000 - x3Pos
                        else:
                            kk = 1025 - xPos
                            kk2 = 1025 - x2Pos
                            kk3 = 1025 - x3Pos
                    else:
                        kk = 1110 - xPos
                        kk2 = 1110 - x2Pos
                        kk3 = 1110 - x3Pos
                elif piconmode:
                    if picomode == '1':
                        kk = 1025 - xPos
                        kk2 = 1025 - x2Pos
                        kk3 = 1025 - x3Pos
                    else:
                        kk = 940 - xPos
                        kk2 = 940 - x2Pos
                        kk3 = 940 - x3Pos
                else:
                    kk = 1025 - xPos
                    kk2 = 1025 - x2Pos
                    kk3 = 1025 - x3Pos
            if eventmode == '1':
                eventname = _('EventName testing')
            elif eventmode == '2':
                eventname = _('(EventName testing)')
            elif eventmode == '3':
                eventname = _('--EventName testing')
            addingText2(le, ypo, kk, hei, rthlrtvc, 3, eventname, eventColor, None)
            addingText2(le2, ypo2, kk2, hei, rthlrtvc, 3, eventname, eventColorSel, None)
            addingText2(le3, ypo3, kk3, hei, rthlrtvc, 3, eventname, eventColor, None)
    elif listmode:
        selec = _('This is selected channel')
        ypossel = 74 if doubmode else 56
        addingPix(770, ypossel, 42, 32, picstrel)
        addingText2(830, ypossel, 400, 32, rthlrtvc, 0, selec, numColor, numColorSel)
        if piconmode:
            if picomode == '1':
                a = xPos
                e = 105 if doubmode else 80
            else:
                a = 639 if doubmode else 664
                e = 0
            if not doubmode:
                wt = 75
                ht = 45
                ot = 1
                ot2 = 46
            else:
                wt = 100
                ht = 60
                ot = 0
                ot2 = 60
            addingPix(a, ot, wt, ht, picon)
            addingPix(a, ot2, wt, ht, picon2)
            xPos += e
            xPos1 += e
            xPos2 += e
            x2Pos += e
            x2Pos1 += e
            x2Pos2 += e
        if not doubmode:
            if barmode == '1':
                addingPr(xPos, 8, 52, 8, 53, 1, barColor)
                addingPr(x2Pos, 56, 52, 8, 37, 1, barColorSel)
                xPos += 57
                x2Pos += 57
            else:
                addingPrPix(xPos, 8, 52, 8, 53, pixbar, 1, borderColor)
                addingPrPix(x2Pos, 56, 52, 8, 37, pixbar, 1, borderColorSel)
                xPos += 57
                x2Pos += 57
            if percshow:
                if percmode == '1':
                    i = '53%'
                    ii = '37%'
                    poi = 70
                else:
                    i = '(53%)'
                    ii = '(37%)'
                    poi = 80
                addingText2(xPos, 0, poi, 24, rthcrtvc, 1, i, percColor, None)
                addingText2(x2Pos, 48, poi, 24, rthcrtvc, 1, ii, percColorSel, None)
                xPos += poi
                x2Pos += poi
            if crypticonmode == '1':
                cryptpixmap_size = icocrypt.size()
                pixx_width = cryptpixmap_size.width()
                pixx_height = cryptpixmap_size.height()
                if pixx_height < 24:
                    ppp = (24 - pixx_height) / 2
                    ttt = pixx_height
                else:
                    ppp = 0
                    ttt = 24
                addingPix(xPos, ppp, pixx_width, ttt, icocrypt)
                xPos += pixx_width + 5
            addingText2(xPos, 0, 200, 24, rthlrtvc, 2, name, nameColor, None)
            addingText2(x2Pos, 48, 80, 24, rthlrtvc, 2, name2, nameColorSel, None)
            xPos += 210
            x2Pos += 90
            if iconmode == '2':
                pixico_size = pixico.size()
                pic_width = pixico_size.width()
                pic_height = pixico_size.height()
                if pic_height < 24:
                    lgh = 24 / 2
                    igj = pic_height
                else:
                    lgh = 0
                    igj = 24
                addingPix(xPos, lgh, 30, pic_height, pixico)
                addingPix(x2Pos, lgh + 48, 30, pic_height, pixico)
                xPos += 30
                x2Pos += 30
            if remmode != '3':
                if remmode == '1':
                    remain = '(+47 ' + _('min') + ')'
                    remai = '(+63 ' + _('min') + ')'
                if remmode == '2':
                    remain = '(+0' + _('h') + '47' + _('min') + ')'
                    remai = '(+1' + _('h') + '3' + _('min') + ')'
                addingText2(xPos1, 24, 135, 24, rthcrtvc, 5, remain, remColor, None)
                addingText2(x2Pos1, 72, 135, 24, rthcrtvc, 5, remai, remColorSel, None)
                xPos1 += 140
                xPos2 += 140
                x2Pos1 += 140
                x2Pos2 += 140
            if crypticonmode == '2':
                cryptpixmap_size = icocrypt.size()
                pixx_width = cryptpixmap_size.width()
                pixx_height = cryptpixmap_size.height()
                if pixx_height < 24:
                    iii = (24 - pixx_height) / 2
                    eee = pixx_height
                else:
                    iii = 0
                    eee = 24
                addingPix(xPos, iii, pixx_width, eee, icocrypt)
                xPos += pixx_width + 5
            if endmode:
                if piconmode:
                    if picomode == '1':
                        ff = 740 - xPos
                        ffj = 740 - x2Pos
                    else:
                        ff = 655 - xPos
                        ffj = 655 - x2Pos
                else:
                    ff = 740 - xPos
                    ffj = 740 - x2Pos
                addingText2(xPos, 1, ff, 23, rthlrtvc, 4, '12.30 - 14.10', endColor, None)
                addingText2(x2Pos, 49, ffj, 23, rthlrtvc, 4, '12.46 - 14.26', endColorSel, None)
            if eventmode == '1':
                eventname = _('EventName testing')
            elif eventmode == '2':
                eventname = _('(EventName testing)')
            elif eventmode == '3':
                eventname = _('-EventName testing')
            if piconmode:
                if picomode == '1':
                    hh = 735 - xPos1
                    hhf = 735 - x2Pos1
                else:
                    hh = 655 - xPos1
                    hhf = 655 - x2Pos1
            else:
                hh = 735 - xPos1
                hhf = 735 - x2Pos1
            addingText2(xPos1, 24, hh, 24, rthlrtvc, 3, eventname, eventColor, None)
            addingText2(x2Pos1, 72, hhf, 24, rthlrtvc, 3, eventname, eventColorSel, None)
        else:
            if piconmode:
                cc = 740 - xPos if picomode == '1' else 639 - xPos
            else:
                cc = 740 - xPos
            bd = 1 if bordermode else 0
            addingPrPix(xPos, 53, cc, 6, 53, pixlong, bd, None)
            addingPrPix(xPos, 113, cc, 6, 37, pixlong, bd, None)
            if remmode != '3':
                if remmode == '1':
                    remain = '(+47 ' + _('min') + ')'
                    remai = '(+63 ' + _('min') + ')'
                if remmode == '2':
                    remain = '(+0' + _('h') + '47' + _('min') + ')'
                    remai = '(+1' + _('h') + '3' + _('min') + ')'
                addingText2(xPos1, 27, 135, 27, rthcrtvc, 5, remain, remColor, None)
                addingText2(x2Pos1, 87, 135, 27, rthcrtvc, 5, remain, remColorSel, None)
            xPos1 += 140
            xPos2 += 140
            x2Pos1 += 140
            x2Pos2 += 140
            if crypticonmode == '1':
                cryptpixmap_size = icocrypt.size()
                pixx_width = cryptpixmap_size.width()
                pixx_height = cryptpixmap_size.height()
                if pixx_height < 27:
                    ggg = (27 - pixx_height) / 2
                    hhh = pixx_height
                else:
                    ggg = 0
                    hhh = 27
                addingPix(xPos, ggg, pixx_width, hhh, icocrypt)
                xPos += pixx_width + 5
            addingText2(xPos, 0, 200, 27, rthlrtvc, 2, name, nameColor, None)
            addingText2(x2Pos, 60, 55, 27, rthlrtvc, 2, name2, nameColorSel, None)
            xPos += 210
            x2Pos += 65
            if iconmode == '2':
                pixico_size = pixico.size()
                pic_width = pixico_size.width()
                pic_height = pixico_size.height()
                if pic_height < 30:
                    lgh = (30 - pic_height) / 2
                    igj = pic_height
                else:
                    lgh = 0
                    igj = 30
                addingPix(xPos, lgh, 30, igj, pixico)
                addingPix(x2Pos, lgh + 60, 30, igj, pixico)
                xPos += 32
                x2Pos += 32
            if crypticonmode == '2':
                cryptpixmap_size = icocrypt.size()
                pixx_width = cryptpixmap_size.width()
                pixx_height = cryptpixmap_size.height()
                if pixx_height < 30:
                    iii = (30 - pixx_height) / 2
                    eee = pixx_height
                else:
                    iii = 0
                    eee = 30
                addingPix(xPos, iii, pixx_width, eee, icocrypt)
                xPos += pixx_width + 5
            if endmode:
                if piconmode:
                    if picomode == '1':
                        tnt = 740 - xPos if 740 - xPos > 0 else 0
                    else:
                        tnt = 635 - xPos if 635 - xPos > 0 else 0
                else:
                    tnt = 740 - xPos
                addingText2(xPos, 2, tnt, 27, rthlrtvc, 4, '12.30 - 14.10', endColor, None)
                addingText2(x2Pos, 62, tnt, 27, rthlrtvc, 4, '12.46 - 14.26', endColorSel, None)
            if eventmode == '1':
                eventname = _('EventName testing')
            elif eventmode == '2':
                eventname = _('(EventName testing)')
            elif eventmode == '3':
                eventname = _('--EventName testing')
            if piconmode:
                if picomode == '1':
                    bn = 735 - xPos1
                    bnf = 735 - x2Pos1
                else:
                    bn = 635 - xPos1
                    bnf = 635 - x2Pos1
            else:
                bn = 735 - xPos1
                bnf = 735 - x2Pos1
            addingText2(xPos1, 27, bn, 27, rthlrtvc, 3, eventname, eventColor, None)
            addingText2(x2Pos1, 87, bnf, 27, rthlrtvc, 3, eventname, eventColorSel, None)
    else:
        selec = _('This is selected channel')
        addingPix(770, 32, 42, 32, picstrel)
        addingText2(830, 32, 300, 32, rthlrtvc, 0, selec, numColor, numColorSel)
        if piconmode:
            ss = 55 if picomode == '1' else 0
            oo = xPos if picomode == '1' else 689
            ooo = 32
            oop = 64
            addingPix(oo, 0, 50, 30, picon)
            addingPix(oo, ooo, 50, 30, picon2)
            addingPix(oo, oop, 50, 30, picon3)
            xPos += ss
            x2Pos += ss
            x3Pos += ss
            if barmode == '1' and progress != 'no':
                if progress != 'barright':
                    qq = xPos
                    ee = 0 if barpercmode else 57
                else:
                    ee = 0
                    qq = 685 if picomode == '1' else 630
                if not barpercmode:
                    ww = 12
                    ww2 = 44
                    ww3 = 76
                else:
                    ww = 23
                    ww2 = 55
                    ww3 = 87
                addingPr(qq, ww, 52, 8, 53, 1, barColor)
                addingPr(qq, ww2, 52, 8, 37, 1, barColorSel)
                addingPr(qq, ww3, 52, 8, 45, 1, barColor)
                xPos += ee
                x2Pos += ee
                x3Pos += ee
            elif barmode == '2' and progress != 'no':
                if progress != 'barright':
                    qq = xPos
                    ee = 0 if barpercmode else 57
                else:
                    ee = 0
                    qq = 685 if picomode == '1' else 630
                if not barpercmode:
                    ww = 12
                    ww2 = 44
                    ww3 = 76
                else:
                    ww = 23
                    ww2 = 55
                    ww3 = 87
                addingPrPix(qq, ww, 52, 8, 53, pixbar, 1, borderColor)
                addingPrPix(qq, ww2, 52, 8, 37, pixbar, 1, borderColorSel)
                addingPrPix(qq, ww3, 52, 8, 45, pixbar, 1, borderColor)
                xPos += ee
                x2Pos += ee
                x3Pos += ee
            if percshow:
                ii = 0
                if not barpercmode:
                    yy = 32
                    uu = 1
                    if percpos == '1':
                        ii = 60
                        rr = xPos
                    elif picomode == '1':
                        if progress != 'barright':
                            rr = 680
                        elif progress == 'barright':
                            rr = 625
                    elif progress != 'barright':
                        rr = 625
                    elif progress == 'barright':
                        rr = 570
                else:
                    yy = 20
                    uu = 8
                    if percpos == '1':
                        rr = xPos
                        ii = 60
                    else:
                        rr = 680 if picomode == '1' else 625
                if percmode == '1':
                    p = '53%'
                    pp = '37%'
                    ppp = '45%'
                else:
                    p = '(53%)'
                    pp = '(37%)'
                    ppp = '(45%)'
                addingText2(rr, 0, 55, yy, rthcrtvc, 1, p, percColor, None)
                addingText2(rr, 32, 55, yy, rthcrtvc, 1, pp, percColorSel, None)
                addingText2(rr, 64, 55, yy, rthcrtvc, 1, ppp, percColor, None)
                xPos += ii
                x2Pos += ii
                x3Pos += ii
            if crypticonmode == '1':
                cryptpixmap_size = icocrypt.size()
                pixx_width = cryptpixmap_size.width()
                pixx_height = cryptpixmap_size.height()
                if pixx_height < 32:
                    www = (32 - pixx_height) / 2
                    www3 = www + 64
                else:
                    www = 0
                    www3 = 64
                addingPix(xPos, www, pixx_width, pixx_height, icocrypt)
                addingPix(x3Pos, www3, pixx_width, pixx_height, icocrypt)
                xPos += pixx_width + 5
                x2Pos += pixx_width + 5
                x3Pos += pixx_width + 5
        else:
            ee = 0
            if barmode == '1' and progress != 'no':
                if progress != 'barright':
                    qq = xPos
                    if not barpercmode:
                        ee = 57
                else:
                    qq = 685
                if not barpercmode:
                    ww = 12
                    ww2 = 44
                    ww3 = 76
                else:
                    ww = 23
                    ww2 = 55
                    ww3 = 87
                addingPr(qq, ww, 52, 8, 53, 1, barColor)
                addingPr(qq, ww2, 52, 8, 37, 1, barColorSel)
                addingPr(qq, ww3, 52, 8, 45, 1, barColor)
                xPos += ee + 5
                x2Pos += ee + 5
                x3Pos += ee + 5
            elif barmode == '2' and progress != 'no':
                if progress != 'barright':
                    qq = xPos
                    if not barpercmode:
                        ee = 57
                else:
                    qq = 685
                if not barpercmode:
                    ww = 12
                    ww2 = 44
                    ww3 = 76
                else:
                    ww = 23
                    ww2 = 55
                    ww3 = 87
                addingPrPix(qq, ww, 52, 8, 53, pixbar, 1, borderColor)
                addingPrPix(qq, ww2, 52, 8, 37, pixbar, 1, borderColorSel)
                addingPrPix(qq, ww3, 52, 8, 45, pixbar, 1, borderColor)
                xPos += ee
                x2Pos += ee
                x3Pos += ee
            if percshow:
                ii = 60 if percpos == '1' else 0
                if not barpercmode:
                    tt = 0
                    tt2 = 32
                    tt3 = 64
                    yy = 32
                    uu = 1
                    if percpos == '1':
                        rr = xPos
                    elif progress != 'barright':
                        rr = 680
                    elif progress == 'barright':
                        rr = 625
                else:
                    tt = 2
                    tt2 = 34
                    tt3 = 66
                    yy = 20
                    uu = 8
                    rr = xPos if percpos == '1' else 680
                if percmode == '1':
                    p = '53%'
                    pp = '37%'
                    ppp = '45%'
                else:
                    p = '(53%)'
                    pp = '(37%)'
                    ppp = '(45%)'
                addingText2(rr, tt, 55, yy, rthcrtvc, 1, p, percColor, None)
                addingText2(rr, tt2, 55, yy, rthcrtvc, 1, pp, percColorSel, None)
                addingText2(rr, tt3, 55, yy, rthcrtvc, 1, ppp, percColor, None)
                xPos += ii
                x2Pos += ii
                x3Pos += ii
            if crypticonmode == '1':
                cryptpixmap_size = icocrypt.size()
                pixx_width = cryptpixmap_size.width()
                pixx_height = cryptpixmap_size.height()
                if pixx_height < 32:
                    www = (32 - pixx_height) / 2
                    www3 = www + 64
                else:
                    www = 0
                    www3 = 64
                addingPix(xPos, www, pixx_width, pixx_height, icocrypt)
                addingPix(x3Pos, www3, pixx_width, pixx_height, icocrypt)
                xPos += pixx_width + 5
                x2Pos += pixx_width + 5
                x3Pos += pixx_width + 5
        addingText2(xPos + 4, 0, 200, 32, rthlrtvc, 2, name, nameColor, None)
        addingText2(xPos + 4, 32, 55, 32, rthlrtvc, 2, name2, nameColorSel, None)
        addingText2(xPos + 4, 64, 114, 32, rthlrtvc, 2, name3, nameColor, None)
        xPos += 210
        x2Pos += 65
        x3Pos += 124
        if iconmode == '2':
            pixico_size = pixico.size()
            pix_width = pixico_size.width()
            pic_height = pixico_size.height()
            if pic_height < 32:
                lgh = (32 - pic_height) / 2
                lgh2 = lgh + 32
                lgh3 = lgh + 64
                igj = pic_height
            else:
                lgh = 0
                lgh2 = 32
                lgh3 = 64
                igj = 32
            addingPix(xPos, lgh, 30, igj, pixico)
            addingPix(x2Pos, lgh2, 30, igj, pixico)
            addingPix(x3Pos, lgh3, 30, igj, pixico)
            xPos += 35
            x2Pos += 35
            x3Pos += 35
        if crypticonmode == '2':
            cryptpixmap_size = icocrypt.size()
            pixx_width = cryptpixmap_size.width()
            pixx_height = cryptpixmap_size.height()
            if pixx_height < 32:
                www = (32 - pixx_height) / 2
                www3 = www + 64
            else:
                www = 0
                www3 = 64
            addingPix(xPos, www, pixx_width, pixx_height, icocrypt)
            addingPix(x3Pos, www3, pixx_width, pixx_height, icocrypt)
            xPos += pixx_width
            x3Pos += pixx_width
        if eventmode == '1':
            eventname = _('EventName testing')
        elif eventmode == '2':
            eventname = _('(EventName testing)')
        elif eventmode == '3':
            eventname = _('--EventName testing')
        if progress == 'barright':
            if percshow:
                if not barpercmode:
                    if percpos == '1':
                        if piconmode:
                            if picomode == '1':
                                kk = 680 - xPos
                                kk2 = 680 - x2Pos
                                kk3 = 680 - x3Pos
                            else:
                                kk = 620 - xPos
                                kk2 = 620 - x2Pos
                                kk3 = 620 - x3Pos
                        else:
                            kk = 680 - xPos
                            kk2 = 680 - x2Pos
                            kk3 = 680 - x3Pos
                    elif piconmode:
                        if picomode == '1':
                            kk = 620 - xPos
                            kk2 = 620 - x2Pos
                            kk3 = 620 - x3Pos
                        else:
                            kk = 565 - xPos
                            kk2 = 565 - x2Pos
                            kk3 = 565 - x3Pos
                    else:
                        kk = 620 - xPos
                        kk2 = 620 - x2Pos
                        kk3 = 620 - x3Pos
                elif piconmode:
                    if picomode == '1':
                        kk = 680 - xPos
                        kk2 = 680 - x2Pos
                        kk3 = 680 - x3Pos
                    else:
                        kk = 620 - xPos
                        kk2 = 620 - x2Pos
                        kk3 = 620 - x3Pos
                else:
                    kk = 680 - xPos
                    kk2 = 680 - x2Pos
                    kk3 = 680 - x3Pos
            elif piconmode:
                if picomode == '1':
                    kk = 680 - xPos
                    kk2 = 680 - x2Pos
                    kk3 = 680 - x3Pos
                else:
                    kk = 620 - xPos
                    kk2 = 620 - x2Pos
                    kk3 = 620 - x3Pos
            else:
                kk = 680 - xPos
                kk2 = 680 - x2Pos
                kk3 = 680 - x3Pos
        if progress != 'barright':
            if percshow:
                if not barpercmode:
                    if percpos == '1':
                        if piconmode:
                            if picomode == '1':
                                kk = 740 - xPos
                                kk2 = 740 - x2Pos
                                kk3 = 740 - x3Pos
                            else:
                                kk = 680 - xPos
                                kk2 = 680 - x2Pos
                                kk3 = 680 - x3Pos
                        else:
                            kk = 740 - xPos
                            kk2 = 740 - x2Pos
                            kk3 = 740 - x3Pos
                    elif piconmode:
                        if picomode == '1':
                            kk = 680 - xPos
                            kk2 = 680 - x2Pos
                            kk3 = 680 - x3Pos
                        else:
                            kk = 625 - xPos
                            kk2 = 625 - x2Pos
                            kk3 = 625 - x3Pos
                    else:
                        kk = 680 - xPos
                        kk2 = 680 - x2Pos
                        kk3 = 680 - x3Pos
                elif piconmode:
                    if picomode == '1':
                        kk = 740 - xPos
                        kk2 = 740 - x2Pos
                        kk3 = 740 - x3Pos
                    else:
                        kk = 680 - xPos
                        kk2 = 680 - x2Pos
                        kk3 = 680 - x3Pos
                else:
                    kk = 740 - xPos
                    kk2 = 740 - x2Pos
                    kk3 = 740 - x3Pos
            elif piconmode:
                if picomode == '1':
                    kk = 740 - xPos
                    kk2 = 740 - x2Pos
                    kk3 = 740 - x3Pos
                else:
                    kk = 680 - xPos
                    kk2 = 680 - x2Pos
                    kk3 = 680 - x3Pos
            else:
                kk = 740 - xPos
                kk2 = 740 - x2Pos
                kk3 = 740 - x3Pos
        addingText2(xPos, 0, kk, 32, rthlrtvc, 3, eventname, eventColor, None)
        addingText2(x2Pos, 32, kk2, 32, rthlrtvc, 3, eventname, eventColorSel, None)
        addingText2(x3Pos, 64, kk3, 32, rthlrtvc, 3, eventname, eventColor, None)
    return res


return

# okay decompiling ./TestScreen.pyo
