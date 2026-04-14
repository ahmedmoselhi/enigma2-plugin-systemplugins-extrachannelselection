# uncompyle6 version 3.9.3
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.13.9 (main, Oct 30 2025, 02:11:50) [GCC 13.3.0]
# Embedded file name: /usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/plugin.py
# Compiled at: 2019-08-31 08:36:44
from Components.config import *
from .TestScreen import *
from Components.ActionMap import ActionMap
from Plugins.Plugin import PluginDescriptor
from Components.Pixmap import Pixmap
from Components.Sources.List import List
from Components.MenuList import MenuList
from enigma import eSize, getDesktop, eListboxPythonMultiContent, RT_HALIGN_RIGHT, RT_VALIGN_CENTER, gFont, RT_HALIGN_LEFT, ePicLoad
from Screens.Screen import Screen
from Screens.Standby import TryQuitMainloop
from Screens.MessageBox import MessageBox
from Components.MultiContent import MultiContentEntryText, MultiContentEntryPixmapAlphaTest
from Components.Language import language
from Components.ConfigList import ConfigListScreen
from Components.Sources.StaticText import StaticText
from Components.Label import Label
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, SCOPE_LANGUAGE, fileExists, SCOPE_CURRENT_SKIN, SCOPE_SKIN_IMAGE
from Tools.LoadPixmap import LoadPixmap
from xml.dom.minidom import parse, Element
from os import environ, system
import os, gettext
lang = language.getLanguage()
environ['LANGUAGE'] = lang[:2]
gettext.bindtextdomain('enigma2', resolveFilename(SCOPE_LANGUAGE))
gettext.textdomain('enigma2')
gettext.bindtextdomain('ExtraChannelSelection', '%s%s' % (resolveFilename(SCOPE_PLUGINS), 'SystemPlugins/ExtraChannelSelection/locale/'))

def _(txt):
    t = gettext.dgettext('ExtraChannelSelection', txt)
    if t == txt:
        t = gettext.gettext(txt)
    return t


MAPPATH = '/usr/share/enigma2/'
RPATH = '/tmp/'
BACKUPPATH = '/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/backup/'
MAP_FILE = '/usr/share/enigma2/keymap.xml'
pluginversion = '6.1a'
config.plugins.ExtraChannelSelection = ConfigSubsection()
config.plugins.ExtraChannelSelection.enabled = ConfigYesNo(default=True)
config.plugins.ExtraChannelSelection.endmode = ConfigYesNo(default=True)
config.plugins.ExtraChannelSelection.text = ConfigYesNo(default=False)
config.plugins.ExtraChannelSelection.nummode = ConfigYesNo(default=True)
config.plugins.ExtraChannelSelection.bordermode = ConfigYesNo(default=False)
config.plugins.ExtraChannelSelection.barpercmode = ConfigYesNo(default=False)
config.plugins.ExtraChannelSelection.iconmode = ConfigSelection(default='0', choices=[('0', _('None')), ('1', _('Left from servicename')), ('2', _('Right from servicename'))])
config.plugins.ExtraChannelSelection.timericonmode = ConfigSelection(default='1', choices=[('0', _('None')), ('1', _('Left from servicename')), ('2', _('Right from servicename'))])
config.plugins.ExtraChannelSelection.crypticonmode = ConfigSelection(default='0', choices=[('0', _('None')), ('1', _('Left from servicename')), ('2', _('Right from servicename'))])
config.plugins.ExtraChannelSelection.doubmode = ConfigYesNo(default=False)
config.plugins.ExtraChannelSelection.progress = ConfigSelection(default='barleft', choices=[('barleft', _('on left')), ('barright', _('on right')), ('no', _('No'))])
config.plugins.ExtraChannelSelection.percpos = ConfigSelection(default='1', choices=[('1', _('on left')), ('2', _('on right'))])
config.plugins.ExtraChannelSelection.remmode = ConfigSelection(default='1', choices=[('1', _('only minutes')), ('2', _('hours and minutes')), ('3', _('Without remain'))])
colordic = [('1', _('LightBlue2')),
 (
  '2', _('Blue')),
 (
  '3', _('Gray')),
 (
  '4', _('Blue2')),
 (
  '5', _('Blue3')),
 (
  '6', _('Cyan')),
 (
  '7', _('Midnight blue')),
 (
  '8', _('Steel Blue')),
 (
  '9', _('Green')),
 (
  '10', _('Silver')),
 (
  '11', _('Aquamarine')),
 (
  '12', _('Yellow')),
 (
  '13', _('Red')),
 (
  '14', _('Purple')),
 (
  '15', _('White')),
 (
  '16', _('Blue')),
 (
  '17', _('Saddle Brown')),
 (
  '18', _('Crimson')),
 (
  '19', _('Dim Gray')),
 (
  '20', _('Tan')),
 (
  '21', _('Sea green')),
 (
  '22', _('Pink')),
 (
  '23', _('Medium orchid')),
 (
  '24', _('Indian red')),
 (
  '25', _('Antique white')),
 (
  '26', _('Light green')),
 (
  '27', _('Indigo')),
 (
  '28', _('Dark Green')),
 (
  '29', _('Dark olive')),
 (
  '30', _('Color from skin')),
 (
  '31', _('Black')),
 (
  '32', _('Black light')),
 (
  '33', _('Ultramarine')),
 (
  '34', _('Marengo')),
 (
  '35', _('Ocean blue')),
 (
  '36', _('blue-blue')),
 (
  '37', _('azure')),
 (
  '38', _('Pastel yellow')),
 (
  '39', _('Bright blue-green')),
 (
  '40', _('Persian blue')),
 (
  '41', _('The wet tropical forest')),
 (
  '42', _('Pearl')),
 (
  '43', _('Barvinkovy')),
 (
  '44', _('Violet-blue')),
 (
  '45', _('Chestnut')),
 (
  '46', _('Toxic green')),
 (
  '47', _('Selective yellow'))]
try:
    currs = config.skin.primary_skin.value
    curski = '/usr/share/enigma2/' + currs
    system('cp -f ' + curski + ' ' + '/tmp/sk.xml')
    curren = parse('/tmp/sk.xml')
    system('rm -rf ' + '/tmp/sk.xml')
    curres = curren.getElementsByTagName('resolution')
    screens = curren.getElementsByTagName('screen')
    r = open('/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/colors.xml', 'w')
    newLines = '<colors>\n<color name="1" value=""/>\n<color name="2" value=""/>\n</colors>\n'
    r.write(newLines)
    r.close()
    for ele in screens:
        if ele.getAttribute('name') == 'ChannelSelection':
            widgets = ele.getElementsByTagName('widget')
            for el in widgets:
                if el.getAttribute('name') == 'list':
                    try:
                        eventForeg = el.getAttribute('colorServiceDescription')
                        if not eventForeg.startswith('#'):
                            colors = curren.getElementsByTagName('color')
                            for eve in colors:
                                if eve.getAttribute('name') == eventForeg:
                                    eventForeg = eve.getAttribute('value')

                        r = open('/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/colors.xml', 'r')
                        newLines = ''
                        for line in r.readlines():
                            if line == '<color name="1" value=""/>\n':
                                line = '<color name="1" value="%s"/>\n' % eventForeg
                                newLines += line
                            else:
                                newLines += line

                        r.close()
                        r = open('/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/colors.xml', 'w')
                        r.write(newLines)
                        r.close()
                    except:
                        try:
                            eventForeg = el.getAttribute('foregroundColorEvent')
                            if not eventForeg.startswith('#'):
                                colors = curren.getElementsByTagName('color')
                                for eve in colors:
                                    if eve.getAttribute('name') == eventForeg:
                                        eventForeg = eve.getAttribute('value')

                            r = open('/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/colors.xml', 'r')
                            newLines = ''
                            for line in r.readlines():
                                if line == '<color name="1" value=""/>\n':
                                    line = '<color name="1" value="%s"/>\n' % eventForeg
                                    newLines += line
                                else:
                                    newLines += line

                            r.close()
                            r = open('/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/colors.xml', 'w')
                            r.write(newLines)
                            r.close()
                        except:
                            pass

                    try:
                        eventForegSel = el.getAttribute('colorServiceDescriptionSelected')
                        if not eventForegSel.startswith('#'):
                            colors = curren.getElementsByTagName('color')
                            for eve in colors:
                                if eve.getAttribute('name') == eventForegSel:
                                    eventForegSel = eve.getAttribute('value')

                        r = open('/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/colors.xml', 'r')
                        newLines = ''
                        for line in r.readlines():
                            if line == '<color name="2" value=""/>\n':
                                line = '<color name="2" value="%s"/>\n' % eventForegSel
                                newLines += line
                            else:
                                newLines += line

                        r.close()
                        r = open('/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/colors.xml', 'w')
                        r.write(newLines)
                        r.close()
                    except:
                        try:
                            eventForegSel = el.getAttribute('foregroundColorEventSelected')
                            if not eventForegSel.startswith('#'):
                                colors = curren.getElementsByTagName('color')
                                for eve in colors:
                                    if eve.getAttribute('name') == eventForegSel:
                                        eventForegSel = eve.getAttribute('value')

                            r = open('/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/colors.xml', 'r')
                            newLines = ''
                            for line in r.readlines():
                                if line == '<color name="2" value=""/>\n':
                                    line = '<color name="2" value="%s"/>\n' % eventForegSel
                                    newLines += line
                                else:
                                    newLines += line

                            r.close()
                            r = open('/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/colors.xml', 'w')
                            r.write(newLines)
                            r.close()
                        except:
                            pass

                    break

    for ele in curres:
        reso = ele.getAttribute('xres')

    sizeSk = int(reso)
    if sizeSk == 1920:
        fontdic = [
         (
          '1', '22'),
         (
          '2', '23'),
         (
          '3', '24'),
         (
          '4', '25'),
         (
          '5', '26'),
         (
          '6', '27'),
         (
          '7', '28'),
         (
          '8', '29'),
         (
          '9', '30'),
         (
          '10', '31'),
         (
          '11', '32'),
         (
          '12', '33'),
         (
          '13', '34'),
         (
          '14', '35'),
         (
          '15', '36'),
         (
          '16', '37'),
         (
          '17', '38'),
         (
          '18', '39'),
         (
          '19', '40'),
         (
          '20', _('Size from skin'))]
    else:
        fontdic = [
         (
          '1', '14'),
         (
          '2', '15'),
         (
          '3', '16'),
         (
          '4', '17'),
         (
          '5', '18'),
         (
          '6', '19'),
         (
          '7', '20'),
         (
          '8', '21'),
         (
          '9', '22'),
         (
          '10', '23'),
         (
          '11', '24'),
         (
          '12', '25'),
         (
          '13', '26'),
         (
          '14', '27'),
         (
          '15', '28'),
         (
          '16', '29'),
         (
          '17', '30'),
         (
          '18', '31'),
         (
          '19', '32'),
         (
          '20', _('Size from skin'))]
