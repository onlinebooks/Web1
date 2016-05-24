
#------------------------------------------
# login(session,string) :void
# logout() :void
# salvaPass(string) :void
# logged() :bool
#-----------------------------------------

use CGI::Session;
use Digest::SHA  qw(sha1 sha1_hex sha1_base64);
#use Digest::SHA1  qw(sha1 sha1_hex sha1_base64);
require "Amm-news.pl";

sub login{
my $session=$_[0];
my $pass=$_[1];
$pass=sha1($pass);
$session->param("password",$pass);
$session->expire('+8h');
$session->flush();
}


sub logged{
my $session=$_[0];
if($session->is_expired || $session->is_empty){return 0;}
my $vv=$session->param("password");
$vv=sha1($vv);
my $pass="";
open(FILE,"<../data/accesso.txt");
while(!eof(FILE)){
	my $line=<FILE>;
	if($pass eq ""){$pass=$line;}
	else{$pass=$pass."\n".$line;}
	}
close FILE;
if($vv eq $pass){return 1;}
return 0;
}

sub logout{
my $session=$_[0];
$session->param("password","");
$session->close();
$session->delete();
$session->flush();
}

sub cambiaPass{
my $page=$_[0];
my $session=$_[1];
my $old=sha1($page->param("oldpass"));
my $n=$page->param("newpass");
my $rep=$page->param("repass");
if(($old eq $session->param("password")) && length($n)>0 && ($n eq $rep)){
	&salvaPass($n);
	$session->param("password",sha1($n));
	&headerAmministratore();
	print "<div><h1>Cambio Password</h1><p>La password &egrave; stata cambiata.</p>
	<a href=\"Amministratore.cgi\" title=\"ritorna alla pagina di amministrazione\">Back</a></div>";
	&footerAmministratore();
	}
else{
	my %err={};
	$err{"oldpassErrata"}=(!($old eq $session->param("password")));
	$err{"newpassErrata"}=(!(length($n)>0));
	$err{"repassErrata"}=(!($n eq $rep));
	&stampaAmministratore(\%err);
	}
}


sub salvaPass{
	my $pass=$_[0];
	$pass=sha1($pass);
	$pass=sha1($pass);
	open(FILE,">../data/accesso.txt");
	print FILE $pass;
	close FILE;
}

sub loginForm{
my $err=$_[0];
print<<EOF
<?xml version="1.0" encoding="UTF-8"?> 
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
	<link rel="stylesheet" href="../style.css" type="text/css" />
	<title>Amministrazione - IDEA Studio Web</title>
	<link href="https://fonts.googleapis.com/css?family=Montserrat%7cMontserrat+Subrayada%7cIndie+Flower" rel="stylesheet" type="text/css" />
	 <link rel="icon" href="../resources/favicon.gif" type="image/gif" />
	<meta name="author" content="cesco" />
	<meta name="description" content="Area di amministrazione" />
	<meta name="robots" content="noindex" />
	<script src="../javascript/menu-responsive.js" type="text/javascript"></script>
</head>

<body id="amministrazione" onload="abilitamenu();">

<div id="header">

	<div id="path">Ti trovi in: <a href="../index.html" xml:lang="en" title="vai alla home">Home</a> &gt;&gt; Amministrazione</div>
	
	<div id="nav">
	
	<div id="logo">
				<a href="../index.html" accesskey="g" tabindex="0" title="vai alla home">IDEA <span>Studio Web</span></a>
			</div>	
	
	<div id="menu">
		
		<ul id="nav-menu">
			<li><a href="../index.html" title="vai alla home" xml:lang="en" tabindex="1">Home</a></li>	
			<li><a href="../work.html" title="vai alla sezione work" xml:lang="en" tabindex="2">Work</a></li>
			<li><a href="feedback.cgi" title="vai alla sezione feedback" xml:lang="en" tabindex="3">Feedback</a></li>
			<li><a href="news.cgi" title="vai alla sezione news" xml:lang="en" tabindex="4">News</a></li>
			<li><a href="../contatti.html" title="vai alla sezione contatti" tabindex="5">Contatti</a></li>		
			<li><a href="../listino.html" title="vai alla sezione listino" tabindex="6">Listino</a></li>		
					
		</ul>
	</div>
	</div> 
	
</div>

<div id="main">



<h1>Accesso amministratori</h1>

<form id="loginForm" action="Amministratore.cgi" method="post">
<fieldset><legend>Login</legend>
<label for="password">Password</label>
<input type="password" id="password" $err name="password"/>
<input type="submit" name="submit" id="submit" value="login"/>
</fieldset>
</form>

</div><!-- fine del main -->
<!-- inizio footer -->
	<div id="footer">
		<p>Via Ugo Bassi, Padova, Italia - Telefono: 049 1234728 - E-mail: studioideaweb\@gmail.com</p>



  <p>
    <a href="http://validator.w3.org/check?uri=referer"><img
      src="http://www.w3.org/Icons/valid-xhtml10" alt="Valid XHTML 1.0 Strict" height="31" width="88" /></a>
  </p>
  

	</div>
	<!-- fine footer -->

</body>
</html>

EOF

}

