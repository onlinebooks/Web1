#!/usr/bin/perl

use CGI;
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use Digest::SHA  qw(sha1 sha1_hex sha1_base64);

require "login-utils.pl";
require "Amm-news.pl";

my $page=new CGI;
my $session=CGI::Session->new($page);
print $session->header();

my $digitata=$page->param("password");

if($digitata){
&login($session,$digitata);
}
if($page->param("logout") eq "logout"){&logout($session);}

my $log=&logged($session);


if(!$log){
#pagina di login
my $err="";
if($digitata){$err="class=\"invalid\"";}
&loginForm($err);
}else{
#pagina Amministratore

if($page->param("cambiapass") eq "Cambia"){&cambiaPass($page,$session);}
elsif($page->param("submitn") eq "Pubblica notizia"){&inserimentoNews($page);}
elsif($page->param("cercaN") eq "Cerca"){&cercaDataMod($page->param("cercaData"));}
elsif($page->param("modN") eq "Modifica"){&Modform($page->param("idn"));}
elsif($page->param("modificaNdaid")){&Modform($page->param("modificaNdaid"));}
elsif($page->param("submitnMod") eq "Modifica notizia"){&inserisciModifiche($page);}
elsif($page->param("cancellaN") eq "Cancella"){&cancella($page->param("idcn"),1);}
else{&stampaAmministratore(null,$page);}

}



