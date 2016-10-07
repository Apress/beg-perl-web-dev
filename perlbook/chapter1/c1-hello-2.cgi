#!/usr/bin/perl -T

use strict;
use CGI ':standard';

print header,
      start_html('Hello World'),
      h1('Hello World'),
      end_html();

exit;

