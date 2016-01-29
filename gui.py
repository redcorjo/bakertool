# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Bread Maker"), pos = wx.DefaultPosition, size = wx.Size( 666,768 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer_all_details = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"All details") ), wx.HORIZONTAL )
		
		sbSizer_my_ingredients = wx.StaticBoxSizer( wx.StaticBox( sbSizer_all_details.GetStaticBox(), wx.ID_ANY, _(u"My ingredients") ), wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText_flour_input = wx.StaticText( sbSizer_my_ingredients.GetStaticBox(), wx.ID_ANY, _(u"Flour"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_flour_input.Wrap( -1 )
		gSizer1.Add( self.m_staticText_flour_input, 0, wx.ALL, 5 )
		
		self.flour_entry = wx.TextCtrl( sbSizer_my_ingredients.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.flour_entry, 0, wx.ALL, 5 )
		
		self.m_staticText_water_input = wx.StaticText( sbSizer_my_ingredients.GetStaticBox(), wx.ID_ANY, _(u"Water"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_water_input.Wrap( -1 )
		gSizer1.Add( self.m_staticText_water_input, 0, wx.ALL, 5 )
		
		self.water_entry = wx.TextCtrl( sbSizer_my_ingredients.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.water_entry, 0, wx.ALL, 5 )
		
		self.m_staticText_total_weight_input = wx.StaticText( sbSizer_my_ingredients.GetStaticBox(), wx.ID_ANY, _(u"Total Weight"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_total_weight_input.Wrap( -1 )
		gSizer1.Add( self.m_staticText_total_weight_input, 0, wx.ALL, 5 )
		
		self.totalweight_entry = wx.TextCtrl( sbSizer_my_ingredients.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.totalweight_entry, 0, wx.ALL, 5 )
		
		self.m_staticText_sourdought_input = wx.StaticText( sbSizer_my_ingredients.GetStaticBox(), wx.ID_ANY, _(u"Sourdought"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_sourdought_input.Wrap( -1 )
		self.m_staticText_sourdought_input.Hide()
		
		gSizer1.Add( self.m_staticText_sourdought_input, 0, wx.ALL, 5 )
		
		self.sourdought_entry = wx.TextCtrl( sbSizer_my_ingredients.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sourdought_entry.Hide()
		
		gSizer1.Add( self.sourdought_entry, 0, wx.ALL, 5 )
		
		self.m_staticText_percentage_input = wx.StaticText( sbSizer_my_ingredients.GetStaticBox(), wx.ID_ANY, _(u"Percentage"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_percentage_input.Wrap( -1 )
		gSizer1.Add( self.m_staticText_percentage_input, 0, wx.ALL, 5 )
		
		self.percentage_entry = wx.TextCtrl( sbSizer_my_ingredients.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.percentage_entry, 0, wx.ALL, 5 )
		
		
		sbSizer_my_ingredients.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		sbSizer_all_details.Add( sbSizer_my_ingredients, 1, wx.ALL|wx.EXPAND, 5 )
		
		sbSizer_my_final_recipe = wx.StaticBoxSizer( wx.StaticBox( sbSizer_all_details.GetStaticBox(), wx.ID_ANY, _(u"My final recipe") ), wx.VERTICAL )
		
		gSizer2 = wx.GridSizer( 0, 3, 0, 0 )
		
		self.m_staticText_flour_results = wx.StaticText( sbSizer_my_final_recipe.GetStaticBox(), wx.ID_ANY, _(u"Flour"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_flour_results.Wrap( -1 )
		gSizer2.Add( self.m_staticText_flour_results, 0, wx.ALL, 5 )
		
		self.flour_results = wx.TextCtrl( sbSizer_my_final_recipe.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		gSizer2.Add( self.flour_results, 0, wx.ALL, 5 )
		
		self.flour_results_percentage = wx.TextCtrl( sbSizer_my_final_recipe.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.flour_results_percentage, 0, wx.ALL, 5 )
		
		self.m_staticText_water_output = wx.StaticText( sbSizer_my_final_recipe.GetStaticBox(), wx.ID_ANY, _(u"Water"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_water_output.Wrap( -1 )
		gSizer2.Add( self.m_staticText_water_output, 0, wx.ALL, 5 )
		
		self.water_results = wx.TextCtrl( sbSizer_my_final_recipe.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		gSizer2.Add( self.water_results, 0, wx.ALL, 5 )
		
		self.water_results_percentage = wx.TextCtrl( sbSizer_my_final_recipe.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.water_results_percentage, 0, wx.ALL, 5 )
		
		self.m_staticText_total_weight_output = wx.StaticText( sbSizer_my_final_recipe.GetStaticBox(), wx.ID_ANY, _(u"Total Weight"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_total_weight_output.Wrap( -1 )
		gSizer2.Add( self.m_staticText_total_weight_output, 0, wx.ALL, 5 )
		
		self.totalweight_results = wx.TextCtrl( sbSizer_my_final_recipe.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		gSizer2.Add( self.totalweight_results, 0, wx.ALL, 5 )
		
		self.totalweight_results_percentage = wx.TextCtrl( sbSizer_my_final_recipe.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.totalweight_results_percentage, 0, wx.ALL, 5 )
		
		self.m_staticText_yeast_output = wx.StaticText( sbSizer_my_final_recipe.GetStaticBox(), wx.ID_ANY, _(u"Yeast"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_yeast_output.Wrap( -1 )
		gSizer2.Add( self.m_staticText_yeast_output, 0, wx.ALL, 5 )
		
		self.yeast_results = wx.TextCtrl( sbSizer_my_final_recipe.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		gSizer2.Add( self.yeast_results, 0, wx.ALL, 5 )
		
		self.yeast_results_percentage = wx.TextCtrl( sbSizer_my_final_recipe.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.yeast_results_percentage, 0, wx.ALL, 5 )
		
		self.m_staticText_salt_output = wx.StaticText( sbSizer_my_final_recipe.GetStaticBox(), wx.ID_ANY, _(u"Salt"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_salt_output.Wrap( -1 )
		gSizer2.Add( self.m_staticText_salt_output, 0, wx.ALL, 5 )
		
		self.salt_results = wx.TextCtrl( sbSizer_my_final_recipe.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		gSizer2.Add( self.salt_results, 0, wx.ALL, 5 )
		
		self.salt_results_percentage = wx.TextCtrl( sbSizer_my_final_recipe.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.salt_results_percentage, 0, wx.ALL, 5 )
		
		self.m_staticText_sourdought_output = wx.StaticText( sbSizer_my_final_recipe.GetStaticBox(), wx.ID_ANY, _(u"Sourdought"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_sourdought_output.Wrap( -1 )
		self.m_staticText_sourdought_output.Hide()
		
		gSizer2.Add( self.m_staticText_sourdought_output, 0, wx.ALL, 5 )
		
		self.sourdought_results = wx.TextCtrl( sbSizer_my_final_recipe.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.sourdought_results.Hide()
		
		gSizer2.Add( self.sourdought_results, 0, wx.ALL, 5 )
		
		self.sourdought_results_percentage = wx.TextCtrl( sbSizer_my_final_recipe.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sourdought_results_percentage.Hide()
		
		gSizer2.Add( self.sourdought_results_percentage, 0, wx.ALL, 5 )
		
		self.m_staticText_percentage_output = wx.StaticText( sbSizer_my_final_recipe.GetStaticBox(), wx.ID_ANY, _(u"Percentage"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_percentage_output.Wrap( -1 )
		gSizer2.Add( self.m_staticText_percentage_output, 0, wx.ALL, 5 )
		
		self.percentage_results = wx.TextCtrl( sbSizer_my_final_recipe.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		gSizer2.Add( self.percentage_results, 0, wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( sbSizer_my_final_recipe.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		gSizer2.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		
		sbSizer_my_final_recipe.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		
		sbSizer_all_details.Add( sbSizer_my_final_recipe, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( sbSizer_all_details, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		sbSizer_messages = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Messages") ), wx.VERTICAL )
		
		self.m_textCtrl_display_message = wx.TextCtrl( sbSizer_messages.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_READONLY )
		sbSizer_messages.Add( self.m_textCtrl_display_message, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1.Add( sbSizer_messages, 1, wx.EXPAND, 5 )
		
		sbSizer_profiles = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Profiles") ), wx.VERTICAL )
		
		bSizer91 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText16 = wx.StaticText( sbSizer_profiles.GetStaticBox(), wx.ID_ANY, _(u"My recipe name: "), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		bSizer91.Add( self.m_staticText16, 0, wx.ALL, 5 )
		
		self.m_textCtrl_profile = wx.TextCtrl( sbSizer_profiles.GetStaticBox(), wx.ID_ANY, _(u"default"), wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PROCESS_ENTER )
		bSizer91.Add( self.m_textCtrl_profile, 0, wx.ALL, 5 )
		
		m_choice_profileChoices = [ _(u"default") ]
		self.m_choice_profile = wx.Choice( sbSizer_profiles.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), m_choice_profileChoices, 0 )
		self.m_choice_profile.SetSelection( 0 )
		bSizer91.Add( self.m_choice_profile, 0, wx.ALL, 5 )
		
		
		sbSizer_profiles.Add( bSizer91, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( sbSizer_profiles, 1, wx.EXPAND, 5 )
		
		sbSizer_actions = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Actions") ), wx.VERTICAL )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer4.SetMinSize( wx.Size( 2,1 ) ) 
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer9.SetMinSize( wx.Size( 300,-1 ) ) 
		self.m_button1 = wx.Button( sbSizer_actions.GetStaticBox(), wx.ID_ANY, _(u"Execute"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.wizard_selection = wx.Button( sbSizer_actions.GetStaticBox(), wx.ID_ANY, _(u"Wizard"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.wizard_selection, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.cleanup_form = wx.Button( sbSizer_actions.GetStaticBox(), wx.ID_ANY, _(u"Cleanup"), wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		bSizer9.Add( self.cleanup_form, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		m_radioBox_yeast_selectionChoices = [ _(u"Sourdought only"), _(u"Dry yeast only"), _(u"Fresh yeast only"), _(u"Combined sourdought with dry yeast"), _(u"Combined sourdought with fresh yeast") ]
		self.m_radioBox_yeast_selection = wx.RadioBox( sbSizer_actions.GetStaticBox(), wx.ID_ANY, _(u"Yeast selection"), wx.DefaultPosition, wx.DefaultSize, m_radioBox_yeast_selectionChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox_yeast_selection.SetSelection( 1 )
		bSizer4.Add( self.m_radioBox_yeast_selection, 0, wx.ALL, 5 )
		
		
		sbSizer_actions.Add( bSizer4, 1, 0, 5 )
		
		
		bSizer1.Add( sbSizer_actions, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar = wx.MenuBar( 0 )
		self.m_menu_file = wx.Menu()
		self.m_menuItem_open = wx.MenuItem( self.m_menu_file, wx.ID_ANY, _(u"Open"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.AppendItem( self.m_menuItem_open )
		
		self.m_menuItem_save = wx.MenuItem( self.m_menu_file, wx.ID_ANY, _(u"Save"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.AppendItem( self.m_menuItem_save )
		
		self.m_menuItem_save_as = wx.MenuItem( self.m_menu_file, wx.ID_ANY, _(u"Save As"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.AppendItem( self.m_menuItem_save_as )
		
		self.m_menu_file.AppendSeparator()
		
		self.m_menuItem_print = wx.MenuItem( self.m_menu_file, wx.ID_ANY, _(u"Print"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.AppendItem( self.m_menuItem_print )
		
		self.m_menu_file.AppendSeparator()
		
		self.m_menuItem_exit = wx.MenuItem( self.m_menu_file, wx.ID_ANY, _(u"Exit"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.AppendItem( self.m_menuItem_exit )
		
		self.m_menubar.Append( self.m_menu_file, _(u"File") ) 
		
		self.m_menu_help = wx.Menu()
		self.m_menuItem_help = wx.MenuItem( self.m_menu_help, wx.ID_ANY, _(u"Help"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_help.AppendItem( self.m_menuItem_help )
		
		self.m_menu_help.AppendSeparator()
		
		self.m_menuItem_about = wx.MenuItem( self.m_menu_help, wx.ID_ANY, _(u"About"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_help.AppendItem( self.m_menuItem_about )
		
		self.m_menubar.Append( self.m_menu_help, _(u"Help") ) 
		
		self.SetMenuBar( self.m_menubar )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.close_my_app )
		self.m_textCtrl_profile.Bind( wx.EVT_TEXT_ENTER, self.execute_profilename )
		self.m_choice_profile.Bind( wx.EVT_CHOICE, self.execute_onchoice_profile )
		self.m_button1.Bind( wx.EVT_BUTTON, self.execute_breadformula )
		self.wizard_selection.Bind( wx.EVT_BUTTON, self.execute_wizard )
		self.cleanup_form.Bind( wx.EVT_BUTTON, self.execute_cleanup )
		self.m_radioBox_yeast_selection.Bind( wx.EVT_RADIOBOX, self.execute_yeast_selection )
		self.Bind( wx.EVT_MENU, self.execute_open, id = self.m_menuItem_open.GetId() )
		self.Bind( wx.EVT_MENU, self.execute_save, id = self.m_menuItem_save.GetId() )
		self.Bind( wx.EVT_MENU, self.execute_save_as, id = self.m_menuItem_save_as.GetId() )
		self.Bind( wx.EVT_MENU, self.close_my_app, id = self.m_menuItem_exit.GetId() )
		self.Bind( wx.EVT_MENU, self.execute_help, id = self.m_menuItem_help.GetId() )
		self.Bind( wx.EVT_MENU, self.execute_about, id = self.m_menuItem_about.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def close_my_app( self, event ):
		event.Skip()
	
	def execute_profilename( self, event ):
		event.Skip()
	
	def execute_onchoice_profile( self, event ):
		event.Skip()
	
	def execute_breadformula( self, event ):
		event.Skip()
	
	def execute_wizard( self, event ):
		event.Skip()
	
	def execute_cleanup( self, event ):
		event.Skip()
	
	def execute_yeast_selection( self, event ):
		event.Skip()
	
	def execute_open( self, event ):
		event.Skip()
	
	def execute_save( self, event ):
		event.Skip()
	
	def execute_save_as( self, event ):
		event.Skip()
	
	
	def execute_help( self, event ):
		event.Skip()
	
	def execute_about( self, event ):
		event.Skip()
	

###########################################################################
## Class MyDialog_select_percentage_with_sourdought
###########################################################################

class MyDialog_select_percentage_with_sourdought ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Select Percentages"), pos = wx.DefaultPosition, size = wx.Size( 390,323 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText_selected_final_weight = wx.StaticText( self, wx.ID_ANY, _(u"Selected final weight"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_selected_final_weight.Wrap( -1 )
		bSizer5.Add( self.m_staticText_selected_final_weight, 0, wx.ALL, 5 )
		
		self.totalweight_entry = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.totalweight_entry, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Percentage section") ), wx.VERTICAL )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( sbSizer7.GetStaticBox(), wx.ID_ANY, _(u"Bread percentage formula") ), wx.VERTICAL )
		
		self.m_slider_percentage = wx.Slider( sbSizer6.GetStaticBox(), wx.ID_ANY, 60, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_HORIZONTAL|wx.SL_LABELS|wx.STATIC_BORDER )
		sbSizer6.Add( self.m_slider_percentage, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		sbSizer7.Add( sbSizer6, 1, wx.EXPAND, 5 )
		
		sbSizer_slider_sourdought = wx.StaticBoxSizer( wx.StaticBox( sbSizer7.GetStaticBox(), wx.ID_ANY, _(u"Sourdought percentage versus total weight") ), wx.VERTICAL )
		
		self.m_slider_percentage_sourdought = wx.Slider( sbSizer_slider_sourdought.GetStaticBox(), wx.ID_ANY, 10, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_HORIZONTAL|wx.SL_LABELS|wx.STATIC_BORDER )
		sbSizer_slider_sourdought.Add( self.m_slider_percentage_sourdought, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		sbSizer7.Add( sbSizer_slider_sourdought, 1, wx.EXPAND, 5 )
		
		
		bSizer4.Add( sbSizer7, 1, wx.EXPAND, 5 )
		
		self.m_button_execute_selection = wx.Button( self, wx.ID_ANY, _(u"Ok"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button_execute_selection, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button_execute_selection.Bind( wx.EVT_BUTTON, self.execute_percentage_formula )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def execute_percentage_formula( self, event ):
		event.Skip()
	

###########################################################################
## Class MyDialog_select_percentage_without_sourdought
###########################################################################

class MyDialog_select_percentage_without_sourdought ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Select Percentages"), pos = wx.DefaultPosition, size = wx.Size( 402,246 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText_selected_final_weight = wx.StaticText( self, wx.ID_ANY, _(u"Selected final weight"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_selected_final_weight.Wrap( -1 )
		bSizer5.Add( self.m_staticText_selected_final_weight, 0, wx.ALL, 5 )
		
		self.totalweight_entry = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.totalweight_entry, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Percentage section") ), wx.VERTICAL )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( sbSizer7.GetStaticBox(), wx.ID_ANY, _(u"Bread percentage formula") ), wx.VERTICAL )
		
		self.m_slider_percentage = wx.Slider( sbSizer6.GetStaticBox(), wx.ID_ANY, 60, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_HORIZONTAL|wx.SL_LABELS|wx.STATIC_BORDER )
		sbSizer6.Add( self.m_slider_percentage, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		sbSizer7.Add( sbSizer6, 1, wx.EXPAND, 5 )
		
		
		bSizer4.Add( sbSizer7, 1, wx.EXPAND, 5 )
		
		self.m_button_execute_selection = wx.Button( self, wx.ID_ANY, _(u"Ok"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button_execute_selection, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button_execute_selection.Bind( wx.EVT_BUTTON, self.execute_percentage_formula )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def execute_percentage_formula( self, event ):
		event.Skip()
	

