#!/usr/bin/perl -T

use strict;
use CGI qw/:standard/;

my $cookie = cookie(-name=>'testcookie',value=>'testvalue');
print header (-cookie=>$cookie);
print "You've received a cookie<p>\n";

exit;

