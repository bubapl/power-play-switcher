#!/usr/bin/env perl

use strict;
use warnings;
use utf8;
use Glib qw{ TRUE FALSE };
use Gtk2 '-init';
use Data::Dumper;

my $POWER_METHOD_PROFILE = "profile";
my $POWER_METHOD_DYNAMIC = "dynpm";
my $POWER_PROFILES = {LOW=>"low", MID=>"mid", HIGH=>"high", AUTO=>"auto", DEFAULT=>"default"};
my $POWER_PROFILE_FILE_PATH = "/sys/class/drm/card0/device/power_profile";
my $POWER_METHOD_FILE_PATH  = "/sys/class/drm/card0/device/power_method";
my $INFO_FILE_PATH = "/sys/kernel/debug/dri/0/radeon_pm_info";
my $WINDOW_TITLE_PREFIX = "PowerPlay Switcher";
my $builder;
my $window;

$builder = Gtk2::Builder->new();
$builder->add_from_file( 'PowerPlaySwitcher.xml' );

$window = $builder->get_object( 'power_play_switcher_window' );
$builder->connect_signals( undef );

initialize();

$window->show();
Gtk2->main();

sub initialize {
	if (is_supported_environment()) {
		my $current_method = get_current_power_method();
	
		$builder->get_object('radiobutton_method_' . $current_method)->set_active(1);

		if ($current_method eq $POWER_METHOD_PROFILE) {
			my $current_profile = get_current_power_profile();
			$builder->get_object('radiobutton_profile_' . $current_profile)->set_active(1);
		}

		my $id = Glib::Timeout->add (500, \&update_title);
		

		sub update_title {
			my $info = get_info();
			$window->set_title("$WINDOW_TITLE_PREFIX ($info->{engine}, mem: $info->{memory}, $info->{voltage})");
			return 1;  # return 0 or 1 to kill/keep timer going
		}

		if (is_readonly_environment()) {
			disable_all_controls();
			show_dialog({title=>"You are not root!",message=>" You are not root, readonly mode "})
		}
		
	}
	else {
		show_dialog({
			title=>"Not supported environment!",
			message=>"Seems you are on an unsupported environment\ncheck you have an ATI Radeon with PowerPlay, " .
			"you are using\nthe open source driver, the kernel version is >= 2.6.35\nand KMS is enabled"});
	}
}

sub on_power_play_switcher_window_destroy
{
    Gtk2->main_quit();
}

sub on_button_apply_clicked {
	my $radio_method_profile = $builder->get_object('radiobutton_method_profile');
	if ($radio_method_profile->get_active()) {
		my $radio_auto = $builder->get_object('radiobutton_profile_auto');
		my $radio_low = $builder->get_object('radiobutton_profile_low');
		my $radio_mid = $builder->get_object('radiobutton_profile_mid');
		my $radio_high = $builder->get_object('radiobutton_profile_high');
		my $radio_default = $builder->get_object('radiobutton_profile_default');
	
		my $profile = $POWER_PROFILES->{DEFAULT};
		if ($radio_auto->get_active()) {
			$profile = $POWER_PROFILES->{AUTO};
		}
		elsif ($radio_low->get_active()) {
			$profile = $POWER_PROFILES->{LOW};
		}
		elsif ($radio_mid->get_active()) {
			$profile = $POWER_PROFILES->{MID};
		}
		elsif ($radio_high->get_active()) {
			$profile = $POWER_PROFILES->{HIGH};
		}

		print "profile: $profile\n";

		set_current_power_method($POWER_METHOD_PROFILE);
		set_current_power_profile($profile);
	}
	else {
		print "dynpm\n";
		set_current_power_method($POWER_METHOD_DYNAMIC);
	}
	initialize();
}
sub on_radiobutton_method_dynpm_toggled {
	my $radio = shift;
	if ($radio->get_active()) {
		#### DYNPM METHOD
		print "Dynpm Method Selected\n";		
		disable_profiles_radiobuttons(0);
	} else {
		#### PROFILE METHOD
		print "Profile Method Selected\n";		
		enable_profiles_radiobuttons(0);
	}
}

