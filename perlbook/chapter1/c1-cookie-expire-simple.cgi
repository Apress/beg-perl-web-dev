#!/usr/bin/perl -T

use strict;

my @monthnames = qw/Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec/;
my @weekdays = qw/Sunday Monday Tuesday Wednesday Thursday Friday Saturday/;

my $nextweek = time+604800;

my ($sec,$min,$hour,$mday,$mon,$year,$dayname,$dayofyear) = gmtime($nextweek);
$year += 1900;

print "Content-type: text/html\n";
print "Set-Cookie: testcookie=testcookievalue;";
printf ("expires=%s, %02d-%s-%d %02d:%02d:%02d GMT",$weekdays[$dayname],$mday,$monthnames[$mon],$year,$hour,$min,$sec);
print "\n\n";
print "You've received a cookie<p>\n";

exit;

