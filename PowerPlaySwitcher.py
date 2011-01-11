#!/usr/bin/python
#PowerPlaySwitcher 0.2 (now python) [the 0.1 was in Perl]
gtkbuilderui_xml = '''
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <requires lib="gtk+" version="2.16"/>
  <!-- interface-naming-policy project-wide -->
  <object class="GtkWindow" id="power_play_switcher_window">
    <signal name="destroy" handler="on_power_play_switcher_window_destroy"/>
    <child>
      <object class="GtkVBox" id="vbox_main">
        <property name="visible">True</property>
        <property name="spacing">6</property>
        <child>
          <object class="GtkAlignment" id="alignment_methods_title">
            <property name="visible">True</property>
            <child>
              <object class="GtkLabel" id="label_methods_title">
                <property name="visible">True</property>
                <property name="label" translatable="yes">Power Management Methods</property>
                <property name="single_line_mode">True</property>
                <attributes>
                  <attribute name="weight" value="bold"/>
                </attributes>
              </object>
            </child>
          </object>
          <packing>
            <property name="position">0</property>
          </packing>
        </child>
        <child>
          <object class="GtkAlignment" id="alignment_method_dynpm">
            <property name="visible">True</property>
            <property name="left_padding">4</property>
            <child>
              <object class="GtkRadioButton" id="radiobutton_method_dynpm">
                <property name="label" translatable="yes">Dynamic Power Management Method (dynpm)</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">False</property>
                <property name="active">True</property>
                <property name="draw_indicator">True</property>
                <signal name="toggled" handler="on_radiobutton_method_dynpm_toggled"/>
              </object>
            </child>
          </object>
          <packing>
            <property name="position">1</property>
          </packing>
        </child>
        <child>
          <object class="GtkAlignment" id="alignment_method_profile">
            <property name="visible">True</property>
            <property name="left_padding">4</property>
            <child>
              <object class="GtkRadioButton" id="radiobutton_method_profile">
                <property name="label" translatable="yes">Profile Method (profile)</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">False</property>
                <property name="active">True</property>
                <property name="draw_indicator">True</property>
                <property name="group">radiobutton_method_dynpm</property>
              </object>
            </child>
          </object>
          <packing>
            <property name="position">2</property>
          </packing>
        </child>
        <child>
          <object class="GtkAlignment" id="alignment_profile_auto">
            <property name="visible">True</property>
            <property name="left_padding">30</property>
            <child>
              <object class="GtkRadioButton" id="radiobutton_profile_auto">
                <property name="label" translatable="yes">Auto (mid on dc, high on ac)</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">False</property>
                <property name="active">True</property>
                <property name="draw_indicator">True</property>
              </object>
            </child>
          </object>
          <packing>
            <property name="position">3</property>
          </packing>
        </child>
        <child>
          <object class="GtkAlignment" id="alignment_profile_low">
            <property name="visible">True</property>
            <property name="left_padding">30</property>
            <child>
              <object class="GtkRadioButton" id="radiobutton_profile_low">
                <property name="label" translatable="yes">Low</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">False</property>
                <property name="active">True</property>
                <property name="draw_indicator">True</property>
                <property name="group">radiobutton_profile_auto</property>
              </object>
            </child>
          </object>
          <packing>
            <property name="position">4</property>
          </packing>
        </child>
        <child>
          <object class="GtkAlignment" id="alignment_profile_mid">
            <property name="visible">True</property>
            <property name="left_padding">30</property>
            <child>
              <object class="GtkRadioButton" id="radiobutton_profile_mid">
                <property name="label" translatable="yes">Mid</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">False</property>
                <property name="active">True</property>
                <property name="draw_indicator">True</property>
                <property name="group">radiobutton_profile_auto</property>
              </object>
            </child>
          </object>
          <packing>
            <property name="position">5</property>
          </packing>
        </child>
        <child>
          <object class="GtkAlignment" id="alignment_profile_high">
            <property name="visible">True</property>
            <property name="left_padding">30</property>
            <child>
              <object class="GtkRadioButton" id="radiobutton_profile_high">
                <property name="label" translatable="yes">High</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">False</property>
                <property name="active">True</property>
                <property name="draw_indicator">True</property>
                <property name="group">radiobutton_profile_auto</property>
              </object>
            </child>
          </object>
          <packing>
            <property name="position">6</property>
          </packing>
        </child>
        <child>
          <object class="GtkAlignment" id="alignment_profile_default">
            <property name="visible">True</property>
            <property name="left_padding">30</property>
            <child>
              <object class="GtkRadioButton" id="radiobutton_profile_default">
                <property name="label" translatable="yes">Default (power management off)</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">False</property>
                <property name="active">True</property>
                <property name="draw_indicator">True</property>
                <property name="group">radiobutton_profile_auto</property>
              </object>
            </child>
          </object>
          <packing>
            <property name="position">7</property>
          </packing>
        </child>
        <child>
          <object class="GtkAlignment" id="alignment_button_apply">
            <property name="visible">True</property>
            <property name="bottom_padding">12</property>
            <property name="left_padding">334</property>
            <property name="right_padding">12</property>
            <child>
              <object class="GtkButton" id="button_apply">
                <property name="label">gtk-apply</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <property name="use_stock">True</property>
                <signal name="clicked" handler="on_button_apply_clicked"/>
              </object>
            </child>
          </object>
          <packing>
            <property name="position">8</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
</interface>
'''

