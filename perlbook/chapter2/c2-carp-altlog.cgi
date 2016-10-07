#!/usr/bin/perl -T

use strict;
use CGI qw/:standard/;

BEGIN {
	use CGI::Carp qw(carpout);
	open ('ERRORLOG', ">>/home/user/logs/cgierrors.log") or
		die("Unable to open log file: $!\n");
	carpout('ERRORLOG');
}

print header,
start_html("Testing CGI Carp");
warn ("This is a test warning");
print p("Hello, this is a test, check the logfile"),
end_html;

exit;
