#!/usr/bin/perl -T

use strict;
use CGI qw/:standard/;

my $cookie = cookie(-name=>'testcookie',value=>'testcookievalue',expires=>'+7d');
print header (-cookie=>$cookie),
start_html('CGI Cookie Test'),
p("You've received a cookie\n"),
end_html;

exit;