import pygtk
pygtk.require('2.0')
import glib
import gtk
import os
import re

class PowerPlaySwitcher(object):       
	POWER_METHOD_PROFILE = "profile"
	POWER_METHOD_DYNAMIC = "dynpm"
	POWER_PROFILES = {'LOW':"low", 'MID':"mid", 'HIGH':"high", 'AUTO':"auto", 'DEFAULT':"default"}
	POWER_PROFILE_FILE_PATH = "/sys/class/drm/card0/device/power_profile"
	POWER_METHOD_FILE_PATH  = "/sys/class/drm/card0/device/power_method"
	INFO_FILE_PATH = "/sys/kernel/debug/dri/0/radeon_pm_info"
	WINDOW_TITLE_PREFIX = "PowerPlay Switcher"
	builder = None
	window = None

	def __init__(self):
		self.builder = gtk.Builder()
		#self.builder.add_from_file( 'PowerPlaySwitcher.xml' )
		self.builder.add_from_string( gtkbuilderui_xml )

		self.window = self.builder.get_object( 'power_play_switcher_window' )
		self.builder.connect_signals( self )

		self.initialize()

		self.window.show()
	
	def initialize(self):
		if (self.is_supported_environment()):
			current_method = self.get_current_power_method()
	
			self.builder.get_object('radiobutton_method_' + current_method).set_active(True)

			if (current_method == self.POWER_METHOD_PROFILE):
				current_profile = self.get_current_power_profile()
				self.builder.get_object('radiobutton_profile_' + current_profile).set_active(True)
			
			def update_title():
				info = self.get_info()
				self.window.set_title("%s (%s, mem: %s, %s)" % (self.WINDOW_TITLE_PREFIX, info['engine'], info['memory'], info['voltage']))
				return 1  # return 0 or 1 to kill/keep timer going
	
			id = glib.timeout_add(500, update_title)
		
			if (self.is_readonly_environment()):
				self.disable_all_controls()
				self.show_dialog(title="You are not root!", message=" You are not root, readonly mode ")

		else:
			self.disable_all_controls()
			self.show_dialog(
				title="Not supported environment!",
				message="Seems you are on an unsupported environment\ncheck you have an ATI Radeon with PowerPlay, " +
				"you are using\nthe open source driver, the kernel version is >= 2.6.35\nand KMS is enabled")

	def on_power_play_switcher_window_destroy(self, widget, data=None):
	    gtk.main_quit()

	def on_button_apply_clicked(self, widget, data=None):
		radio_method_profile = self.builder.get_object('radiobutton_method_profile')
		if (radio_method_profile.get_active()):
			radio_auto = self.builder.get_object('radiobutton_profile_auto')
			radio_low = self.builder.get_object('radiobutton_profile_low')
			radio_mid = self.builder.get_object('radiobutton_profile_mid')
			radio_high = self.builder.get_object('radiobutton_profile_high')
			radio_default = self.builder.get_object('radiobutton_profile_default')
	
			profile = self.POWER_PROFILES['DEFAULT']
			if (radio_auto.get_active()):
				profile = self.POWER_PROFILES['AUTO']
			elif (radio_low.get_active()):
				profile = self.POWER_PROFILES['LOW']
			elif (radio_mid.get_active()):
				profile = self.POWER_PROFILES['MID']
			elif (radio_high.get_active()):
				profile = self.POWER_PROFILES['HIGH']
		
			print "profile: " + profile

			self.set_current_power_method(self.POWER_METHOD_PROFILE)
			self.set_current_power_profile(profile)
		else:
			print "dynpm"
			self.set_current_power_method(self.POWER_METHOD_DYNAMIC)

		self.initialize()

	def on_radiobutton_method_dynpm_toggled(self, radio, data=None):
		if (radio.get_active()):
			#### DYNPM METHOD
			print "Dynpm Method Selected"		
			self.disable_profiles_radiobuttons()
		else:
			#### PROFILE METHOD
			print "Profile Method Selected"		
			self.enable_profiles_radiobuttons()

	def show_dialog(self, title, message):
		dialog = gtk.Dialog(title, self.window, gtk.DIALOG_DESTROY_WITH_PARENT,	(gtk.STOCK_OK, gtk.RESPONSE_ACCEPT))
		label = gtk.Label(message)
		dialog.get_content_area().add(label)
		# Ensure that the dialog box is destroyed when the user responds.
		def on_response(self, widget, data=None): self.destroy()
		dialog.connect("response", on_response)
		dialog.show_all()

	def enable_profiles_radiobuttons(self): self.toggle_profiles_radiobuttons(True)
	def disable_profiles_radiobuttons(self): self.toggle_profiles_radiobuttons(False)
	def toggle_profiles_radiobuttons(self,true_false):
		self.builder.get_object('radiobutton_profile_auto').set_sensitive(true_false)
		self.builder.get_object('radiobutton_profile_low').set_sensitive(true_false)
		self.builder.get_object('radiobutton_profile_mid').set_sensitive(true_false)
		self.builder.get_object('radiobutton_profile_high').set_sensitive(true_false)
		self.builder.get_object('radiobutton_profile_default').set_sensitive(true_false)

	def disable_all_controls(self):
		self.builder.get_object('radiobutton_method_profile').set_sensitive(False)
		self.builder.get_object('radiobutton_method_dynpm').set_sensitive(False)
		self.builder.get_object('button_apply').set_sensitive(False)
		self.disable_profiles_radiobuttons()

	def is_supported_environment(self):
		if (os.access(self.POWER_METHOD_FILE_PATH, os.R_OK)):
			return True
		else:
			return False
		
	def is_readonly_environment(self):
		if (os.access(self.POWER_METHOD_FILE_PATH, os.W_OK)):
			return False
		else:
			return True

	def get_current_power_method(self):
		fileMethod = open(self.POWER_METHOD_FILE_PATH,"rt")
		method = fileMethod.readline()
		fileMethod.close()
		return method.strip()

	def get_current_power_profile(self):
		fileProfile = open(self.POWER_PROFILE_FILE_PATH,"rt")
		profile = fileProfile.readline()
		fileProfile.close()
		return profile.strip()

	def set_current_power_method(self, method):
		print "SETTING method: " + method
		fileMethod = open(self.POWER_METHOD_FILE_PATH,"wt")
		fileMethod.write(method)
		fileMethod.close()

	def set_current_power_profile(self, profile):
		print "SETTING profile: " + profile
		fileProfile = open(self.POWER_PROFILE_FILE_PATH,"wt")
		fileProfile.write(profile)
		fileProfile.close()

	def get_info(self):
		#info file default response:
		#default engine clock: 680000 kHz
		#current engine clock: 109680 kHz
		#default memory clock: 800000 kHz
		#current memory clock: 249750 kHz
		#voltage: 950 mV
		engine_clock = ""
		memory_clock = ""
		voltage = ""

		if (os.path.exists(self.INFO_FILE_PATH)):
			file_info = open (self.INFO_FILE_PATH, "rt")
			while (True):
				line = file_info.readline();
				if (line == ""): break #stops at the end of the file

				match = re.search("current engine clock: (.*)",line) 
				if (match):
					engine_clock = match.group(1).strip()

				match = re.search("current memory clock: (.*)", line)
				if (match):
					memory_clock = match.group(1).strip()
		
				match = re.search("voltage: (.*)", line)
				if (match):
					voltage = match.group(1).strip()
		
		return {'memory': memory_clock, 'engine': engine_clock, 'voltage': voltage}


if __name__ == "__main__":
	app = PowerPlaySwitcher()
	gtk.main()


