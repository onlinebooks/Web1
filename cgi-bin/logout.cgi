#!/usr/bin/perl

use CGI;
use CGI::Carp qw(fatalsToBrowser); 
use CGI::Session;
use CGI qw(:standard);
use XML::LibXML;
use Digest::SHA  qw(sha1 sha1_hex sha1_base64);

require 'functions.pl';
my $page = CGI->new;
my $session = CGI::Session->new( undef, $page, { Directory => '/tmp' } )
  or die CGI::Session->errstr;
 $session->param("loggato","");
$session->param("username","");
$session->close();
$session->delete();


#&logout($session);

print $page->redirect("index.cgi");
