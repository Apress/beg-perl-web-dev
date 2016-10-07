#!/usr/bin/perl

use strict;
use CGI qw/:standard/;

print header;

if (param('color')) {
     print start_html('Hello'),
    "Hello ", param('name'),p,
    "Your favorite color is: ",param('color'),p,
    hr;
}
elsif (param('name')) {
    print start_html('Hello'),
   "Hello ",
    param('name'),
    p,
    start_form,
    "Please enter your favorite color: ",textfield('color'),
    hidden(-name=>'name',-value=>param('name')),
    submit,
    end_form,
    hr;
 else {
    print start_html('Hello'),
    start_form,
   "Enter your name: ",textfield('name'),
    submit,
    end_form,
    hr;
}

print end_html;

exit;