except:
    fontdic = [
     (
      '1', '14'),
     (
      '2', '15'),
     (
      '3', '16'),
     (
      '4', '17'),
     (
      '5', '18'),
     (
      '6', '19'),
     (
      '7', '20'),
     (
      '8', '21'),
     (
      '9', '22'),
     (
      '10', '23'),
     (
      '11', '24'),
     (
      '12', '25'),
     (
      '13', '26'),
     (
      '14', '27'),
     (
      '15', '28'),
     (
      '16', '29'),
     (
      '17', '30'),
     (
      '18', '31'),
     (
      '19', '32'),
     (
      '20', _('Size from skin'))]

config.plugins.ExtraChannelSelection.showline = ConfigYesNo(default=True)
config.plugins.ExtraChannelSelection.colshowline = ConfigSelection(default='30', choices=colordic)
config.plugins.ExtraChannelSelection.coltext = ConfigSelection(default='30', choices=colordic)
config.plugins.ExtraChannelSelection.colormode = ConfigYesNo(default=True)
config.plugins.ExtraChannelSelection.piconmode = ConfigYesNo(default=True)
config.plugins.ExtraChannelSelection.picomode = ConfigSelection(default='2', choices=[('1', _('on left')), ('2', _('on right'))])
config.plugins.ExtraChannelSelection.bigpicomode = ConfigSelection(default='1', choices=[('1', _('60 pixels')), ('2', _('90 pixels'))])
config.plugins.ExtraChannelSelection.listmode = ConfigYesNo(default=False)
config.plugins.ExtraChannelSelection.barmode = ConfigSelection(default='1', choices=[('1', _('ProgressBar with color')), ('2', _('ProgressBar with pixmap'))])
config.plugins.ExtraChannelSelection.picbar = ConfigSelection(default='1', choices=[('1', _('Pixmap from skin')),
 (
  '2', _('Light green pixmap')),
 (
  '3', _('Dark blue pixmap')),
 (
  '4', _('Dark green pixmap')),
 (
  '5', _('Red pixmap')),
 (
  '6', _('Striped blue pixmap')),
 (
  '7', _('Bright yellow pixmap')),
 (
  '8', _('Black pixmap')),
 (
  '9', _('Light blue pixmap')),
 (
  '10', _('Varicoloured pixmap')),
 (
  '11', _('Versicolor pixmap')),
 (
  '12', _('Dark yellow pixmap'))])
config.plugins.ExtraChannelSelection.picicocrypt = ConfigSelection(default='2', choices=[('1', _('Icon dollar')),
 (
  '2', _('Denomination')),
 (
  '3', _('Icon from OpenPli')),
 (
  '4', _('Lock')),
 (
  '5', _('Key on a black background')),
 (
  '6', _('Key without background')),
 (
  '7', _('Yellow')),
 (
  '8', _('Dollar on a white background')),
 (
  '9', _('Orange')),
 (
  '10', _('Dollar on a blue background')),
 (
  '11', _('Dollar on a yellow background')),
 (
  '12', _('Euro on a red background')),
 (
  '13', _('Key on a red background')),
 (
  '14', _('Dollar on a red background')),
 (
  '15', _('Blue'))])
config.plugins.ExtraChannelSelection.linemode = ConfigSelection(default='1', choices=[('1', _('60 pixels')), ('2', _('48 pixels'))])
config.plugins.ExtraChannelSelection.percshow = ConfigYesNo(default=True)
config.plugins.ExtraChannelSelection.percmode = ConfigSelection(default='1', choices=[('1', _('Percent without brackets')), ('2', _('Percent in brackets'))])
config.plugins.ExtraChannelSelection.eventmode = ConfigSelection(default='1', choices=[('1', _('Event without brackets')), ('2', _('Event in brackets')), ('3', _('Event through a dash'))])
config.plugins.ExtraChannelSelection.recordmode = ConfigSelection(default='0', choices=[('0', _('None')),
 (
  '1', _('Left from servicename')),
 (
  '2', _('Right from servicename')),
 (
  '3', _('Red colored'))])
config.plugins.ExtraChannelSelection.colremain = ConfigSelection(default='30', choices=colordic)
config.plugins.ExtraChannelSelection.colselremain = ConfigSelection(default='30', choices=colordic)
config.plugins.ExtraChannelSelection.colnum = ConfigSelection(default='30', choices=colordic)
config.plugins.ExtraChannelSelection.colselnum = ConfigSelection(default='30', choices=colordic)
config.plugins.ExtraChannelSelection.colend = ConfigSelection(default='30', choices=colordic)
config.plugins.ExtraChannelSelection.colselend = ConfigSelection(default='30', choices=colordic)
config.plugins.ExtraChannelSelection.colbar = ConfigSelection(default='30', choices=colordic)
config.plugins.ExtraChannelSelection.colbarsel = ConfigSelection(default='30', choices=colordic)
config.plugins.ExtraChannelSelection.colborder = ConfigSelection(default='30', choices=colordic)
config.plugins.ExtraChannelSelection.colbordersel = ConfigSelection(default='30', choices=colordic)
config.plugins.ExtraChannelSelection.colname = ConfigSelection(default='30', choices=colordic)
config.plugins.ExtraChannelSelection.colnamesel = ConfigSelection(default='30', choices=colordic)
config.plugins.ExtraChannelSelection.colperc = ConfigSelection(default='30', choices=colordic)
config.plugins.ExtraChannelSelection.colpercsel = ConfigSelection(default='30', choices=colordic)
config.plugins.ExtraChannelSelection.colevent = ConfigSelection(default='30', choices=colordic)
config.plugins.ExtraChannelSelection.coleventsel = ConfigSelection(default='30', choices=colordic)
config.plugins.ExtraChannelSelection.colsat = ConfigSelection(default='30', choices=colordic)
config.plugins.ExtraChannelSelection.colselsat = ConfigSelection(default='30', choices=colordic)
config.plugins.ExtraChannelSelection.fontnum = ConfigSelection(default='20', choices=fontdic)
config.plugins.ExtraChannelSelection.fontperc = ConfigSelection(default='20', choices=fontdic)
config.plugins.ExtraChannelSelection.fontname = ConfigSelection(default='20', choices=fontdic)
config.plugins.ExtraChannelSelection.fontevent = ConfigSelection(default='20', choices=fontdic)
config.plugins.ExtraChannelSelection.fontend = ConfigSelection(default='20', choices=fontdic)
config.plugins.ExtraChannelSelection.fontrem = ConfigSelection(default='20', choices=fontdic)
config.plugins.ExtraChannelSelection.fonttxt = ConfigSelection(default='20', choices=fontdic)
config.plugins.ExtraChannelSelection.fontsat = ConfigSelection(default='20', choices=fontdic)
config.plugins.ExtraChannelSelection.channsum = ConfigYesNo(default=True)
config.plugins.ExtraChannelSelection.showsky = ConfigYesNo(default=True)
config.plugins.ExtraChannelSelection.showcurr = ConfigYesNo(default=True)
config.plugins.ExtraChannelSelection.showprov = ConfigYesNo(default=True)
config.plugins.ExtraChannelSelection.shownew = ConfigYesNo(default=True)
config.plugins.ExtraChannelSelection.showhd = ConfigYesNo(default=True)
config.plugins.ExtraChannelSelection.piconpathmode = ConfigSelection(default='0', choices=[('0', _('Standart')),
 (
  '1', '/media/usb/transparentpicon/'),
 (
  '2', '/media/usb/blackpicon/'),
 (
  '3', '/media/usb/whitepicon/'),
 (
  '4', '/media/usb/colorpicon/'),
 (
  '5', '/media/hdd/transparentpicon/'),
 (
  '6', '/media/hdd/blackpicon/'),
 (
  '7', '/media/hdd/whitepicon/'),
 (
  '8', '/media/hdd/colorpicon/')])
allow = False

def namehours():
    return _('h')


def namemin():
    return _('min')


def alreadyPatch():
    status = 0
    if fileExists(MAP_FILE):
        r = open(MAP_FILE, 'r')
        exist = False
        for line in r.readlines():
            if exist:
                if line.__contains__('ServiceUp'):
                    status += 1
                elif line.__contains__('ServicePageUp'):
                    status += 1
                    break
            if line.__contains__('<map context="ChannelSelectBaseActions">'):
                exist = True

        r.close()
    if status == 2:
        return True
    return False


