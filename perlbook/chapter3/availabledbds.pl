#!/usr/bin/perl -T

use strict;
use DBI;

my @ary;
@ary = DBI->available_drivers;

foreach my $dbd (@ary) {
	print "$dbd driver is available\n";
}
