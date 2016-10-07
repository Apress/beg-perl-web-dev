#!/usr/bin/perl -T

use strict;
use CGI qw/:standard/;

my $name = param('name');
if ($name =~ /^([\w]+'?[\w]+)$/) {
	$name = $1;
} else {
	warn "Tainted data found in $name";
	$name = "";
}

print header,
start_html('Hello'),
start_form,
"Enter your name: ",textfield('name'),
submit,
end_form,
hr;

if (param()) {
    print "Hello $name",
    p;
}

print end_html;

exit;

