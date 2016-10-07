#!/usr/bin/perl -T

use strict;
use CGI qw/:standard/;
use CGI::Carp;

#croak "Croaking";
#confess "Confessing: $!";
carp "Carping";
warn "warning";
#die "dying";

print header;

exit;