def StartMainSession(reason, **kwargs):
    global allow
    MAPPATH = '/usr/share/enigma2/'
    FILEPATH = '/usr/lib/enigma2/python/Components/'
    CHANNELPATH = '/usr/lib/enigma2/python/Screens/'
    MAP_FILE = '/usr/share/enigma2/keymap.xml'
    CHECKPATH = '/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/forchek/'
    allow = False
    import os
    if fileExists(CHANNELPATH + 'ChannelSelection.pyo'):
        if os.path.getsize(CHANNELPATH + 'ChannelSelection.pyo') != os.path.getsize(CHECKPATH + 'ChannelSelection.pyo'):
            allow = False
        else:
            allow = True
        allow = True
    if allow:
        if config.plugins.ExtraChannelSelection.enabled.value:
            if not alreadyPatch():
                mapreplace = True
                try:
                    if fileExists(MAPPATH + 'keymap-ori.xml'):
                        if os.path.getsize(MAPPATH + 'keymap.xml') != os.path.getsize(MAPPATH + 'keymap-ori.xml'):
                            system('rm -rf ' + MAPPATH + 'keymap-ori.xml')
                            system('cp -f ' + MAPPATH + 'keymap.xml ' + MAPPATH + 'keymap-ori.xml')
                            mapreplace = False
                    else:
                        system('cp -f ' + MAPPATH + 'keymap.xml ' + MAPPATH + 'keymap-ori.xml')
                        mapreplace = False
                except:
                    pass

                r = open(MAP_FILE, 'r')
                rewrite = False
                newLines = ''
                for line in r.readlines():
                    if rewrite and line.__contains__('</map>'):
                        line = line.replace('</map>', '\t<key id="KEY_UP" mapto="ServiceUp" flags="m" />\n\t\t<key id="KEY_DOWN" mapto="ServiceDown" flags="m" />\n\t</map>')
                        rewrite = False
                    if line.__contains__('<map context="ChannelSelectBaseActions">'):
                        rewrite = True
                    newLines += line

                r.close()
                r = open(MAP_FILE, 'w')
                r.write(newLines)
                r.close()
            sizeSki = getDesktop(0).size().width()
            if sizeSki == 1920:
                import ServiceListhd, Screens.ChannelSelection, ChannelSelectionhd, Screens.InfoBarGenerics, Screens.EpgSelection
                Screens.InfoBarGenerics.ChannelSelection = ChannelSelectionhd.ChannelSelection
                Screens.EpgSelection.ChannelSelection = ChannelSelectionhd
                Screens.ChannelSelection.ServiceList = ServiceListhd.ServiceList
                Screens.ChannelSelection.refreshServiceList = ServiceListhd.refreshServiceList
            else:
                import ServiceList, Screens.ChannelSelection, ChannelSelection, Screens.InfoBarGenerics, Screens.EpgSelection
                Screens.InfoBarGenerics.ChannelSelection = ChannelSelection.ChannelSelection
                Screens.EpgSelection.ChannelSelection = ChannelSelection
                Screens.ChannelSelection.ServiceList = ServiceList.ServiceList
                Screens.ChannelSelection.refreshServiceList = ServiceList.refreshServiceList
    return


class PluginHistory(Screen):
    sizeSkin = getDesktop(0).size().width()
    if sizeSkin == 1920:
        skin = '\n<screen name="PluginHistory" position="center,center" size="895,675" title="Plugin History">\n  <widget name="text" position="22,20" size="850,595" itemHeight="38" font="Regular;30" halign="left"/>\n  <ePixmap position="325,663" zPosition="1" size="245,2" pixmap="/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/images/red.png" alphatest="blend" />\n  <widget source="red_key" render="Label" position="325,625" zPosition="2" size="245,38" font="Regular; 30" halign="center" valign="center" backgroundColor="#41000000" foregroundColor="#00dddddd" transparent="1" />\n</screen>'
    else:
        skin = '\n<screen name="PluginHistory" position="center,center" size="595,450" title="Plugin History">\n  <widget name="text" position="15,20" size="720,410" itemHeight="28" font="Regular;20" halign="left"/>\n  <ePixmap position="215,438" zPosition="1" size="165,2" pixmap="/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/images/red.png" alphatest="blend" />\n  <widget source="red_key" render="Label" position="215,408" zPosition="2" size="165,30" font="Regular; 20" halign="center" valign="center" backgroundColor="#41000000" foregroundColor="#00dddddd" transparent="1" />\n</screen>'

    def __init__(self, session):
        self.session = session
        Screen.__init__(self, session)
        self.setTitle(_('Plugin History'))
        self['shortcuts'] = ActionMap(['ShortcutActions', 'WizardActions'], {'cancel': (self.cancel), 'back': (self.cancel), 
           'red': (self.cancel), 
           'ok': (self.cancel)})
        self['red_key'] = StaticText(_('Close'))
        self['text'] = Label(_('Author: a.k.a. Uchkun (c).\n\nSpecial thanks to Nikolasi for saved time for the\nderivation of Picon.\n\nThe idea of the plugin was born in autumn 2012 in\nthe study of the source listboxservice.cpp.\nIt has become clear that it is achievable.\nA designer multicontent own even novice programmers\nto Enigma.\n\nPurses for transfers:\nWebMoney\nZ356196865451\nR105983132832'))
        return

    def cancel(self):
        self.close()
        return


class BackScreen(Screen):
    sizeSkin = getDesktop(0).size().width()
    if sizeSkin == 1920:
        skin = '\n<screen name="BackScreen" position="center,center" size="895,675" title="Backup settings for current skin">\n  <widget name="text" position="110,530" size="700,40" foregroundColor="#00009a00" font="Regular;32" halign="right" transparent="1" />\n  <widget name="txt" position="50,430" size="795,40" foregroundColor="#00696969" halign="center" font="Regular;34" transparent="1" />\n  <ePixmap position="325,663" zPosition="1" size="245,3" pixmap="/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/images/red.png" alphatest="blend" />\n  <widget source="red_key" render="Label" position="325,625" zPosition="2" size="245,38" font="Regular; 30" halign="center" valign="center" backgroundColor="#41000000" foregroundColor="#00dddddd" transparent="1" />\n  <widget source="menu" render="Listbox" position="22,20" size="850,150" scrollbarMode="showOnDemand" transparent="1">\n    <convert type="TemplatedMultiContent">\n      {"template": [\n        MultiContentEntryText(pos = (15, 5), size = (820, 40), font=0, flags = RT_HALIGN_LEFT, text = 0)\n        ],\n        "fonts": [gFont("Regular", 34)],\n        "itemHeight": 50\n      }\n    </convert>\n  </widget>\n</screen>'
    else:
        skin = '\n<screen name="BackScreen" position="center,center" size="595,450" title="Backup settings for current skin">\n  <widget name="text" position="69,339" size="500,30" foregroundColor="#00009a00" font="Regular;22" halign="right" transparent="1" />\n  <widget name="txt" position="29,237" size="535,30" foregroundColor="#00696969" halign="center" font="Regular;24" transparent="1" />\n  <ePixmap position="215,438" zPosition="1" size="165,2" pixmap="/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/images/red.png" alphatest="blend" />\n  <widget source="red_key" render="Label" position="215,408" zPosition="2" size="165,30" font="Regular; 20" halign="center" valign="center" backgroundColor="#41000000" foregroundColor="#00dddddd" transparent="1" />\n  <widget source="menu" render="Listbox" position="15,10" size="570,100" scrollbarMode="showOnDemand" transparent="1">\n    <convert type="TemplatedMultiContent">\n      {"template": [\n        MultiContentEntryText(pos = (15, 5), size = (570, 30), font=0, flags = RT_HALIGN_LEFT, text = 0)\n        ],\n        "fonts": [gFont("Regular", 23)],\n        "itemHeight": 40\n      }\n    </convert>\n  </widget>\n</screen>'

    def __init__(self, session):
        self.session = session
        Screen.__init__(self, session)
        self.setTitle(_('Backup settings for current skin'))
        self['shortcuts'] = ActionMap(['ShortcutActions', 'WizardActions'], {'cancel': (self.cancel), 'back': (self.cancel), 
           'red': (self.cancel), 
           'ok': (self.action)})
        currentSkin = config.skin.primary_skin.value
        if currentSkin == 'skin.xml':
            currentSkin = 'Default_skin'
        else:
            currentSkin = currentSkin[:currentSkin.rfind('/')]
        self['red_key'] = StaticText(_('Close'))
        self['text'] = Label(_('Current skin - %s') % currentSkin)
        self['txt'] = Label(_('Press OK for action'))
        self.list = []
        self['menu'] = List(self.list)
        self.createList()
        return

    def createList(self):
        self.list = []
        self.list.append((_('Save settings for current skin'), 'save'))
        self.list.append((_('Restore settings for current skin'), 'restore'))
        self['menu'].setList(self.list)
        return

    def action(self, selectEntry=None):
        if selectEntry == None:
            selectEntry = self['menu'].getCurrent()[1]
            currentSkin = config.skin.primary_skin.value
            if currentSkin == 'skin.xml':
                currentSkin = 'Default_skin'
            else:
                currentSkin = currentSkin[:currentSkin.rfind('/')]
            if selectEntry == 'save':
                if fileExists((BACKUPPATH + '%s') % currentSkin):
                    self.session.openWithCallback(self.saveset, MessageBox, _('Backup file is already exists!\nDo you want rewrite backup file?'), MessageBox.TYPE_YESNO, timeout=8, default=False)
                elif not fileExists((BACKUPPATH + '%s') % currentSkin):
                    w = open('/etc/enigma2/settings', 'r')
                    e = w.read()
                    w.close()
                    r = e.split('\n')
                    s = []
                    for x in r:
                        if x.__contains__('ExtraChannelSelection'):
                            s.append(x)

                    q = ('\n').join(s)
                    l = q + '\n'
                    h = open('/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/backup/%s' % currentSkin, 'w')
                    h.write(l)
                    h.close()
                    self.session.open(MessageBox, _('Settings successfully saved!'), MessageBox.TYPE_INFO, timeout=6)
            elif selectEntry == 'restore':
                if not fileExists((BACKUPPATH + '%s') % currentSkin):
                    self.session.open(MessageBox, _('Backup file not exists!'), MessageBox.TYPE_INFO, timeout=6)
                elif fileExists((BACKUPPATH + '%s') % currentSkin):
                    self.session.openWithCallback(self.restoreset, MessageBox, _('Do not be afraid, now image will be stopped and restarted for the restore the settings of ExtraChannelSelection for the current skin.\nRestore settings?'), MessageBox.TYPE_YESNO, timeout=5)
        return

    def cancel(self):
        self.close()
        return

    def saveset(self, answer):
        if answer is True:
            w = open('/etc/enigma2/settings', 'r')
            e = w.read()
            w.close()
            r = e.split('\n')
            s = []
            for x in r:
                if x.__contains__('ExtraChannelSelection'):
                    s.append(x)

            q = ('\n').join(s)
            l = q + '\n'
            currentSkin = config.skin.primary_skin.value
            if currentSkin == 'skin.xml':
                currentSkin = 'Default_skin'
            else:
                currentSkin = currentSkin[:currentSkin.rfind('/')]
            h = open('/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/backup/%s' % currentSkin, 'w')
            h.write(l)
            h.close()
            self.session.open(MessageBox, _('Settings successfully saved!'), MessageBox.TYPE_INFO, timeout=6)
        return

    def restoreset(self, answer):
        if answer is True:
            w = open('/etc/enigma2/settings', 'r')
            e = w.read()
            w.close()
            r = e.split('\n')
            s = []
            for x in r:
                if not x.__contains__('ExtraChannelSelection'):
                    s.append(x)

            j = ('\n').join(s)
            currentSkin = config.skin.primary_skin.value
            if currentSkin == 'skin.xml':
                currentSkin = 'Default_skin'
            else:
                currentSkin = currentSkin[:currentSkin.rfind('/')]
            p = open('/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/backup/%s' % currentSkin, 'r')
            l = p.read()
            p.close()
            m = j + l
            v = open('/tmp/settings', 'w')
            v.write(m)
            v.close()
            if fileExists(RPATH + 'linemode'):
                system('rm -rf ' + RPATH + 'linemode')
            if fileExists(RPATH + 'listmode'):
                system('rm -rf ' + RPATH + 'listmode')
            if fileExists(RPATH + 'enabled'):
                system('rm -rf ' + RPATH + 'enabled')
            if fileExists(RPATH + 'doubmode'):
                system('rm -rf ' + RPATH + 'doubmode')
            if fileExists(RPATH + 'piconpathmodeq'):
                system('rm -rf ' + RPATH + 'piconpathmodeq')
            if fileExists(RPATH + 'piconpathmodew'):
                system('rm -rf ' + RPATH + 'piconpathmodew')
            if fileExists(RPATH + 'piconpathmodee'):
                system('rm -rf ' + RPATH + 'piconpathmodee')
            if fileExists(RPATH + 'piconpathmoder'):
                system('rm -rf ' + RPATH + 'piconpathmoder')
            if fileExists(RPATH + 'piconpathmodet'):
                system('rm -rf ' + RPATH + 'piconpathmodet')
            if fileExists(RPATH + 'piconpathmodey'):
                system('rm -rf ' + RPATH + 'piconpathmodey')
            if fileExists(RPATH + 'piconpathmodeu'):
                system('rm -rf ' + RPATH + 'piconpathmodeu')
            if fileExists(RPATH + 'piconpathmodei'):
                system('rm -rf ' + RPATH + 'piconpathmodei')
            if fileExists(RPATH + 'piconpathmodeo'):
                system('rm -rf ' + RPATH + 'piconpathmodeo')
            from Screens.Console import Console
            print('run script')
            script = '/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/script/restore_settings.sh'
            os.chmod(script, 493)
            self.session.open(Console, cmdlist=[script])
        return


