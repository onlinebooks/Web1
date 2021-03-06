#!/usr/bin/perl

use warnings;
use strict;
use CGI;
use CGI::Carp qw(fatalsToBrowser); 
use CGI::Session;

print "Content-type: text/html\n\n";

print<<EOF;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
<head>
	<title>Registrazione - Libronline</title>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
	<meta http-equiv="Content-Script-Type" content="text/javascript"/>
	<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
	<meta name="title" content="" />
	<meta name="description" content="Home page del sito del progetto" />
	<meta name="keywords" content="libraria Padova" />
	<meta name="language" content="italian it" />
	<meta name="author" content="root" />
	<link href="style.css" rel="stylesheet" type="text/css" media="screen"/>
	<link rel="stylesheet" href="printstyle.css" type="text/css" media="print"/>	
	<link rel="stylesheet" href="mobilestyle.css" type="text/css" media="handheld, screen and (max-width:480px), only screen and (max-device-width:480px)"/>
	<link href="https://fonts.googleapis.com/css?family=Montserrat%7cMontserrat+Subrayada%7cIndie+Flower" rel="stylesheet" type="text/css" />
	<link href="https://fonts.googleapis.com/css?family=Fredoka+One%7cShadows+Into+Light+Two%7cCherry+Cream+Soda%7cCinzel+Decorative" rel="stylesheet" type="text/css" />
	<script type="text/javascript" src="javascript/check_registrazione.js"></script>
</head>
<body>
	<div id="header">
		<span id="logo"></span>
		<h1> Libronline</h1>
		<h2> il tuo libro a portata di mano ovunque sei</h2>
	</div>
	<div id="main">
		<div id="menu">
			<ul>
				<li><a href="index.html" tabindex="0">Home</a></li>
				<li><a href="libri.html" tabindex="1">Libri</a></li>
				<li><a href="contatti.html" tabindex="2">Contatti</a></li>	
				<li>Registrati</li>
				<li><a href="login.html" tabindex="3">Entra</a></li>
			</ul>
		</div>
			<div id="contenuto">
			<div id="path">
				Ti trovi in: <a href="index.html" xml:lang="en">Home</a> » Registrati
			</div>
			<div id="centra">
				EOF

sub createSession() {
		$session = new CGI::Session();
		$session->param('pwd', $password);
}


sub getPwd() {
	$session = CGI::Session->load() or die $!;
	if ($session->is_expired || $session->is_empty ) {
		return undef;
		}	
 	else {
		my $pwd = $session->param('pwd');
		return $pwd;
		}
}

sub destroySession() {
$session = CGI::Session->load() or die $!;
$SID = $session->id();
$session->close();
$session->delete();
$session->flush();
}		

# modifica

$page = new CGI;
createSession();
$password=getPwd();

