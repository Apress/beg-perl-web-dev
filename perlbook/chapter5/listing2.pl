#!/usr/bin/perl

use LWP;

$browser = LWP::UserAgent->new(agent => 'Perly v1');
$result = $browser->get("http://www.braingia.org/ewfojwefoj");
die "An error occured: ", $result->status_line( ) unless $result->is_success;

#Do something more meaningful with the content than this!
print $result->content; 

exit;