class ExtraChannelSelection(Screen, ConfigListScreen):
    PiconPaths = ('/usr/share/enigma2/picon/', '/media/cf/picon/', '/media/usb/picon/',
                  '/media/ba/picon/', '/media/hdd/picon/', '/picon/')
    sizeSkin = getDesktop(0).size().width()
    if sizeSkin == 1920:
        skin = '\n<screen name="ExtraChannelSelection" position="center,center" size="1840,960" title="ExtraChannelSelection settings">\n  <widget position="30,25" size="1310,590" name="config" itemHeight="45" foregroundColor="#00ffcc33" font="Regular;32" scrollbarMode="showOnDemand" />\n  <widget name="description" position="1365,25" size="450,590" font="Regular;28" halign="left" valign="center"/>\n  <ePixmap position="1004,930" zPosition="1" size="250,3" pixmap="/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/images/yellow.png" alphatest="blend" />\n  <widget source="yellow_key" render="Label" position="1004,870" zPosition="2" size="250,45" font="Regular; 30" halign="center" valign="center" backgroundColor="#41000000" foregroundColor="#00dddddd" transparent="1" />\n  <ePixmap position="168,930" zPosition="1" size="250,3" pixmap="/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/images/red.png" alphatest="blend" />\n  <widget source="red_key" render="Label" position="168,870" zPosition="2" size="250,45" font="Regular; 30" halign="center" valign="center" backgroundColor="#41000000" foregroundColor="#00dddddd" transparent="1" />\n  <ePixmap position="1422,930" zPosition="1" size="250,3" pixmap="/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/images/blue.png" alphatest="blend" />\n  <widget source="blue_key" render="Label" position="1422,870" zPosition="2" size="250,45" font="Regular; 30" halign="center" valign="center" backgroundColor="#41000000" foregroundColor="#00dddddd" transparent="1" />\n  <eLabel position="15,625" size="1,235" backgroundColor="#5395c3"/>\n  <eLabel position="15,860" size="1140,1" backgroundColor="#5395c3"/>\n  <eLabel position="15,625" size="1140,1" backgroundColor="#5395c3"/>\n  <eLabel position="1155,625" size="1,235" backgroundColor="#5395c3"/>\n  <widget name="test" position="30,650" size="1750,180" selectionDisabled="1" zPosition="5" transparent="1" />\n  <ePixmap position="586,930" zPosition="1" size="250,2" pixmap="/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/images/green.png" alphatest="blend" />\n  <widget source="green_key" render="Label" position="586,870" zPosition="2" size="250,45" font="Regular; 30" halign="center" valign="center" backgroundColor="#41000000" foregroundColor="#00dddddd" transparent="1" />\n</screen>'
    else:
        skin = '\n<screen name="ExtraChannelSelection" position="center,center" size="1230,640" title="ExtraChannelSelection settings">\n  <widget position="15,10" size="874,394" name="config" itemHeight="30" foregroundColor="#00ffcc33" font="Regular;21" scrollbarMode="showOnDemand" />\n  <widget name="description" position="905,20" size="310,374" font="Regular;19" halign="left" valign="center"/>\n  <ePixmap position="951,620" zPosition="1" size="165,2" pixmap="/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/images/yellow.png" alphatest="blend" />\n  <widget source="yellow_key" render="Label" position="951,590" zPosition="2" size="165,30" font="Regular; 20" halign="center" valign="center" backgroundColor="#41000000" foregroundColor="#00dddddd" transparent="1" />\n  <ePixmap position="114,620" zPosition="1" size="165,2" pixmap="/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/images/red.png" alphatest="blend" />\n  <widget source="red_key" render="Label" position="114,590" zPosition="2" size="165,30" font="Regular; 20" halign="center" valign="center" backgroundColor="#41000000" foregroundColor="#00dddddd" transparent="1" />\n  <ePixmap position="672,620" zPosition="1" size="165,2" pixmap="/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/images/blue.png" alphatest="blend" />\n  <widget source="blue_key" render="Label" position="672,590" zPosition="2" size="165,30" font="Regular; 20" halign="center" valign="center" backgroundColor="#41000000" foregroundColor="#00dddddd" transparent="1" />\n  <eLabel position="10,410" size="1,150" backgroundColor="#5395c3"/>\n  <eLabel position="10,560" size="760,1" backgroundColor="#5395c3"/>\n  <eLabel position="10,410" size="760,1" backgroundColor="#5395c3"/>\n  <eLabel position="770,410" size="1,150" backgroundColor="#5395c3"/>\n  <widget name="test" position="20,425" size="1170,120" selectionDisabled="1" zPosition="5" transparent="1" />\n  <ePixmap position="393,620" zPosition="1" size="165,2" pixmap="/usr/lib/enigma2/python/Plugins/SystemPlugins/ExtraChannelSelection/images/green.png" alphatest="blend" />\n  <widget source="green_key" render="Label" position="393,590" zPosition="2" size="165,30" font="Regular; 20" halign="center" valign="center" backgroundColor="#41000000" foregroundColor="#00dddddd" transparent="1" />\n</screen>'

    def __init__(self, session):
        Screen.__init__(self, session)
        if config.plugins.ExtraChannelSelection.linemode.value == '1':
            a = open('/tmp/linemode', 'w')
            a.write('a\n')
            a.close()
        if config.plugins.ExtraChannelSelection.listmode.value:
            a = open('/tmp/listmode', 'w')
            a.write('a\n')
            a.close()
        if config.plugins.ExtraChannelSelection.enabled.value:
            c = open('/tmp/enabled', 'w')
            c.write('a\n')
            c.close()
        if config.plugins.ExtraChannelSelection.doubmode.value:
            h = open('/tmp/doubmode', 'w')
            h.write('a\n')
            h.close()
        if config.plugins.ExtraChannelSelection.piconpathmode.value == '0':
            h = open('/tmp/piconpathmodeq', 'w')
            h.write('a\n')
            h.close()
        if config.plugins.ExtraChannelSelection.piconpathmode.value == '1':
            h = open('/tmp/piconpathmodew', 'w')
            h.write('a\n')
            h.close()
        if config.plugins.ExtraChannelSelection.piconpathmode.value == '2':
            h = open('/tmp/piconpathmodee', 'w')
            h.write('a\n')
            h.close()
        if config.plugins.ExtraChannelSelection.piconpathmode.value == '3':
            h = open('/tmp/piconpathmoder', 'w')
            h.write('a\n')
            h.close()
        if config.plugins.ExtraChannelSelection.piconpathmode.value == '4':
            h = open('/tmp/piconpathmodet', 'w')
            h.write('a\n')
            h.close()
        if config.plugins.ExtraChannelSelection.piconpathmode.value == '5':
            h = open('/tmp/piconpathmodey', 'w')
            h.write('a\n')
            h.close()
        if config.plugins.ExtraChannelSelection.piconpathmode.value == '6':
            h = open('/tmp/piconpathmodeu', 'w')
            h.write('a\n')
            h.close()
        if config.plugins.ExtraChannelSelection.piconpathmode.value == '7':
            h = open('/tmp/piconpathmodei', 'w')
            h.write('a\n')
            h.close()
        if config.plugins.ExtraChannelSelection.piconpathmode.value == '8':
            h = open('/tmp/piconpathmodeo', 'w')
            h.write('a\n')
            h.close()
        self.setup_title = _('ExtraChannelSelection - Version: %s') % pluginversion
        self['red_key'] = StaticText(_('Close'))
        self['green_key'] = StaticText(_('Save'))
        self['yellow_key'] = StaticText(_('Info'))
        self['blue_key'] = StaticText(_('Backup'))
        self['description'] = Label('')
        self['test'] = TestScreenList([])
        self['setupActions'] = ActionMap(['SetupActions', 'OkCancelActions', 'ColorActions'], {'red': (self.cancel), 'cancel': (self.cancel), 
           'green': (self.save), 
           'yellow': (self.info), 
           'blue': (self.back), 
           'ok': (self.save)}, -2)
        ConfigListScreen.__init__(self, [])
        self.initConfig()
        self.createSetup()
        self.onClose.append(self.__closed)
        self.onLayoutFinish.append(self.__layoutFinished)
        if not self.displayText in self['config'].onSelectionChanged:
            self['config'].onSelectionChanged.append(self.displayText)
        testscr = []
        testscr.append(TestScreenListEntry(config.plugins.ExtraChannelSelection.enabled.value, config.plugins.ExtraChannelSelection.endmode.value, config.plugins.ExtraChannelSelection.text.value, config.plugins.ExtraChannelSelection.nummode.value, config.plugins.ExtraChannelSelection.bordermode.value, config.plugins.ExtraChannelSelection.barpercmode.value, config.plugins.ExtraChannelSelection.iconmode.value, config.plugins.ExtraChannelSelection.crypticonmode.value, config.plugins.ExtraChannelSelection.doubmode.value, config.plugins.ExtraChannelSelection.progress.value, config.plugins.ExtraChannelSelection.percpos.value, config.plugins.ExtraChannelSelection.remmode.value, config.plugins.ExtraChannelSelection.showline.value, config.plugins.ExtraChannelSelection.colshowline.value, config.plugins.ExtraChannelSelection.coltext.value, config.plugins.ExtraChannelSelection.colormode.value, config.plugins.ExtraChannelSelection.piconmode.value, config.plugins.ExtraChannelSelection.picomode.value, config.plugins.ExtraChannelSelection.bigpicomode.value, config.plugins.ExtraChannelSelection.listmode.value, config.plugins.ExtraChannelSelection.barmode.value, config.plugins.ExtraChannelSelection.picbar.value, config.plugins.ExtraChannelSelection.picicocrypt.value, config.plugins.ExtraChannelSelection.linemode.value, config.plugins.ExtraChannelSelection.percshow.value, config.plugins.ExtraChannelSelection.percmode.value, config.plugins.ExtraChannelSelection.eventmode.value, config.plugins.ExtraChannelSelection.recordmode.value, config.plugins.ExtraChannelSelection.colremain.value, config.plugins.ExtraChannelSelection.colselremain.value, config.plugins.ExtraChannelSelection.colnum.value, config.plugins.ExtraChannelSelection.colselnum.value, config.plugins.ExtraChannelSelection.colend.value, config.plugins.ExtraChannelSelection.colselend.value, config.plugins.ExtraChannelSelection.colbar.value, config.plugins.ExtraChannelSelection.colbarsel.value, config.plugins.ExtraChannelSelection.colborder.value, config.plugins.ExtraChannelSelection.colbordersel.value, config.plugins.ExtraChannelSelection.colname.value, config.plugins.ExtraChannelSelection.colnamesel.value, config.plugins.ExtraChannelSelection.colperc.value, config.plugins.ExtraChannelSelection.colpercsel.value, config.plugins.ExtraChannelSelection.colevent.value, config.plugins.ExtraChannelSelection.coleventsel.value, config.plugins.ExtraChannelSelection.colsat.value, config.plugins.ExtraChannelSelection.colselsat.value))
        testscr.reverse()
        self['test'].setList(testscr)
        return

    def testScreen(self):
        testscr = []
        testscr.append(TestScreenListEntry(config.plugins.ExtraChannelSelection.enabled.value, config.plugins.ExtraChannelSelection.endmode.value, config.plugins.ExtraChannelSelection.text.value, config.plugins.ExtraChannelSelection.nummode.value, config.plugins.ExtraChannelSelection.bordermode.value, config.plugins.ExtraChannelSelection.barpercmode.value, config.plugins.ExtraChannelSelection.iconmode.value, config.plugins.ExtraChannelSelection.crypticonmode.value, config.plugins.ExtraChannelSelection.doubmode.value, config.plugins.ExtraChannelSelection.progress.value, config.plugins.ExtraChannelSelection.percpos.value, config.plugins.ExtraChannelSelection.remmode.value, config.plugins.ExtraChannelSelection.showline.value, config.plugins.ExtraChannelSelection.colshowline.value, config.plugins.ExtraChannelSelection.coltext.value, config.plugins.ExtraChannelSelection.colormode.value, config.plugins.ExtraChannelSelection.piconmode.value, config.plugins.ExtraChannelSelection.picomode.value, config.plugins.ExtraChannelSelection.bigpicomode.value, config.plugins.ExtraChannelSelection.listmode.value, config.plugins.ExtraChannelSelection.barmode.value, config.plugins.ExtraChannelSelection.picbar.value, config.plugins.ExtraChannelSelection.picicocrypt.value, config.plugins.ExtraChannelSelection.linemode.value, config.plugins.ExtraChannelSelection.percshow.value, config.plugins.ExtraChannelSelection.percmode.value, config.plugins.ExtraChannelSelection.eventmode.value, config.plugins.ExtraChannelSelection.recordmode.value, config.plugins.ExtraChannelSelection.colremain.value, config.plugins.ExtraChannelSelection.colselremain.value, config.plugins.ExtraChannelSelection.colnum.value, config.plugins.ExtraChannelSelection.colselnum.value, config.plugins.ExtraChannelSelection.colend.value, config.plugins.ExtraChannelSelection.colselend.value, config.plugins.ExtraChannelSelection.colbar.value, config.plugins.ExtraChannelSelection.colbarsel.value, config.plugins.ExtraChannelSelection.colborder.value, config.plugins.ExtraChannelSelection.colbordersel.value, config.plugins.ExtraChannelSelection.colname.value, config.plugins.ExtraChannelSelection.colnamesel.value, config.plugins.ExtraChannelSelection.colperc.value, config.plugins.ExtraChannelSelection.colpercsel.value, config.plugins.ExtraChannelSelection.colevent.value, config.plugins.ExtraChannelSelection.coleventsel.value, config.plugins.ExtraChannelSelection.colsat.value, config.plugins.ExtraChannelSelection.colselsat.value))
        testscr.reverse()
        self['test'].setList(testscr)
        return

    def displayText(self):
        if self['config'].getCurrent() == self.cfg_enabled:
            self['description'].setText(_("Enable or disable the plugin ----------------. Plugin's menu is dynamic. When open any items, other items opened or closed. Restart required."))
        elif self['config'].getCurrent() == self.cfg_text:
            self['description'].setText(_("When enabled, if EPG from TV Guide is not available, will be shown static text - 'No EPG data available'. No restart required."))
        elif self['config'].getCurrent() == self.cfg_coltext:
            self['description'].setText(_("Color selection for the above text - 'No EPG data available'. No restart required."))
        elif self['config'].getCurrent() == self.cfg_listmode:
            self['description'].setText(_('When enabled, each channel in the selector will occupy two lines with additional information, and advanced settings for double-row configuration will appear in the menu, and vice versa, settings for only single-row configuration on the channel list will disappear. Restart required.'))
        elif self['config'].getCurrent() == self.cfg_doubmode:
            self['description'].setText(_('Choose a type of the doubleline channellist.'))
        elif self['config'].getCurrent() == self.cfg_bordermode:
            self['description'].setText(_('When enabled, the long progress-bar will be with a border. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_barpercmode:
            self['description'].setText(_("Showing percent above the progressbar to saving space in the channel list. It is necessary to configure the location of percent and location of progressbar at one side - at the left side or at the right side for both. Location percent set in the same menu in item 'Percent location'. No restart required."))
        elif self['config'].getCurrent() == self.cfg_progress:
            self['description'].setText(_("Configure the location of progress - at the left or at the right side. Keep in mind, if you have included on the previous item 'Bar and percent together', then will need to put a progressbar in the same side with percent. No restart required."))
        elif self['config'].getCurrent() == self.cfg_percpos:
            self['description'].setText(_("Configure the location of percent - at the left or at the right side. Keep in mind, if you have included on the previous item 'Bar and percent together', then will need to put a percent in the same side with progressbar. No restart required."))
        elif self['config'].getCurrent() == self.cfg_recordmode:
            self['description'].setText(_('Configure the location of record indicator - at the left or at the right side. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_iconmode:
            self['description'].setText(_('Configure the location of service icons - at the left or at the right side. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_crypticonmode:
            self['description'].setText(_('Configure the location of crypt icons - at the left or at the right side. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_remmode:
            self['description'].setText(_('Select the type of display the time remaining in the double-row list of channels. Two types, number of minutes or hours with minutes. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_endmode:
            self['description'].setText(_('When enabled, In the double-row channel list will be displayed start-time and end-time of event. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_nummode:
            self['description'].setText(_('Specify whether or not to show number of channels in the channel list. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_barmode:
            self['description'].setText(_("'ProgressBar with color' means that you will need to choose the color for progressbar. At a choice of this option, be convinced that in the skin.xml a certain picture isn't applied to the cursor. 'ProgressBar with pixmap' means that you will need to choose a pixmap as a progressbar. In the version with the picture color will turn richer and brighter. No restart required."))
        elif self['config'].getCurrent() == self.cfg_colbar:
            self['description'].setText(_("Choose a color to the progressbar. Valid only if you select the 'ProgressBar with color'. No restart required."))
        elif self['config'].getCurrent() == self.cfg_colbarsel:
            self['description'].setText(_("Choose a color to the progressbar, when it selected. Valid only if you select the 'ProgressBar with color'. No restart required."))
        elif self['config'].getCurrent() == self.cfg_picbar:
            self['description'].setText(_("Choose a pixmap to the progressbar. Valid only if you select the 'ProgressBar with pixmap'. No restart required."))
        elif self['config'].getCurrent() == self.cfg_colbordersel:
            self['description'].setText(_("Choose a color to the border of progressbar, when it selected. Valid only if you select the 'ProgressBar with pixmap'. No restart required."))
        elif self['config'].getCurrent() == self.cfg_picicocrypt:
            self['description'].setText(_('Choose a pixmap for crypt icon. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_colborder:
            self['description'].setText(_('Choose a color to the border of progressbar. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_colsat:
            self['description'].setText(_('Choose a color to the satlist and providerlist. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_colselsat:
            self['description'].setText(_('Choose a color to the satlist and providerlist, when it selected. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_percshow:
            self['description'].setText(_('When enabled, percent will be displayed. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_percmode:
            self['description'].setText(_('Select the type of display of percent. In brackets or without brackets, or you can disable display of percent. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_eventmode:
            self['description'].setText(_('Select the type of display the name of the event. In brackets or without brackets, or through a dash. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_piconmode:
            self['description'].setText(_('Specify whether or not to show picons in the channel list. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_picomode:
            self['description'].setText(_('Configure the location of picons - at the left or at the right side in the channel list. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_bigpicomode:
            self['description'].setText(_('Choose height for picon in channel list in double-line mode. It working only for full HD skin. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_colormode:
            self['description'].setText(_("If you choose 'yes', a plug-in will try to choose colors for elements of the list of channels from settings of the current skin. Some colors in a skin can be not set. Also there are elements for which colors in skins aren't set in general. To these cases, default colors will be applied. If you choose 'no', further will it is necessary to adjust colors for all elements. No restart required."))
        elif self['config'].getCurrent() == self.cfg_fontnum:
            self['description'].setText(_('Select a font size for the number of channel. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_fontperc:
            self['description'].setText(_('Select a font size for the percent. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_fontname:
            self['description'].setText(_('Select a font size for the Service Name. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_fontevent:
            self['description'].setText(_('Select a font size for the Event. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_fontend:
            self['description'].setText(_('Select a font size for the start- and end- time for event in the double-row list of channels. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_fontrem:
            self['description'].setText(_('Select a font size for the remaining time for event in the double-row list of channels. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_fonttxt:
            self['description'].setText(_("Select a font size for the text - 'No EPG data available'. No restart required."))
        elif self['config'].getCurrent() == self.cfg_fontsat:
            self['description'].setText(_('Select a font size for the satlist and providerlist. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_colnum:
            self['description'].setText(_('Choose a color for the number of channel. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_colselnum:
            self['description'].setText(_('Choose a color for the number of channel, when it selected. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_colname:
            self['description'].setText(_('Choose a color for the Service Name. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_colnamesel:
            self['description'].setText(_('Choose a color for the Service Name, when it selected. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_colperc:
            self['description'].setText(_('Choose a color for the percent. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_colpercsel:
            self['description'].setText(_('Choose a color for the percent, when it selected. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_colevent:
            self['description'].setText(_('Choose a color for the Event. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_coleventsel:
            self['description'].setText(_('Choose a color for the Event, when it selected. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_colend:
            self['description'].setText(_('Choose a color for the start- and end- time for event in the double-row list of channels. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_colselend:
            self['description'].setText(_('Choose a color for the start- and end- time for event in the double-row list of channels, when it selected. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_colremain:
            self['description'].setText(_('Choose a color for the remaining time for event in the double-row list of channels. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_colselremain:
            self['description'].setText(_('Choose a color for the remaining time for event in the double-row list of channels, when it selected. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_linemode:
            self['description'].setText(_('Choose height for item in channel list in single-line mode. It working only for full HD skin. Restart required.'))
        elif self['config'].getCurrent() == self.cfg_showline:
            self['description'].setText(_('Choose, separator line will be shown or not will be shown the in the channel list. It not working for long-progressbar option. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_colshowline:
            self['description'].setText(_('Choose a color for the separator line in the channel list. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_timericonmode:
            self['description'].setText(_('Configure the location of icons for waiting timers - at the left or at the right side. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_channsum:
            self['description'].setText(_('Choose, show or not show the number of channels in the satellite list. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_showsky:
            self['description'].setText(_('Choose, show or not show Sky subservices in the satellite list. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_showcurr:
            self['description'].setText(_('Choose, show or not show current transponder in the satellite list. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_showprov:
            self['description'].setText(_('Choose, show or not show providers in the satellite list. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_shownew:
            self['description'].setText(_('Choose, show or not show new channels in the satellite list. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_showhd:
            self['description'].setText(_('Choose, show or not show separately show hd channels in the satellite list. No restart required.'))
        elif self['config'].getCurrent() == self.cfg_piconpathmode:
            self['description'].setText(_('Choose, on which folder exists your picons. Restart required.'))
        return

    def __closed(self):
        return

    def __layoutFinished(self):
        self.setTitle(self.setup_title)
        return

    def initConfig(self):

        def getPrevValues(section):
            res = {}
            for key, val in list(section.content.items.items()):
                if isinstance(val, ConfigSubsection):
                    res[key] = getPrevValues(val)
                else:
                    res[key] = val.value

            return res

        self.ECS = config.plugins.ExtraChannelSelection
        self.prev_values = getPrevValues(self.ECS)
        self.cfg_enabled = getConfigListEntry(_('ExtraChannelSelection Enabled'), self.ECS.enabled)
        self.cfg_text = getConfigListEntry(_('The text in the absence of an event'), self.ECS.text)
        self.cfg_coltext = getConfigListEntry(_('Color for this text'), self.ECS.coltext)
        self.cfg_linemode = getConfigListEntry(_('Channel line height for full HD'), self.ECS.linemode)
        self.cfg_bigpicomode = getConfigListEntry(_('Channel picon height for full HD'), self.ECS.bigpicomode)
        self.cfg_showline = getConfigListEntry(_('Separator line in the channel list'), self.ECS.showline)
        self.cfg_colshowline = getConfigListEntry(_('Color for separator line'), self.ECS.colshowline)
        self.cfg_listmode = getConfigListEntry(_('Doubleline channellist'), self.ECS.listmode)
        self.cfg_nummode = getConfigListEntry(_('Show channel number'), self.ECS.nummode)
        self.cfg_doubmode = getConfigListEntry(_('Long progressbar'), self.ECS.doubmode)
        self.cfg_bordermode = getConfigListEntry(_('Long bar with border'), self.ECS.bordermode)
        self.cfg_barpercmode = getConfigListEntry(_('Bar and percent together'), self.ECS.barpercmode)
        self.cfg_progress = getConfigListEntry(_('Progressbar location'), self.ECS.progress)
        self.cfg_percpos = getConfigListEntry(_('Percent location'), self.ECS.percpos)
        self.cfg_remmode = getConfigListEntry(_('Remaining time type'), self.ECS.remmode)
        self.cfg_endmode = getConfigListEntry(_('Start-end time enabled'), self.ECS.endmode)
        self.cfg_barmode = getConfigListEntry(_('ProgressBar Type'), self.ECS.barmode)
        self.cfg_colbar = getConfigListEntry(_('Color for Bar'), self.ECS.colbar)
        self.cfg_colbarsel = getConfigListEntry(_('Color for selected Bar'), self.ECS.colbarsel)
        self.cfg_picbar = getConfigListEntry(_('Pixmap for Bar'), self.ECS.picbar)
        self.cfg_colbordersel = getConfigListEntry(_('Color for selected BarBorder'), self.ECS.colbordersel)
        self.cfg_colborder = getConfigListEntry(_('Color for BarBorder'), self.ECS.colborder)
        self.cfg_colsat = getConfigListEntry(_('Color for Satlist'), self.ECS.colsat)
        self.cfg_colselsat = getConfigListEntry(_('Color for selected Satlist'), self.ECS.colselsat)
        self.cfg_percshow = getConfigListEntry(_('Show percent'), self.ECS.percshow)
        self.cfg_percmode = getConfigListEntry(_('Percent Type'), self.ECS.percmode)
        self.cfg_recordmode = getConfigListEntry(_('Record indicator location'), self.ECS.recordmode)
        self.cfg_iconmode = getConfigListEntry(_('Service icon location'), self.ECS.iconmode)
        self.cfg_crypticonmode = getConfigListEntry(_('Crypt icon location'), self.ECS.crypticonmode)
        self.cfg_picicocrypt = getConfigListEntry(_('Pixmap for crypt icon'), self.ECS.picicocrypt)
        self.cfg_eventmode = getConfigListEntry(_('Eventview type'), self.ECS.eventmode)
        self.cfg_piconmode = getConfigListEntry(_('Show picon'), self.ECS.piconmode)
        self.cfg_picomode = getConfigListEntry(_('Picon location'), self.ECS.picomode)
        self.cfg_colormode = getConfigListEntry(_('Colors of elements from a skin'), self.ECS.colormode)
        self.cfg_fontnum = getConfigListEntry(_('Font-size Number'), self.ECS.fontnum)
        self.cfg_fontperc = getConfigListEntry(_('Font-size Percent'), self.ECS.fontperc)
        self.cfg_fontname = getConfigListEntry(_('Font-size Service Name'), self.ECS.fontname)
        self.cfg_fontevent = getConfigListEntry(_('Font-size Event'), self.ECS.fontevent)
        self.cfg_fontend = getConfigListEntry(_('Font-size Start-End'), self.ECS.fontend)
        self.cfg_fontrem = getConfigListEntry(_('Font-size Remain'), self.ECS.fontrem)
        self.cfg_fonttxt = getConfigListEntry(_('Font-size Text'), self.ECS.fonttxt)
        self.cfg_fontsat = getConfigListEntry(_('Font-size Sat & Prov'), self.ECS.fontsat)
        self.cfg_timericonmode = getConfigListEntry(_('Waiting timers icon location'), self.ECS.timericonmode)
        self.cfg_colnum = getConfigListEntry(_('Color for number'), self.ECS.colnum)
        self.cfg_colselnum = getConfigListEntry(_('Color for number when selected'), self.ECS.colselnum)
        self.cfg_colname = getConfigListEntry(_('Color for Service Name'), self.ECS.colname)
        self.cfg_colnamesel = getConfigListEntry(_('Color for Service Name when selected'), self.ECS.colnamesel)
        self.cfg_colperc = getConfigListEntry(_('Color for percent'), self.ECS.colperc)
        self.cfg_colpercsel = getConfigListEntry(_('Color for percent when selected'), self.ECS.colpercsel)
        self.cfg_colevent = getConfigListEntry(_('Color for event'), self.ECS.colevent)
        self.cfg_coleventsel = getConfigListEntry(_('Color for event when selected'), self.ECS.coleventsel)
        self.cfg_colend = getConfigListEntry(_('Start-end Color'), self.ECS.colend)
        self.cfg_colselend = getConfigListEntry(_('Start-end Color when selected'), self.ECS.colselend)
        self.cfg_colremain = getConfigListEntry(_('Color for remaining time'), self.ECS.colremain)
        self.cfg_colselremain = getConfigListEntry(_('Color for remaining time when selected'), self.ECS.colselremain)
        self.cfg_channsum = getConfigListEntry(_('Show the number of channels in the satellite list'), self.ECS.channsum)
        self.cfg_showsky = getConfigListEntry(_('Show the Sky subservices in the satellite list'), self.ECS.showsky)
        self.cfg_showcurr = getConfigListEntry(_('Show the current transponder in the satellite list'), self.ECS.showcurr)
        self.cfg_showprov = getConfigListEntry(_('Show the provider in the satellite list'), self.ECS.showprov)
        self.cfg_shownew = getConfigListEntry(_('Show the new channels in the satellite list'), self.ECS.shownew)
        self.cfg_showhd = getConfigListEntry(_('Show the hd channels in the satellite list'), self.ECS.showhd)
        self.cfg_piconpathmode = getConfigListEntry(_('Folder for picons'), self.ECS.piconpathmode)
        return

    def createSetup(self):
        list = [self.cfg_enabled]
        if self.ECS.enabled.value:
            list.append(self.cfg_nummode)
            list.append(self.cfg_piconmode)
            if self.ECS.piconmode.value:
                list.append(self.cfg_picomode)
            list.append(self.cfg_listmode)
            list.append(self.cfg_progress)
            if not self.ECS.listmode.value:
                list.append(self.cfg_barpercmode)
            list.append(self.cfg_barmode)
            if self.ECS.barmode.value == '2':
                list.append(self.cfg_picbar)
            list.append(self.cfg_percshow)
            if self.ECS.percshow.value:
                list.append(self.cfg_percmode)
                list.append(self.cfg_percpos)
            list.append(self.cfg_linemode)
            list.append(self.cfg_showline)
            if self.ECS.listmode.value:
                list.append(self.cfg_bigpicomode)
                list.append(self.cfg_doubmode)
                list.append(self.cfg_remmode)
                list.append(self.cfg_endmode)
                if self.ECS.doubmode.value:
                    list.append(self.cfg_bordermode)
            list.append(self.cfg_iconmode)
            list.append(self.cfg_crypticonmode)
            list.append(self.cfg_picicocrypt)
            list.append(self.cfg_recordmode)
            list.append(self.cfg_timericonmode)
            list.append(self.cfg_eventmode)
            list.append(self.cfg_text)
            if self.ECS.text.value:
                list.append(self.cfg_coltext)
            if self.ECS.showline.value:
                list.append(self.cfg_colshowline)
            elif self.ECS.barmode.value == '2':
                list.append(self.cfg_colbordersel)
            list.append(self.cfg_colborder)
            if self.ECS.barmode.value == '1':
                list.append(self.cfg_colbar)
                list.append(self.cfg_colbarsel)
            list.append(self.cfg_colormode)
            if not self.ECS.colormode.value:
                list.append(self.cfg_colnum)
                list.append(self.cfg_colselnum)
                list.append(self.cfg_colname)
                list.append(self.cfg_colnamesel)
                list.append(self.cfg_colperc)
                list.append(self.cfg_colpercsel)
                list.append(self.cfg_colevent)
                list.append(self.cfg_coleventsel)
                if self.ECS.listmode.value:
                    list.append(self.cfg_colend)
                    list.append(self.cfg_colselend)
                    list.append(self.cfg_colremain)
                    list.append(self.cfg_colselremain)
            list.append(self.cfg_colsat)
            list.append(self.cfg_colselsat)
            list.append(self.cfg_fontnum)
            list.append(self.cfg_fontperc)
            list.append(self.cfg_fontname)
            list.append(self.cfg_fontevent)
            if self.ECS.listmode.value:
                list.append(self.cfg_fontend)
                list.append(self.cfg_fontrem)
            if self.ECS.text.value:
                list.append(self.cfg_fonttxt)
            list.append(self.cfg_fontsat)
            list.append(self.cfg_channsum)
            list.append(self.cfg_showhd)
            list.append(self.cfg_showsky)
            list.append(self.cfg_showcurr)
            list.append(self.cfg_showprov)
            list.append(self.cfg_shownew)
            list.append(self.cfg_piconpathmode)
        self['config'].list = list
        self['config'].l.setList(list)
        return

    def keyLeft(self):
        ConfigListScreen.keyLeft(self)
        self.newConfig()
        self.testScreen()
        return

    def keyRight(self):
        ConfigListScreen.keyRight(self)
        self.newConfig()
        self.testScreen()
        return

    def newConfig(self):
        cur = self['config'].getCurrent()
        if cur in (self.cfg_enabled,
         self.cfg_showline,
         self.cfg_percshow,
         self.cfg_text,
         self.cfg_barmode,
         self.cfg_colormode,
         self.cfg_piconmode,
         self.cfg_listmode,
         self.cfg_doubmode,
         self.cfg_barpercmode):
            self.createSetup()
        return

    def cancel(self):

        def setPrevValues(section, values):
            for key, val in list(section.content.items.items()):
                value = values.get(key, None)
                if value is not None:
                    if isinstance(val, ConfigSubsection):
                        setPrevValues(val, value)
                    else:
                        val.value = value

            return

        setPrevValues(self.ECS, self.prev_values)
        if self['config'].isChanged():
            self.session.openWithCallback(self.exitConfirmed, MessageBox, _('Really close without saving settings?'), MessageBox.TYPE_YESNO, timeout=8)
        else:
            self.close()
        return

    def exitConfirmed(self, answer):
        if answer:
            self.ECS.save()
            if fileExists(RPATH + 'linemode'):
                system('rm -rf ' + RPATH + 'linemode')
            if fileExists(RPATH + 'listmode'):
                system('rm -rf ' + RPATH + 'listmode')
            if fileExists(RPATH + 'enabled'):
                system('rm -rf ' + RPATH + 'enabled')
            if fileExists(RPATH + 'doubmode'):
                system('rm -rf ' + RPATH + 'doubmode')
            if fileExists(RPATH + 'piconpathmodeq'):
                system('rm -rf ' + RPATH + 'piconpathmodeq')
            if fileExists(RPATH + 'piconpathmodew'):
                system('rm -rf ' + RPATH + 'piconpathmodew')
            if fileExists(RPATH + 'piconpathmodee'):
                system('rm -rf ' + RPATH + 'piconpathmodee')
            if fileExists(RPATH + 'piconpathmoder'):
                system('rm -rf ' + RPATH + 'piconpathmoder')
            if fileExists(RPATH + 'piconpathmodet'):
                system('rm -rf ' + RPATH + 'piconpathmodet')
            if fileExists(RPATH + 'piconpathmodey'):
                system('rm -rf ' + RPATH + 'piconpathmodey')
            if fileExists(RPATH + 'piconpathmodeu'):
                system('rm -rf ' + RPATH + 'piconpathmodeu')
            if fileExists(RPATH + 'piconpathmodei'):
                system('rm -rf ' + RPATH + 'piconpathmodei')
            if fileExists(RPATH + 'piconpathmodeo'):
                system('rm -rf ' + RPATH + 'piconpathmodeo')
            self.close()
        return

    def save(self):
        for i in self['config'].list:
            i[1].save()

        configfile.save()
        if not alreadyPatch():
            mapreplace = True
            try:
                if fileExists(MAPPATH + 'keymap-ori.xml'):
                    if os.path.getsize(MAPPATH + 'keymap.xml') != os.path.getsize(MAPPATH + 'keymap-ori.xml'):
                        system('rm -rf ' + MAPPATH + 'keymap-ori.xml')
                        system('cp -f ' + MAPPATH + 'keymap.xml ' + MAPPATH + 'keymap-ori.xml')
                        mapreplace = False
                else:
                    system('cp -f ' + MAPPATH + 'keymap.xml ' + MAPPATH + 'keymap-ori.xml')
                    mapreplace = False
            except:
                pass

            r = open(MAP_FILE, 'r')
            rewrite = False
            newLines = ''
            for line in r.readlines():
                if rewrite and line.__contains__('</map>'):
                    line = line.replace('</map>', '\t<key id="KEY_UP" mapto="ServiceUp" flags="m" />\n\t\t<key id="KEY_DOWN" mapto="ServiceDown" flags="m" />\n\t</map>')
                    rewrite = False
                if line.__contains__('<map context="ChannelSelectBaseActions">'):
                    rewrite = True
                newLines = newLines + line

            r.close()
            r = open(MAP_FILE, 'w')
            r.write(newLines)
            r.close()
        linemode = True if fileExists(RPATH + 'linemode') else False
        listmode = True if fileExists(RPATH + 'listmode') else False
        enabled = True if fileExists(RPATH + 'enabled') else False
        doubmode = True if fileExists(RPATH + 'doubmode') else False
        piconpathmodeq = True if fileExists(RPATH + 'piconpathmodeq') else False
        piconpathmodew = True if fileExists(RPATH + 'piconpathmodew') else False
        piconpathmodee = True if fileExists(RPATH + 'piconpathmodee') else False
        piconpathmoder = True if fileExists(RPATH + 'piconpathmoder') else False
        piconpathmodet = True if fileExists(RPATH + 'piconpathmodet') else False
        piconpathmodey = True if fileExists(RPATH + 'piconpathmodey') else False
        piconpathmodeu = True if fileExists(RPATH + 'piconpathmodeu') else False
        piconpathmodei = True if fileExists(RPATH + 'piconpathmodei') else False
        piconpathmodeo = True if fileExists(RPATH + 'piconpathmodeo') else False
        if not config.plugins.ExtraChannelSelection.enabled.value and enabled or config.plugins.ExtraChannelSelection.enabled.value and not enabled or not config.plugins.ExtraChannelSelection.doubmode.value and doubmode or config.plugins.ExtraChannelSelection.doubmode.value and not doubmode or config.plugins.ExtraChannelSelection.linemode.value == '2' and linemode or config.plugins.ExtraChannelSelection.linemode.value == '1' and not linemode or not config.plugins.ExtraChannelSelection.listmode.value and listmode or config.plugins.ExtraChannelSelection.listmode.value and not listmode or config.plugins.ExtraChannelSelection.piconpathmode.value == '0' and not piconpathmodeq or config.plugins.ExtraChannelSelection.piconpathmode.value == '1' and not piconpathmodew or config.plugins.ExtraChannelSelection.piconpathmode.value == '2' and not piconpathmodee or config.plugins.ExtraChannelSelection.piconpathmode.value == '3' and not piconpathmoder or config.plugins.ExtraChannelSelection.piconpathmode.value == '4' and not piconpathmodet or config.plugins.ExtraChannelSelection.piconpathmode.value == '5' and not piconpathmodey or config.plugins.ExtraChannelSelection.piconpathmode.value == '6' and not piconpathmodeu or config.plugins.ExtraChannelSelection.piconpathmode.value == '7' and not piconpathmodei or config.plugins.ExtraChannelSelection.piconpathmode.value == '8' and not piconpathmodeo:
            self.session.openWithCallback(self.restart, MessageBox, _('GUI needs a restart to apply a new settings\nDo you want to Restart the GUI now?'), MessageBox.TYPE_YESNO, timeout=8)
        elif fileExists(RPATH + 'linemode'):
            system('rm -rf ' + RPATH + 'linemode')
        if fileExists(RPATH + 'listmode'):
            system('rm -rf ' + RPATH + 'listmode')
        if fileExists(RPATH + 'enabled'):
            system('rm -rf ' + RPATH + 'enabled')
        if fileExists(RPATH + 'doubmode'):
            system('rm -rf ' + RPATH + 'doubmode')
        if fileExists(RPATH + 'piconpathmodeq'):
            system('rm -rf ' + RPATH + 'piconpathmodeq')
        if fileExists(RPATH + 'piconpathmodew'):
            system('rm -rf ' + RPATH + 'piconpathmodew')
        if fileExists(RPATH + 'piconpathmodee'):
            system('rm -rf ' + RPATH + 'piconpathmodee')
        if fileExists(RPATH + 'piconpathmoder'):
            system('rm -rf ' + RPATH + 'piconpathmoder')
        if fileExists(RPATH + 'piconpathmodet'):
            system('rm -rf ' + RPATH + 'piconpathmodet')
        if fileExists(RPATH + 'piconpathmodey'):
            system('rm -rf ' + RPATH + 'piconpathmodey')
        if fileExists(RPATH + 'piconpathmodeu'):
            system('rm -rf ' + RPATH + 'piconpathmodeu')
        if fileExists(RPATH + 'piconpathmodei'):
            system('rm -rf ' + RPATH + 'piconpathmodei')
        if fileExists(RPATH + 'piconpathmodeo'):
            system('rm -rf ' + RPATH + 'piconpathmodeo')
        self.close()
        return

    def info(self):
        self.session.open(PluginHistory)
        return

    def back(self):
        self.session.open(BackScreen)
        return

    def restart(self, answer):
        if answer is True:
            if fileExists(RPATH + 'linemode'):
                system('rm -rf ' + RPATH + 'linemode')
            if fileExists(RPATH + 'listmode'):
                system('rm -rf ' + RPATH + 'listmode')
            if fileExists(RPATH + 'enabled'):
                system('rm -rf ' + RPATH + 'enabled')
            if fileExists(RPATH + 'doubmode'):
                system('rm -rf ' + RPATH + 'doubmode')
            if fileExists(RPATH + 'piconpathmodeq'):
                system('rm -rf ' + RPATH + 'piconpathmodeq')
            if fileExists(RPATH + 'piconpathmodew'):
                system('rm -rf ' + RPATH + 'piconpathmodew')
            if fileExists(RPATH + 'piconpathmodee'):
                system('rm -rf ' + RPATH + 'piconpathmodee')
            if fileExists(RPATH + 'piconpathmoder'):
                system('rm -rf ' + RPATH + 'piconpathmoder')
            if fileExists(RPATH + 'piconpathmodet'):
                system('rm -rf ' + RPATH + 'piconpathmodet')
            if fileExists(RPATH + 'piconpathmodey'):
                system('rm -rf ' + RPATH + 'piconpathmodey')
            if fileExists(RPATH + 'piconpathmodeu'):
                system('rm -rf ' + RPATH + 'piconpathmodeu')
            if fileExists(RPATH + 'piconpathmodei'):
                system('rm -rf ' + RPATH + 'piconpathmodei')
            if fileExists(RPATH + 'piconpathmodeo'):
                system('rm -rf ' + RPATH + 'piconpathmodeo')
            self.session.open(TryQuitMainloop, 3)
        return


def main(session, **kwargs):
    if not allow:
        session.open(MessageBox, _("You can't use this plugin. Your system files out of date (very old or very new).\nApparently a regular update changed them, or you have older image OpenATV, or you (or any plugin) manually changed them.\nTo protect your image from instability ExtraChannelSelection plugin disabled himself.\nFor the solution this problem, contact the author of the plugin on the https://akauchkun.blogspot.com/"), MessageBox.TYPE_INFO, timeout=35)
    else:
        session.open(ExtraChannelSelection)
    return


def Plugins(path, **kwargs):
    list = [PluginDescriptor(name=_('ExtraChannelSelection'), description=_('Settings of service list on channel selection'), where=[PluginDescriptor.WHERE_PLUGINMENU, PluginDescriptor.WHERE_EXTENSIONSMENU], icon='ecs.png', fnc=main), PluginDescriptor(where=[PluginDescriptor.WHERE_SESSIONSTART], fnc=StartMainSession)]
    return list