if(!$password){

	my $submit=$page->param('submit');  
	if($submit){
	
		$password=$page->param('pwd'); 
		if($password eq "admin"){
			print "<h1>BENVENUTO</h1>";
			}
		else
			{print "<h1>ERRORE</h1>";}
		}
		
	else{
	
print<<EOF;
				<h1>Iscriviti:</h1>
				<div class="form_interna">
				<form  action="" method="post" onsubmit="return check_registrazione()">
				 <fieldset>
				  <legend> Registrazione </legend>
					<p><span class="capo"> Nome: </span>
					<input name="nome" title="nome" type="text" id="nome"/>
					<span class="capo"> Cognome:</span>
					<input name="cognome" title="cognome" type="text" id="cognome"/>
					<span class="capo"> Data di nascita:</span>
					
					<select name="giorno" id="giorno">
						<option>1</option>
						<option>2</option>
						<option>3</option>
						<option>4</option>
						<option>5</option>
						<option>6</option>
						<option>7</option>
						<option>8</option>
						<option>9</option>
						<option>10</option>
						<option>11</option>
						<option>12</option>
						<option>13</option>
						<option>14</option>
						<option>15</option>
						<option>16</option>
						<option>17</option>
						<option>18</option>
						<option>19</option>
						<option>20</option>
						<option>21</option>
						<option>22</option>
						<option>23</option>
						<option>24</option>
						<option>25</option>
						<option>26</option>
						<option>27</option>
						<option>28</option>
						<option>29</option>
						<option>30</option>
						<option>31</option>
					</select>
				
					<select name="mese" id="mese">
						<option>Gen</option>
						<option>Feb</option>
						<option>Mar</option>
						<option>Apr</option>
						<option>Mag</option>
						<option>Giu</option>
						<option>Lug</option>
						<option>Ago</option>
						<option>Set</option>
						<option>Ott</option>
						<option>Nov</option>
						<option>Dic</option>
						</select>
						
					<select name="anno" id="anno">
						<option> 2015 </option>
						<option> 2014 </option>
						<option> 2013 </option>
						<option> 2012 </option>
						<option> 2011 </option>
						<option> 2010 </option>
						<option> 2009 </option>
						<option> 2008 </option>
						<option> 2007 </option>
						<option> 2006 </option>
						<option> 2005 </option>
						<option> 2004 </option>
						<option> 2003 </option>
						<option> 2002 </option>
						<option> 2001 </option>
						<option> 2000 </option>
						<option> 1999 </option>
						<option> 1998 </option>
						<option> 1997 </option>
						<option> 1996 </option>
						<option> 1995 </option>
						<option> 1994 </option>
						<option> 1993 </option>
						<option> 1992 </option>
						<option> 1991 </option>
						<option> 1990 </option>
						<option> 1989 </option>
						<option> 1988 </option>
						<option> 1987 </option>
						<option> 1986 </option>
						<option> 1985 </option>
						<option> 1984 </option>
						<option> 1983 </option>
						<option> 1982 </option>
						<option> 1981 </option>
						<option> 1980 </option>
						<option> 1979 </option>
						<option> 1978 </option>
						<option> 1977 </option>
						<option> 1976 </option>
						<option> 1975 </option>
						<option> 1974 </option>
						<option> 1973 </option>
						<option> 1972 </option>
						<option> 1971 </option>
						<option> 1970 </option>
						<option> 1969 </option>
						<option> 1968 </option>
						<option> 1967 </option>
						<option> 1966 </option>
						<option> 1965 </option>
						<option> 1964 </option>
						<option> 1963 </option>
						<option> 1962 </option>
						<option> 1961 </option>
						<option> 1960 </option>
						<option> 1959 </option>
						<option> 1958 </option>
						<option> 1957 </option>
						<option> 1956 </option>
						<option> 1955 </option>
						<option> 1954 </option>
						<option> 1953 </option>
						<option> 1952 </option>
						<option> 1951 </option>
						<option> 1950 </option>
						<option> 1949 </option>
						<option> 1948 </option>
						<option> 1947 </option>
						<option> 1946 </option>
						<option> 1945 </option>
						<option> 1944 </option>
						<option> 1943 </option>
						<option> 1942 </option>
						<option> 1941 </option>
						<option> 1940 </option>
						<option> 1939 </option>
						<option> 1938 </option>
						<option> 1937 </option>
						<option> 1936 </option>
						<option> 1935 </option>
						<option> 1934 </option>
						<option> 1933 </option>
						<option> 1932 </option>
						<option> 1931 </option>
						<option> 1930 </option>
						<option> 1929 </option>
						<option> 1928 </option>
						<option> 1927 </option>
						<option> 1926 </option>
						<option> 1925 </option>
						<option> 1924 </option>
						<option> 1923 </option>
						<option> 1922 </option>
						<option> 1921 </option>
						<option> 1920 </option>
						<option> 1919 </option>
						<option> 1918 </option>
						<option> 1917 </option>
						<option> 1916 </option>
						<option> 1915 </option>
						<option> 1914 </option>
						<option> 1913 </option>
						<option> 1912 </option>
						<option> 1911 </option>
						<option> 1910 </option>
						<option> 1909 </option>
						<option> 1908 </option>
						<option> 1907 </option>
						<option> 1906 </option>
						<option> 1905 </option>
						<option> 1904 </option>
						<option> 1903 </option>
						<option> 1902 </option>
						<option> 1901 </option>
					</select>
					
					<span class="capo"> E-mail:</span>
					<input name="e_mail" title="e-mail" type="text" id="email"/>
					<span class="capo"> Username:</span>
					<input name="username" title="username" type="text" id="username"/>
					<span class="capo"> Password:</span>
					<input name="password" title="password" type="password" id="password"/>
					<span class="capo"> Reinserisci Password:</span>
					<input name="password" title="password" type="password" id="repeat_password"/></p>
					<input type="submit" title="conferma" value="Conferma" name="conferma"/>
					<input type="reset" title="annulla" value="Annulla" name="annulla"/>
				 </fieldset>
				</form>
			EOF
	
	}
}

else{

	print "<h1>LOGGED</h1>";

}

print<<EOF;
			</div>
		</div>
		</div>
	</div>
	<div id="footer">
	via ugo bassi libreria libronline
	</div>
</body>
</html>
EOF
