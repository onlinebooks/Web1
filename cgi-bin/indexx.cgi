#!perl

use strict;
use warnings;

use CGI::Session;
use CGI qw(:standard);

my $page = CGI->new;
my $session = CGI::Session->new( undef, $page, { Directory => '/tmp' } )
  or die CGI::Session->errstr;

my $username = $session->param('username');

print header,
  start_html( -BGCOLOR => 'green' ),
  p("Hello, $username"), p( "The time now is: ", scalar(localtime) ),
  end_html;

