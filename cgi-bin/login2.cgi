#!perl

use strict;
use warnings;

use CGI::Session;
use CGI qw(:standard);

my $open = "1234";

my $page = CGI->new;
my $session = CGI::Session->new( undef, $page, { Directory => '/tmp' } )
  or die CGI::Session->errstr;
my $username = $page->param('username') // '';
my $password = $page->param('password') // '';

# Process Form
my @errors;
if ( $cgi->request_method eq 'POST' ) {
    if ( !$username ) {
        push @errors, "No username specified.";
    }

    if ( !$password ) {
        push @errors, "No password specified.";
    }
    elsif ( $password ne $open ) {
        push @errors, "Sorry, wrong password.";
    }

    if ( !@errors ) {
        $session->param( username => $username );
        print $page->redirect("indexx.cgi");
        exit;
    }
}

print $session->header(),
  start_html("Input Form"),
  start_form,
  p(
    "Please enter your username:",
    textfield(
        -name      => 'username',
        -maxlength => 20
    )
  ),
  p(
    "Please enter your password:",
    textfield(
        -name      => 'password',
        -maxlength => 20
    )
  ),
  p(submit), hr,
  end_form,
  map( { p( { -style => 'Color: red;' }, $_ ) } @errors ),
  end_html();