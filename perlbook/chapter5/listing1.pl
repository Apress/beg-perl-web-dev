#!/usr/bin/perl

use LWP::Simple;

$webpage = get("http://www.braingia.org/");

if (grep {/Steve/} $webpage) {
	print "I found the text\n";
}
