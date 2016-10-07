#!/usr/bin/perl -T

use strict;
use CGI qw/:standard/;

my $retrievedcookie = cookie('testcookie');

print header,
start_html,
p("You sent a cookie and its value was $retrievedcookie\n"),
end_html;

exit;

