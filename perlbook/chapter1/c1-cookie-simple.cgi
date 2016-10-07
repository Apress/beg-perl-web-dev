#!/usr/bin/perl -T

use strict;

print "Content-type: text/html\n";
print "Set-Cookie: testcookie=testvalue;";
print "\n\n";
print "You've received a cookie<p>\n";

exit;