sub stampaAmministratore{
my %err=%{$_[0]};
my $page=$_[1];

&headerAmministratore();

print '<div id="ammNotizie">';
&nuovaNews();
print '<hr class="divis"/>';
&stampaModificaNews();
print "</div>";

print '<hr class="divis"/>';
&cancellaFeedback($page);


print '<hr class="divis"/><div id="ammAccesso">
<h1>Cambia password</h1>
<form action="Amministratore.cgi" method="post">
<fieldset><legend>Cambia password</legend>
<label for="oldpass">Vecchia Password</label>
<input type="password" name="oldpass" id="oldpass" ';

if($err{"oldpassErrata"}){print "class=\"invalid\"";}

print ' /><br/>
<label for="newpass">Nuova Password</label>
<input type="password" name="newpass" id="newpass" ';
if($err{"newpassErrata"}){print "class=\"invalid\"";}
print ' /><br/>
<label for="repass">Ripeti password</label>
<input type="password" name="repass" id="repass" ';
if($err{"repassErrata"}){print "class=\"invalid\"";}
print ' /><br/>
<input type="submit" name="cambiapass" id="cambiapass" value="Cambia"/>
</fieldset>
</form>
</div>';

&footerAmministratore();

}

sub headerAmministratore{
print <<EOF
<?xml version="1.0" encoding="UTF-8"?> 
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
	<link rel="stylesheet" href="../style.css" type="text/css" />
	<title>Amministrazione - IDEA Studio Web</title>
	<link href="https://fonts.googleapis.com/css?family=Montserrat%7cMontserrat+Subrayada%7cIndie+Flower" rel="stylesheet" type="text/css" />
	 <link rel="icon" href="../resources/favicon.gif" type="image/gif" />
	<meta name="author" content="Francesco" />
	<meta name="description" content="Area di amministrazione" />
	<meta name="robots" content="noindex" />
</head>

<body id="amministrazione">

<div id="header">

	<div id="path">Ti trovi nella zona di Amministrazione</div>
	
	<div id="nav">
	
	<div id="logo">
				<a href="../index.html" title="link alla home">IDEA <span>Studio Web</span></a>
			</div>	
	
		<a id="logout" href="Amministratore.cgi?logout=logout" title="esegui il logout">LOGOUT</a>
	
	</div> 
	
</div>

<div id="main">
EOF

}

sub footerAmministratore{
print<<EOF

</div><!-- fine del main -->
<!-- inizio footer -->
	<div id="footer">
		<p>Via Ugo Bassi, Padova, Italia - Telefono: 049 1234728 - E-mail: studioideaweb\@gmail.com</p>
  

	</div>
	<!-- fine footer -->

</body>
</html>

EOF

}

return true;
