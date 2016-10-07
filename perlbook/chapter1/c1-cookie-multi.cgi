#!/usr/bin/perl -T

use strict;
use CGI qw/:standard/;

my $cookie = cookie(-name=>'testcookie',value=>'testcookievalue',expires=>'+7d');
my $cookie2 = cookie(-name=>'secondcookie',value=>'secondcookievalue',expires=>'+1d');
print header (-cookie=>[$cookie,$cookie2]),
start_html('CGI Cookie Test'),
p("You've received a cookie\n"),
end_html;

exit;