sub show_dialog {
	my $params = shift;
	my $title = $params->{title};
	my $message = $params->{message};
	my $dialog = Gtk2::Dialog->new ($title, $window, 'destroy-with-parent', 'gtk-ok' => 'none');
	my $label = Gtk2::Label->new ($message);
	$dialog->get_content_area ()->add ($label);
	# Ensure that the dialog box is destroyed when the user responds.
	$dialog->signal_connect (response => sub { $_[0]->destroy });
	$dialog->show_all;
}
sub enable_profiles_radiobuttons {toggle_profiles_radiobuttons(1);}
sub disable_profiles_radiobuttons {toggle_profiles_radiobuttons(0);}
sub toggle_profiles_radiobuttons {
	my $true_false = shift;
	$builder->get_object('radiobutton_profile_auto')->set_sensitive($true_false);
	$builder->get_object('radiobutton_profile_low')->set_sensitive($true_false);
	$builder->get_object('radiobutton_profile_mid')->set_sensitive($true_false);
	$builder->get_object('radiobutton_profile_high')->set_sensitive($true_false);
	$builder->get_object('radiobutton_profile_default')->set_sensitive($true_false);
}
sub disable_all_controls {
	$builder->get_object('radiobutton_method_profile')->set_sensitive(0);
	$builder->get_object('radiobutton_method_dynpm')->set_sensitive(0);	
	$builder->get_object('button_apply')->set_sensitive(0);	
	disable_profiles_radiobuttons();
}

sub on_radiobutton_profile_auto_toggled {
	my $radio = shift;
	if ($radio->get_active()) {
		print "auto\n";
	}
}
sub on_radiobutton_profile_low_toggled {
	my $radio = shift;
	if ($radio->get_active()) {
		print "low\n";
	}
}
sub on_radiobutton_profile_mid_toggled {
	my $radio = shift;
	if ($radio->get_active()) {
		print "mid\n";
	}
}
sub on_radiobutton_profile_high_toggled {
	my $radio = shift;
	if ($radio->get_active()) {
		print "high\n";
	}
}
sub on_radiobutton_profile_default_toggled {
	my $radio = shift;
	if ($radio->get_active()) {
		print "default\n";
	}
}

sub is_supported_environment {
	if (-r $POWER_METHOD_FILE_PATH) {
		return 1;
	}
	else {
		return 0;
	}
}
sub is_readonly_environment {
	if (-w $POWER_METHOD_FILE_PATH) {
		return 0;	
	}
	else {
		return 1;
	}
}

sub get_current_power_method {
	my $file_method;
	my $method;
	open($file_method,  "< $POWER_METHOD_FILE_PATH");
	while (<$file_method>) {
		chomp;
		$method = $_;
		last;
	}
	close $file_method;
	return $method;
}
sub get_current_power_profile {
	my $file_profile;
	my $profile;
	open($file_profile,  "< $POWER_PROFILE_FILE_PATH");
	while (<$file_profile>) {
		chomp;
		$profile = $_;
		last;
	}
	close $file_profile;
	return $profile;
}

sub set_current_power_method {
	my $method = shift;
	my $file_method;
	open($file_method,  "> $POWER_METHOD_FILE_PATH");
	print "SETTING method: $method\n";
	print $file_method $method;
	close $file_method;
}
sub set_current_power_profile {
	my $profile = shift;
	my $file_profile;	
	open($file_profile,  "> $POWER_PROFILE_FILE_PATH");
	print "SETTING profile: $profile\n";
	print $file_profile $profile;
	close $file_profile;
}

sub get_info {
	#default engine clock: 680000 kHz
	#current engine clock: 109680 kHz
	#default memory clock: 800000 kHz
	#current memory clock: 249750 kHz
	#voltage: 950 mV
	my $engine_clock;
	my $memory_clock;
	my $voltage;

	my $file_info;

	if (-e $INFO_FILE_PATH) {
		open ($file_info,  "< $INFO_FILE_PATH");
		while (<$file_info>) {
			if ($_ =~ /^current engine clock: (.*)/s) {
				$engine_clock = $1;
			}
			if ($_ =~ /^current memory clock: (.*)/s) {
				$memory_clock = $1;
			}
			if ($_ =~ /^voltage: (.*)/s) {
				$voltage = $1;
			}
		}
	}

	chomp $engine_clock;
	chomp $memory_clock;
	chomp $voltage;
	return {memory=>$memory_clock, engine=>$engine_clock, voltage=>$voltage};
}



