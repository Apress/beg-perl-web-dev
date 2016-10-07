#!/usr/bin/perl -T

use strict;
use CGI qw/:standard/;

my $retrievedcookie = cookie('testcookie');
my $retrievedcookie2 = cookie('secondcookie');

print header,
start_html,
p("You sent a couple cookies and their values were $retrievedcookie and $retrievedcookie2\n"),
end_html;

exit;
