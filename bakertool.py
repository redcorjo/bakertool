import gui
import wx
import mylocale
import pickle

DEBUG="NO"

mylocale.mylocale()

class MyWindow(gui.MyFrame1):

    myfilename="breadrecipe.cfg"
    def __init__(self, parent):
        gui.MyFrame1.__init__(self, parent)
        icon1 = wx.Icon("./icons/bread16.png", wx.BITMAP_TYPE_ANY)
        self.SetIcon(icon1)
        self.flour_entry.Bind(wx.EVT_CHAR, self.handle_keypress)
        self.water_entry.Bind(wx.EVT_CHAR, self.handle_keypress)
        self.totalweight_entry.Bind(wx.EVT_CHAR, self.handle_keypress)
        self.percentage_entry.Bind(wx.EVT_CHAR, self.handle_keypress)
        self.yeast_option="dryyeast"
        self.m_radioBox_yeast_selection.SetSelection(1)
        self.display_message(_(u"Are you ready to make bread? :-)"))
        self.m_choice_profileChoices = [ _(u"default")]
        self.m_choice_profile.Clear()
        self.m_choice_profile.AppendItems(self.m_choice_profileChoices)
        self.m_choice_profile.SetSelection(0)

    def execute_breadformula( self, event ):
        if event == "load_config":
            self.flour_entry.SetValue(str(mybread.flour))
            self.water_entry.SetValue(str(mybread.water))
            self.totalweight_entry.SetValue(str(mybread.totalweight))
            self.percentage_entry.SetValue(str(mybread.percentage))
            self.sourdought_entry.SetValue(str(mybread.sourdought))
        else:
            mybread.reset()

            if self.flour_entry.GetValue() != "":
                mybread.flour=round(float(self.flour_entry.GetValue()),2)
            else:
                mybread.flour=0
            if self.water_entry.GetValue() != "":
                mybread.water=round(float(self.water_entry.GetValue()),2)
            else:
                mybread.water=0
            if self.totalweight_entry.GetValue() != "":
                mybread.totalweight=round(float(self.totalweight_entry.GetValue()),2)
            else:
                mybread.totalweight=0
            if self.percentage_entry.GetValue() != "":
                mybread.percentage=round(float(self.percentage_entry.GetValue()),2)
            else:
                mybread.percentage=0
            if self.sourdought_entry.GetValue() != "":
                mybread.sourdought=round(float(self.sourdought_entry.GetValue()),2)
            else:
                mybread.sourdought=0
            if self.m_textCtrl_profile.GetValue() != "":
                mybread.profile=unicode(self.m_textCtrl_profile.GetValue())
            else:
                mybread.profile=_(u"default")
        self.obtain_yeast_option()
        mybread.breadformula(self.yeast_option)
        self.flour_results.SetValue(str(int(mybread.flour)))
        self.water_results.SetValue(str(int(mybread.water)))
        self.totalweight_results.SetValue(str(int(mybread.totalweight)))
        self.percentage_results.SetValue(str(int(mybread.percentage))+"%")
        self.yeast_results.SetValue(str(int(mybread.yeast)))
        self.salt_results.SetValue(str(int(mybread.salt)))
        self.sourdought_results.SetValue(str(int(mybread.sourdought)))
        self.flour_results_percentage.SetValue(str(int(mybread.flour_percentage))+"%")
        self.water_results_percentage.SetValue(str(int(mybread.water_percentage))+"%")
        self.totalweight_results_percentage.SetValue(str(int(mybread.totalweight_percentage))+"%")
        self.salt_results_percentage.SetValue(str(float(mybread.saltpercentage))+"%")
        self.yeast_results_percentage.SetValue(str(float(mybread.yeastpercentage))+"%")
        self.sourdought_results_percentage.SetValue(str(int(mybread.sourdoughtpercentage))+"%")
        self.execute_profilename(event)

    def execute_cleanup( self, event ):
        self.display_message(_(u"executed cleanup"))
        mybread.reset()
        self.flour_entry.SetValue("")
        self.water_entry.SetValue("")
        self.totalweight_entry.SetValue("")
        self.percentage_entry.SetValue("")
        self.sourdought_entry.SetValue("")
        self.flour_results.SetValue("")
        self.water_results.SetValue("")
        self.totalweight_results.SetValue("")
        self.percentage_results.SetValue("")
        self.yeast_results.SetValue("")
        self.salt_results.SetValue("")
        self.sourdought_results.SetValue("")
        self.flour_results_percentage.SetValue("")
        self.water_results_percentage.SetValue("")
        self.totalweight_results_percentage.SetValue("")
        self.salt_results_percentage.SetValue("")
        self.yeast_results_percentage.SetValue("")
        self.sourdought_results_percentage.SetValue("")

    def execute_cleanup_results( self):
        self.display_message(_(u"executed cleanup results"))
        mybread.reset()
        self.flour_results.SetValue("")
        self.water_results.SetValue("")
        self.totalweight_results.SetValue("")
        self.percentage_results.SetValue("")
        self.yeast_results.SetValue("")
        self.salt_results.SetValue("")
        self.sourdought_results.SetValue("")
        self.flour_results_percentage.SetValue("")
        self.water_results_percentage.SetValue("")
        self.totalweight_results_percentage.SetValue("")
        self.salt_results_percentage.SetValue("")
        self.yeast_results_percentage.SetValue("")
        self.sourdought_results_percentage.SetValue("")

    def handle_keypress(self, event):
        keycode = event.GetKeyCode()
        if chr(keycode).isdigit() or keycode == 8 :
            event.Skip()
        elif keycode == 9 or keycode == 13 :
            debug_print ("tab or intro")
            event.EventObject.Navigate()
            event.Skip()
        else:
            debug_print ("other char " + str(keycode))

    def execute_yeast_selection( self, event ):
        self.obtain_yeast_option()
        myevent = event.GetEventObject()
        if self.yeast_option == "sourdought":
            self.m_staticText_sourdought_input.Show()
            self.m_staticText_sourdought_output.Show()
            self.sourdought_entry.Show()
            self.sourdought_results.Show()
            self.sourdought_results_percentage.Show()
            mybread.yeastpercentage=0
            mybread.yeast=0
            self.display_message(_(u"activated selection: sourdought only"))
        elif self.yeast_option == "dryyeast":
            self.m_staticText_sourdought_input.Hide()
            self.m_staticText_sourdought_output.Hide()
            self.sourdought_entry.Hide()
            self.sourdought_results.Hide()
            self.sourdought_results_percentage.Hide()
            self.sourdought_entry.SetValue("")
            mybread.yeastpercentage=0.5
            self.display_message(_(u"activated selection: dry yeast only"))
        elif self.yeast_option == "freshyeast":
            self.m_staticText_sourdought_input.Hide()
            self.m_staticText_sourdought_output.Hide()
            self.sourdought_entry.Hide()
            self.sourdought_results.Hide()
            self.sourdought_results_percentage.Hide()
            self.sourdought_entry.SetValue("")
            mybread.yeastpercentage=1
            self.display_message(_(u"activated selection: fresh yeast only"))
        elif self.yeast_option == "sourdought_and_dryyeast":
            self.m_staticText_sourdought_input.Show()
            self.m_staticText_sourdought_output.Show()
            self.sourdought_entry.Show()
            self.sourdought_results.Show()
            self.sourdought_results_percentage.Show()
            mybread.yeastpercentage=0.5
            self.display_message(_(u"activated selection: sourdought and dry yeast combined"))
        elif self.yeast_option == "sourdought_and_freshyeast":
            self.m_staticText_sourdought_input.Show()
            self.m_staticText_sourdought_output.Show()
            self.sourdought_entry.Show()
            self.sourdought_results.Show()
            self.sourdought_results_percentage.Show()
            mybread.yeastpercentage=1
            self.display_message(_(u"activated selection: sourdought and fresh yeast combined"))
        else:
            self.m_staticText_sourdought_input.Show()
            self.m_staticText_sourdought_output.Show()
            self.sourdought_entry.Show()
            self.sourdought_results.Show()
            self.sourdought_results_percentage.Show()
            mybread.yeastpercentage=1

    def execute_wizard(self,event):
        debug_print("execute wizard")
        if self.yeast_option == "dryyeast" or self.yeast_option == "freshyeast":
                dialog=MyDialog_without_sourdought(None)
        else:
            dialog=MyDialog_with_sourdought(None)
        dialog.SetTitle(_(u"Bread maker percentage selection"))
        if dialog.ShowModal() == wx.ID_OK:
            debug_print ("show totalweight=%d percentage=%d%%" % (mybread.totalweight,mybread.percentage))
        self.display_message(_(u"Percentage build based in chosen values"))
        self.totalweight_entry.SetValue(str(int(mybread.totalweight)))
        self.percentage_entry.SetValue(str(int(mybread.percentage)))
        self.obtain_yeast_option()
        if self.yeast_option == "sourdought":
            debug_print ("sourdought only")
            mybread.breadformula("sourdought")
            self.sourdought_entry.SetValue(str(int(mybread.sourdought)))
        elif self.yeast_option == "dryyeast":
            debug_print ("dry yeast only")
            mybread.breadformula("yeast")
        elif self.yeast_option == "freshyeast":
            debug_print ("fresh yeast only")
            mybread.breadformula("yeast")
        elif self.yeast_option == "sourdought_and_dryyeast":
            debug_print ("sourdought and dry yeast")
            mybread.breadformula("sourdought_and_yeast")
            self.sourdought_entry.SetValue(str(int(mybread.sourdought)))
        elif self.yeast_option == "sourdought_and_freshyeast":
            debug_print ("sourdought and fresh yeast")
            mybread.breadformula("sourdought_and_yeast")
            self.sourdought_entry.SetValue(str(int(mybread.sourdought)))
        self.execute_breadformula(self)

    def obtain_yeast_option(self):
        if self.m_radioBox_yeast_selection.GetSelection() == 0:
            self.yeast_option="sourdought"
        elif self.m_radioBox_yeast_selection.GetSelection() == 1:
            self.yeast_option="dryyeast"
        elif self.m_radioBox_yeast_selection.GetSelection() == 2:
            self.yeast_option="freshyeast"
        elif self.m_radioBox_yeast_selection.GetSelection() == 3:
            self.yeast_option="sourdought_and_dryyeast"
        elif self.m_radioBox_yeast_selection.GetSelection() == 4:
            self.yeast_option="sourdought_and_freshyeast"
        if self.yeast_option == "dryyeast" or self.yeast_option == "freshyeast":
            self.yeastoption="yeast"
        elif self.yeast_option == "sourdought":
            self.yeastoption="sourdought"
        else:
            self.yeastoption="sourdought_and_yeast"
        mybread.yeast_option=self.yeast_option

    def display_message(self, mystring):
        self.m_textCtrl_display_message.SetValue(mystring)
        font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True)
        self.m_textCtrl_display_message.SetFont(font)

    def execute_about( self, event ):
        debug_print("executed_about")

        description = _("""Bread Maker tool is the perfect calculator to
assist all Baker's percentage calculations providing different
combinations to build your Baker recipes.
""")

        licence = _("""Bread Maker tool is free software; you can redistribute
it and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation; either version 2 of the License,
or (at your option) any later version.

Bread Maker tool may come with bugs. This is the fun of freeware :-).

""")
        info = wx.AboutDialogInfo()
        info.SetIcon(wx.Icon('./icons/bread128.png', wx.BITMAP_TYPE_ANY))
        info.SetName('Bread Maker tool')
        info.SetVersion('0.6')
        info.SetDescription(description)
        info.SetCopyright('(C) 2015 - 2016 Jordi Redondo')
        info.SetWebSite('https://github.com/redcorjo/bakertool.git')
        wx.AboutBox(info)

    def execute_help( self, event ):
        debug_print("executed_help")
        description = _("""For more details about the baker percentage refer to Wikipedia site at:

https://en.wikipedia.org/wiki/Baker_percentage
""")
        myhelp = wx.MessageDialog(self, description, "Help", wx.OK)
        result = myhelp.ShowModal() == wx.ID_YES
        myhelp.Destroy()

    def execute_open( self, event ):
        debug_print("execute_open")
        openFileDialog = wx.FileDialog(self, "Open " + self.myfilename + " file", "", "",
                                       "cfg files (*.cfg)|*.cfg", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        openFileDialog.SetFilename(self.myfilename)

        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return
        else:
            with open(openFileDialog.GetPath(),'rb') as mydescriptor:
                mybread.myprofiledict=pickle.load(mydescriptor)
            debug_print(str(mybread.myprofiledict))
            mybread.unpackage_from_dictionary()
            self.m_choice_profileChoices=mybread.myprofiledict.keys()
            self.m_choice_profileChoices.remove("default")
            self.m_choice_profileChoices.insert(0,"default")
            self.m_choice_profile.Clear()
            self.m_choice_profile.AppendItems(self.m_choice_profileChoices)
            self.m_choice_profile.SetSelection(0)

            self.execute_breadformula("load_config")

    def execute_save( self, event ):
        debug_print("execute_save")
        with open(self.myfilename,'wb') as mydescriptor:
            pickle.dump(mybread.myprofiledict,mydescriptor)
        debug_print(str(mybread.myprofiledict))

    def execute_save_as( self, event ):
        debug_print("execute_save_as")
        saveFileDialog = wx.FileDialog(self, "Save " + self.myfilename + " file", "", "",
                                   "cfg files (*.cfg)|*.cfg", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

        saveFileDialog.SetFilename(self.myfilename)
        if saveFileDialog.ShowModal() == wx.ID_CANCEL:
            return
        else:
            with open(saveFileDialog.GetPath(),'wb') as mydescriptor:
                pickle.dump(mybread.myprofiledict,mydescriptor)
            debug_print(str(mybread.myprofiledict))

    def close_my_app(self, event):
        exit()

    def execute_profilename( self, event ):
        debug_print("execute_profilename")
        if self.m_textCtrl_profile.GetValue() != "":
            mybread.profile=unicode(self.m_textCtrl_profile.GetValue())
        else:
            mybread.profile=_(u"default")
        if mybread.profile not in self.m_choice_profileChoices:
            self.m_choice_profileChoices.append(mybread.profile)
            self.m_choice_profile.Clear()
            self.m_choice_profile.AppendItems(self.m_choice_profileChoices)
            self.m_choice_profile.SetSelection(len(self.m_choice_profileChoices)-1)
        mybread.package_to_dictionary()

    def execute_onchoice_profile( self, event ):
        choice=self.m_choice_profile.GetStringSelection()
        self.m_textCtrl_profile.SetValue(choice)
        mybread.unpackage_from_dictionary(choice)
        self.yeast_option=mybread.yeast_option
        if self.yeast_option == "sourdought":
            self.m_radioBox_yeast_selection.SetSelection(0)
        if self.yeast_option == "dryyeast":
            self.m_radioBox_yeast_selection.SetSelection(1)
        if self.yeast_option == "freshyeast":
            self.m_radioBox_yeast_selection.SetSelection(2)
        if self.yeast_option == "sourdought_and_dryyeast":
            self.m_radioBox_yeast_selection.SetSelection(3)
        if self.yeast_option == "sourdought_and_freshyeast":
            self.m_radioBox_yeast_selection.SetSelection(4)
        self.execute_yeast_selection(event)
        self.execute_breadformula("load_config")

class MyDialog_with_sourdought(gui.MyDialog_select_percentage_with_sourdought):

    def __init__(self, parent):
        gui.MyDialog_select_percentage_with_sourdought.__init__(self, parent)
        self.totalweight_entry.Bind(wx.EVT_CHAR, self.handle_keypress)

    def handle_keypress(self, event):
        keycode = event.GetKeyCode()
        if chr(keycode).isdigit() or keycode == 8 :
            event.Skip()
        elif keycode == 9 or keycode == 13 :
            debug_print ("tab or intro")
            event.EventObject.Navigate()
            event.Skip()
        else:
            debug_print ("other char " + str(keycode))

    def execute_percentage_formula( self, event ):
        debug_print("execute percentage")
        if self.totalweight_entry.GetValue() != "":
            mybread.totalweight=int(self.totalweight_entry.GetValue())
        else:
            mybread.totalweight=0
        if self.m_slider_percentage.GetValue() != "":
            mybread.percentage=int(self.m_slider_percentage.GetValue())
        else:
            mybread.percentage=0
        if self.m_slider_percentage_sourdought.GetValue() != "":
            mybread.sourdoughtpercentage=int(self.m_slider_percentage_sourdought.GetValue())
        else:
            mybread.sourdoughtpercentage=0
        if mybread.totalweight > 0:
            mybread.breadformula_totalweight_percentage_sourdoughtpercentage(window.yeast_option)
        debug_print ("totalweight=%d percentage=%d%%" % (mybread.totalweight,mybread.percentage))
        self.Close()

class MyDialog_without_sourdought(gui.MyDialog_select_percentage_without_sourdought):

    def __init__(self, parent):
        gui.MyDialog_select_percentage_without_sourdought.__init__(self, parent)
        self.totalweight_entry.Bind(wx.EVT_CHAR, self.handle_keypress)

    def handle_keypress(self, event):
        keycode = event.GetKeyCode()
        if chr(keycode).isdigit() or keycode == 8 :
            event.Skip()
        elif keycode == 9 or keycode == 13 :
            debug_print ("tab or intro")
            event.EventObject.Navigate()
            event.Skip()
        else:
            debug_print ("other char " + str(keycode))

    def execute_percentage_formula( self, event ):
        mybread.sourdought=0
        if self.totalweight_entry.GetValue() != "":
            mybread.totalweight=int(self.totalweight_entry.GetValue())
            #window.totalweight_entry=totalweight_entry.GetValue()
        else:
            mybread.totalweight=0
            #window.totalweight_entry=0
        if self.m_slider_percentage.GetValue() != "":
            mybread.percentage=int(self.m_slider_percentage.GetValue())
            #window.percentage_entry=self.m_slider_percentage.GetValue()
            mybread.breadformula_totalweight_percentage_sourdoughtpercentage(window.yeast_option)
        else:
            mybread.percentage=0
            #window.percentage_entry=0
        #print "totalweight=%d percentage=%d%%" % (mybread.totalweight,mybread.percentage)
        self.Close()

class Breadmaker():
    flour=0
    water=0
    totalweight=0
    percentage=0
    yeast=0
    salt=0
    sourdought=0
    sourdought_water=0
    sourdought_flour=0
    flour_percentage=0
    water_percentage=0
    totalweight_percentage=0
    yeastpercentage=0
    saltpercentage=0
    sourdoughtpercentage=0
    yeast_option="dryyeast"

    def __init__(self):
        self.myprofiledict={}
        self.profile="default"
        self.flour=0
        self.water=0
        self.totalweight=0
        self.percentage=0
        self.sourdought=0
        self.sourdought_water=0
        self.sourdought_flour=0
        self.yeast=0
        self.salt=0
        self.flour_percentage=0
        self.water_percentage=0
        self.totalweight_percentage=0
        self.sourdoughtpercentage=0
        self.yeast_option="dryyeast"
        self.yeastpercentage=0
        self.saltpercentage=0
        self.package_to_dictionary()


    def reset(self):
        self.flour=0
        self.water=0
        self.totalweight=0
        self.yeast=0
        self.salt=0
        self.percentage=0
        self.sourdought=0
        self.sourdought_water=0
        self.sourdought_flour=0
        self.flour_percentage=0
        self.water_percentage=0
        self.totalweight_percentage=0
        self.sourdoughtpercentage=0
        self.yeastpercentage=0
        self.saltpercentage=0

    def package_to_dictionary(self):
        myvariables=dir(self)
        self.mydictionary={}
        for myitem in myvariables:
            myvalue=getattr(self,myitem)
            if isinstance(myvalue,int) or isinstance(myvalue,str) or isinstance(myvalue,float) \
                    or isinstance(myvalue,unicode):
                if not myitem.startswith("__"):
                    self.mydictionary[myitem]=myvalue
        self.myprofiledict[self.profile]=self.mydictionary


    def unpackage_from_dictionary(self,myprofile=u"default"):
        for myvariable,myvalue in self.myprofiledict[myprofile].iteritems():
            setattr(self,myvariable,myvalue)


    def salt_and_yeast_calculation(self):
        self.saltpercentage=2
        if self.yeast_option=="dryyeast" or self.yeast_option=="sourdought_and_dryyeast":
            self.yeastpercentage=1
        else:
            self.yeastpercentage=0.5
        if self.yeast_option=="dryyeast" or self.yeast_option=="freshyeast":
            self.yeast=(self.flour/100.00)*self.yeastpercentage
            self.salt=(self.flour/100.00)*self.saltpercentage
        else:
            self.yeast=((self.flour+self.sourdought)/100.00)*self.yeastpercentage
            self.salt=((self.flour+self.sourdought)/100.00)*self.saltpercentage

    def total_formula_percentage(self, yeastoption):
        self.init_sourdought(yeastoption)
        if self.flour > 0 or self.sourdought > 0:
            self.flour_percentage=(self.flour/(self.flour+self.sourdought_flour))*100.0
            self.water_percentage=(self.water/(self.flour+self.sourdought_water))*100.0
            self.sourdoughtpercentage=(self.sourdought/(self.flour+self.sourdought_flour))*100.0
            self.totalweight_percentage=self.flour_percentage+self.water_percentage+self.sourdoughtpercentage
            self.percentage=self.totalweight_percentage-100
        else:
            self.flour_percentage=0
            self.water_percentage=0
            self.sourdoughtpercentage=0
            self.totalweight_percentage=0
            self.percentage=0


    def init_sourdought(self,yeastoption):
        if yeastoption == "sourdought" or yeastoption == "sourdought_and_yeast":
            if self.sourdought > 0:
                self.sourdought_water=self.sourdought/2.0
                self.sourdought_flour=self.sourdought/2.0
        else:
            self.sourdought_water=0
            self.sourdought_flour=0
            self.sourdought=0

    def breadformula(self,yeast_option="none"):
        debug_print ("yeast option : " + yeast_option)
        if yeast_option == "dryyeast" or yeast_option == "freshyeast":
            yeastoption="yeast"
        elif yeast_option == "sourdought":
            yeastoption="sourdought"
        else:
            yeastoption="sourdought_and_yeast"
        if self.flour > 0 and self.water > 0 :
            self.breadformula_flour_water(yeastoption)
            self.total_formula_percentage(yeastoption)
        elif self.flour > 0 and self.percentage > 0 :
            self.breadformula_flour_percentage(yeastoption)
            self.total_formula_percentage(yeastoption)
        elif self.totalweight > 0 and self.percentage > 0 :
            self.breadformula_totalweight_percentage(yeastoption)
            self.total_formula_percentage(yeastoption)
        elif self.water > 0 and self.percentage > 0 :
            self.breadformula_water_percentage(yeastoption)
            self.total_formula_percentage(yeastoption)
        elif self.flour > 0 and self.water > 0 and self.totalweight > 0 :
            self.breadformula_flour_water_totalweight(yeastoption)
            self.total_formula_percentage(yeastoption)
        elif self.flour > 0 and self.water > 0 and self.sourdought > 0 :
            self.breadformula_flour_water_sourdought(yeastoption)
            self.total_formula_percentage(yeastoption)
        elif self.flour > 0 and self.totalweight > 0 and self.sourdought:
            self.breadformula_flour_totalweight_sourdought(yeastoption)
            self.total_formula_percentage(yeastoption)
        elif self.flour > 0 and self.totalweight > 0 :
            self.breadformula_flour_totalweight(yeastoption)
            self.total_formula_percentage(yeastoption)
        elif self.water > 0 and self.totalweight > 0 and self.sourdought > 0 :
            self.breadformula_water_totalweight_sourdought(yeastoption)
            self.total_formula_percentage(yeastoption)
        elif self.water > 0 and self.totalweight > 0 :
            self.breadformula_water_totalweight(yeastoption)
            self.total_formula_percentage(yeastoption)
        elif self.totalweight > 0 and self.percentage > 0 and self.sourdought > 0 :
            self.breadformula_totalweight_percentage_sourdought(yeastoption)
            self.total_formula_percentage(yeastoption)
        else:
            window.display_message (_(u"no enough ingredients to make a selection!"))
            mybread.reset()
            debug_print ("OTHER: water=%d flour=%d totalweight=%d percentage=%d%%" % (self.water,self.flour,
                                                                               self.totalweight,self.percentage))
        debug_print ("water=%d flour=%d totalweight=%d yeast=%d salt=%d percentage=%d%% yeastpercentage=%f%% " \
              "saltpercentage=%d%% sourdought=%d sourdought_flour=%d sourdought_water=%d sourdought_percentage=%d%%" % \
                  (self.water,self.flour,self.totalweight,self.yeast,self.salt,self.percentage,self.yeastpercentage,
                   self.saltpercentage,self.sourdought,self.sourdought_flour,self.sourdought_water,self.sourdoughtpercentage))
        self.package_to_dictionary()
        debug_print ("#####################################################")

    def breadformula_flour_totalweight(self,yeastoption):
        debug_print ("breadformula_flour_totalweight")
        self.init_sourdought(yeastoption)
        if yeastoption == "yeast":
            debug_print("with yeast only")
            self.water=self.totalweight-self.flour
            self.percentage=(self.water/float(self.flour))*100
            self.salt_and_yeast_calculation()
            window.display_message(_(u"executed formula using flour and totalweight"))
        else:
            debug_print("including sourdought")
            if self.water > 0:
                self.breadformula_flour_water_totalweight(yeastoption)
            elif self.sourdought > 0:
                self.breadformula_flour_totalweight_sourdought(yeastoption)
            elif self.percentage > 0:
                self.breadformula_flour_totalweight_percentage(yeastoption)
            else:
                window.display_message(_(u"no enough ingredients to make a selection with flour and totalweight!"))
                window.execute_cleanup_results()

    def breadformula_water_totalweight(self,yeastoption):
        debug_print ("breadformula_water_totalweight")
        self.init_sourdought(yeastoption)
        if yeastoption == "yeast":
            debug_print("with yeast only")
            self.flour=self.totalweight-self.water
            self.percentage=(self.water/float(self.flour))*100
            self.salt_and_yeast_calculation()
            window.display_message(_(u"executed formula using water and totalweight"))
        else:
            debug_print("including sourdought")
            if self.flour > 0:
                self.breadformula_flour_water_totalweight(yeastoption)
            elif self.sourdought > 0:
                self.breadformula_water_totalweight_sourdought(yeastoption)
            elif self.percentage > 0:
                self.breadformula_water_totalweight_percentage(yeastoption)
            else:
                window.display_message(_(u"no enough ingredients to make a selection with water and totalweight!"))
                window.execute_cleanup_results()

    def breadformula_totalweight_percentage(self,yeastoption):
        debug_print ("breadformula_totalweight_percentage")
        self.init_sourdought(yeastoption)
        if yeastoption == "yeast":
            debug_print("with yeast only")
            self.flour=self.totalweight/float((100+self.percentage)/100.00)
            self.water=self.totalweight-self.flour
            self.salt_and_yeast_calculation()
            window.display_message(_(u"executed formula using totalweight and percentage"))
        else:
            debug_print("including sourdought")
            if self.flour > 0:
                self.breadformula_flour_totalweight_percentage(yeastoption)
            elif self.sourdought > 0:
                self.breadformula_totalweight_percentage_sourdought(yeastoption)
            elif self.water > 0:
                self.breadformula_water_totalweight_percentage(yeastoption)
            else:
                window.display_message(_(u"no enough ingredients to make a selection with totalweight and percentage!"))
                window.execute_cleanup_results()

    def breadformula_flour_water(self,yeastoption):
        debug_print ("breadformula_flour_water")
        self.init_sourdought(yeastoption)
        if yeastoption == "yeast":
            debug_print("with yeast only")
            self.totalweight=self.flour+self.water
            self.percentage=((self.water)/(float(self.flour)))*100
            self.salt_and_yeast_calculation()
            window.display_message(_(u"executed formula using flour and water"))
        else:
            debug_print("including sourdought")
            if self.totalweight > 0:
                self.breadformula_flour_water_totalweight(yeastoption)
            elif self.percentage > 0:
                self.breadformula_flour_water_percentage(yeastoption)
            elif self.sourdought > 0:
                self.breadformula_flour_water_sourdought(yeastoption)
            else:
                window.display_message(_(u"no enough ingredients to make a selection with flour and water!"))
                window.execute_cleanup_results()

    def breadformula_flour_percentage(self,yeastoption):
        debug_print ("breadformula_flour_percentage")
        self.init_sourdought(yeastoption)
        if yeastoption == "yeast":
            debug_print("with yeast only")
            self.water=self.flour*self.percentage/100
            self.totalweight=self.flour+self.water
            self.salt_and_yeast_calculation()
            window.display_message(_(u"executed formula using flour and percentage"))
        else:
            debug_print("including sourdought")
            if self.water > 0:
                self.breadformula_flour_water_percentage(yeastoption)
            elif self.sourdought > 0:
                self.breadformula_flour_percentage_sourdought(yeastoption)
            elif self.totalweight > 0:
                self.breadformula_flour_totalweight_percentage(yeastoption)
            else:
                window.display_message(_(u"no enough ingredients to make a selection with flour and percentage!"))
                window.execute_cleanup_results()

    def breadformula_water_percentage(self,yeastoption):
        debug_print ("breadformula_water_percentage")
        self.init_sourdought(yeastoption)
        if yeastoption == "yeast":
            debug_print("with yeast only")
            self.flour=self.water*100/self.percentage
            self.totalweight=self.flour+self.water
            self.salt_and_yeast_calculation()
            window.display_message(_(u"executed formula using water and percentage"))
        else:
            debug_print("including sourdought")
            if self.flour > 0:
                self.breadformula_flour_water_percentage(yeastoption)
            elif self.sourdought > 0:
                self.breadformula_water_percentage_sourdought(yeastoption)
            elif self.totalweight > 0:
                self.breadformula_water_totalweight_percentage(yeastoption)
            else:
                window.display_message(_(u"no enough ingredients to make a selection with water and percentage!"))
                window.execute_cleanup_results()

    def breadformula_totalweight_percentage_sourdoughtpercentage(self,yeastoption):
        debug_print ("breadformula_totalweight_percentage_sourdoughtpercentage")
        self.init_sourdought(yeastoption)
        if yeastoption == "yeast":
            debug_print("with yeast only")
            self.breadformula_totalweight_percentage(yeastoption)
        else:
            debug_print("including sourdought") #to double check
            self.totalweight_percentage=self.percentage+100
            self.flour=(self.totalweight/self.totalweight_percentage)*(100-(self.sourdoughtpercentage/2.0))
            self.water=(self.totalweight/self.totalweight_percentage)*(self.percentage-(self.sourdoughtpercentage/2.0))
            self.sourdought=self.totalweight-self.flour-self.water
            window.display_message(_(u"executed formula using totalweight, percentage and and sourdought percentage"))

    def breadformula_flour_water_totalweight(self,yeastoption):
        debug_print("breadformula_flour_water_totalweight")
        self.init_sourdought(yeastoption)
        if yeastoption == "yeast":
            debug_print("with yeast only")
            self.percentage=(self.water)/(float(self.flour))*100
            self.salt_and_yeast_calculation()
            window.display_message(_(u"executed formula using flour, water and totalweight"))
        else:
            debug_print("including sourdought")
            self.sourdought=self.totalweight-self.flour-self.water
            self.percentage=(self.water+self.sourdought_water)/(float(self.flour)+self.sourdought_flour)*100
            self.salt_and_yeast_calculation()
            window.display_message(_(u"executed formula using flour, water and totalweight"))

    def breadformula_flour_totalweight_percentage(self,yeastoption):
        debug_print("breadformula_flour_totalweight_percentage")
        self.init_sourdought(yeastoption)
        if yeastoption == "yeast":
            debug_print("with yeast only")
            self.breadformula_flour_totalweight(yeastoption)
        else:
            debug_print("including sourdought")
            window.display_message(_(u"no enough ingredients to make a selection with flour, totalweight and percentage!"))
            window.execute_cleanup_results()

    def breadformula_water_totalweight_percentage(self,yeastoption):
        debug_print("breadformula_water_totalweight_percentage")
        self.init_sourdought(yeastoption)
        if yeastoption == "yeast":
            debug_print("with yeast only")
            self.breadformula_water_totalweight(yeastoption)
        else:
            debug_print("including sourdought")
            window.display_message(_(u"no enough ingredients to make a selection with water, totalweight and percentage!"))
            window.execute_cleanup_results()

    def breadformula_flour_water_sourdought(self,yeastoption):
        debug_print("breadformula_flour_water_sourdought")
        self.init_sourdought(yeastoption)
        if yeastoption == "yeast":
            debug_print("with yeast only")
            self.breadformula_flour_water(yeastoption)
        else:
            debug_print("including sourdought")
            self.totalweight=self.sourdought+self.flour+self.water
            self.percentage=(self.water+self.sourdought_water)/(float(self.flour)+self.sourdought_flour)*100
            self.salt_and_yeast_calculation()
            window.display_message(_(u"executed formula using flour, water and sourdought"))

    def breadformula_flour_water_percentage(self,yeastoption):
        debug_print("breadformula_flour_water_percentage")
        self.init_sourdought(yeastoption)
        if yeastoption == "yeast":
            debug_print("with yeast only")
            self.breadformula_flour_water(yeastoption)
        else:
            debug_print("including sourdought")
            if self.sourdought > 0:
                self.totalweight=self.flour+self.sourdought+self.water
            else:
                window.display_message(_(u"no enough ingredients to make a selection with flour, water and percentage!"))
                window.execute_cleanup_results()

    def breadformula_flour_totalweight_sourdought(self,yeastoption):
        debug_print("breadformula_flour_totalweight_sourdought")
        self.init_sourdought(yeastoption)
        if yeastoption == "yeast":
            debug_print("with yeast only")
            self.breadformula_flour_totalweight(yeastoption)
        else:
            debug_print("including sourdought")
            self.water=self.totalweight-self.flour-self.sourdought
            self.percentage=((self.water+self.sourdought_water)/float(self.flour+self.sourdought_flour))*100
            self.salt_and_yeast_calculation()
            window.display_message(_(u"executed formula using flour, totalweight and sourdought"))

    def breadformula_flour_percentage_sourdought(self,yeastoption):
        debug_print("breadformula_flour_percentage_sourdought")
        self.init_sourdought(yeastoption)
        if yeastoption == "yeast":
            debug_print("with yeast only")
            self.breadformula_flour_percentage(yeastoption)
        else:
            debug_print("including sourdought")
            window.display_message(_(u"no enough ingredients to make a selection with flour, percentage and sourdought!"))
            window.execute_cleanup_results()

    def breadformula_water_percentage_sourdought(self,yeastoption):
        debug_print("breadformula_water_percentage_sourdought")
        self.init_sourdought(yeastoption)
        if yeastoption == "yeast":
            debug_print("with yeast only")
            self.breadformula_water_percentage(yeastoption)
        else:
            debug_print("including sourdought")
            window.display_message(_(u"no enough ingredients to make a selection with water, percentage and sourdought!"))
            window.execute_cleanup_results()

    def breadformula_water_totalweight_sourdought(self,yeastoption):
        debug_print("breadformula_water_totalweight_sourdought")
        self.init_sourdought(yeastoption)
        if yeastoption == "yeast":
            debug_print("with yeast only")
            self.breadformula_water_totalweight(yeastoption)
        else:
            debug_print("including sourdought")
            self.flour=self.totalweight-self.water-self.sourdought
            self.percentage=((self.water+self.sourdought_water)/float(self.flour+self.sourdought_flour))*100
            self.salt_and_yeast_calculation()
            window.display_message(_(u"executed formula using water, totalweight and sourdought"))

    def breadformula_totalweight_percentage_sourdought(self,yeastoption):
        debug_print("breadformula_totalweight_percentage_sourdought")
        self.init_sourdought(yeastoption)
        if yeastoption == "yeast":
            debug_print("with yeast only")
            self.breadformula_totalweight_percentage(yeastoption)
        else:
            debug_print("including sourdought")
            self.flour=(self.totalweight/float((100+self.percentage)/100.00))-self.sourdought_flour
            self.water=self.totalweight-self.flour-self.sourdought_flour-self.sourdought_water
            self.salt_and_yeast_calculation()
            window.display_message(_(u"executed formula using totalweight, percentage and sourdought"))

def debug_print(message):
    if DEBUG == "YES":
        print "message: %s" % message

def main():
    global mybread
    global window

    mybread=Breadmaker()

    app = wx.App()
    window=MyWindow(None)
    window.SetTitle(_(u"Bread maker"))
    window.Show()
    app.MainLoop()
    exit()

if __name__ == '__main__':
    main()