#!/usr/bin/perl -T

use strict;
use CGI qw/:standard/;
use CGI::Carp qw(fatalsToBrowser set_message);
set_message("This is a better message for the end.");


print header,
start_html("Testing CGI Carp");
die ("This is a test die");
print end_html;

exit;

