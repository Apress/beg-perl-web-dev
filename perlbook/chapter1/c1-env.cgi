#!/usr/bin/perl -T

use strict;
use CGI qw/:standard/;

print header,
start_html('Environment Variables');
foreach my $variable (keys %ENV) {
    print p("$variable is $ENV{$variable}");
}
print end_html;

exit; 

