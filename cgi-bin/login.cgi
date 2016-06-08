#!perl

use strict;
use warnings;
use CGI;
use CGI::Session;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser); 
use XML::LibXML;
use Digest::SHA  qw(sha1 sha1_hex sha1_base64);

my $page = CGI->new;
my $session = CGI::Session->new( undef, $page, { Directory => '/tmp' } )
  or die CGI::Session->errstr;

require 'functions.pl';

my @controlli;
my @check;
print "Content-type: text/html\n\n";



sub printContenuto{

if($page->param("submit") || $page->param("submitR")){
	
	if($page->param("submit")){
		
		my $username = $page->param("username");
		if(!$username || !checkLogin($username,'user')){$check[0]="nv";}
		else{$check[0]="v";}
		
		my $password = $page->param("password");
		if(!$password || !checkLogin($username,'password',$password)){$check[1]="nv";}
		else{$check[1]="v";}
		
		my $size = @check;
		my $v=0;
		for (my $i=0; $i < $size; $i++){
			if($check[$i] eq "v"){$v=$v+1;}
		}
		if($v eq $size){
			my $log=&logged($session,$username,$password);
			if($log){
					$session->param(loggato => "loggato");$session->param( username => $username );
					$session->expire('+8h');$session->flush();
					print "<h2>Ti sei loggato!</h2><p>Sarai reindirizzato alla <span xml:lang='en'>Home page</span>.</p>
					<META HTTP-EQUIV=refresh CONTENT='1;URL=../cgi_bin/index.cgi'>\n";
			} 
		}
		else{
		print"<h2>Entra o registrati per accedere a più funzionalità</h2>
							<form class='formLogin' method='post' action='login.cgi' onsubmit='return login()'>
								<fieldset><legend><span xml:lang='en'>Login</span></legend>";
		if($check[0]eq "nv"){print "<label for='username' class='erroreInserimento'><span xml:lang='en'>Username</span> errato</label><input type='text' id='username'  name='username' value=\"$username\"/>";}
		else{print "<label for='username'><span xml:lang='en'><span xml:lang='en'>Username</span></span></label><input type='text' id='username'  name='username' value=\"$username\"/>";}
		
		if($check[1] eq "nv"){print "<label for='password' class='erroreInserimento'><span xml:lang='en'>Password</span> errata</label><input type='password' id='password'  name='password' value=\"$password\" />";}
		else{print "<label for='password'><span xml:lang='en'>Password</span></label><input type='password' id='password'  name='password' value=\"$password\"/>";}
		
		print "<input type='submit' name='submit' id='submit' value='Entra'/></fieldset></form>
						<form class='formLogin' method='post' action='login.cgi' onsubmit='return login()'>
			<fieldset>
				<legend>Registrazione</legend>
				<label for='nome'>Nome</label><input type='text' id='nome'  name='nome' />
				<label for='cognome'>Cognome</label><input type='text' id='cognome'  name='cognome' />
				<label for='nascita'>Anno di nascita</label><input type='text' id='nascita'  name='nascita' />
				<label for='usernameR'><span xml:lang='en'>Username</span></label><input type='text' id='usernameR'  name='usernameR' />
				<label for='emailUtente'><span xml:lang='en'>Email</span></label><input type='text' id='emailUtente'  name='emailUtente' />
				<label for='passwordR'><span xml:lang='en'>Password</span></label><input type='password' id='passwordR'  name='passwordR' />
				<label for='confermaPassword'>Conferma <span xml:lang='en'>password</span></label><input type='password' id='confermaPassword'  name='confermaPassword' />
				<input type='submit' name='submitR' id='submitR' value='Registrati'/>
			</fieldset>
		</form>";
		}
		
	}
	
	if($page->param("submitR")){
	
		#REGISTRAZIONE
		my $nome = $page->param("nome");
		if(!$nome){$controlli[0]="nv";}
		else{$controlli[0]="v";}
		
		my $cognome = $page->param("cognome");
		if(!$cognome){$controlli[1]="nv";}
		else{$controlli[1]="v";}
		
		my $nascita = $page->param("nascita");
		my $checkNascita=($nascita !=~ /\d{4}/);
		if(!$nascita || !$checkNascita){$controlli[2]="nv";}
		else{
		if($nascita<1916 || $nascita>2010){$controlli[2]="nv";}
		else{$controlli[2]="v";}
		}
		
		my $usernameR = $page->param("usernameR");
		if(!$usernameR || checkLogin($usernameR,'user')){$controlli[3]="nv";}
		else{$controlli[3]="v";}
		
		my $emailUtente = $page->param("emailUtente");
		my $checkEmail=($emailUtente =~m/^([\w\-\+\.]+)\@([\w\-\+\.]+)\.([\w\-\+\.]+)$/);
		if(!$emailUtente || !$checkEmail){$controlli[4]="nv";}
		else{$controlli[4]="v";}
		
		my $passwordR = $page->param("passwordR");
		if(!$passwordR){$controlli[5]="nv";}
		else{$controlli[5]="v";}		
		
		my $confermaPassword = $page->param("confermaPassword");
		if(!$confermaPassword || !($confermaPassword eq $passwordR)){$controlli[6]="nv";}
		else{$controlli[6]="v";}
		
		my $size = @controlli;
		my $v=0;
		for (my $i=0; $i < $size; $i++){
			if($controlli[$i] eq "v"){$v=$v+1;}
		}
		if($v eq $size){
			my $nodo="
				<utente>
					<user>".$usernameR."</user>
					<nome>".$nome."</nome>
					<cognome>".$cognome."</cognome>
					<annoNascita>".$nascita."</annoNascita>
					<mail>".$emailUtente."</mail>
					<password>".$passwordR."</password>
				</utente>";
				inserimentoSuXML($nodo,"utente");
				print "<h2>Ti sei registrato!</h2>
				<p>Effettua la <span xml:lang='en'>login</span> per avere accesso alla sezione riservata.</p>
				<form class='formLogin' method='post' action='login.cgi' onsubmit='return login()'>
			<fieldset>
				<legend><span xml:lang='en'>Login</span></legend>
				<label for='username'><span xml:lang='en'>Username</span></label><input type='text' id='username'  name='username' />
				<label for='password'><span xml:lang='en'>Password</span></label><input type='password' id='password'  name='password' />
				<input type='submit' name='submit' id='submit' value='Entra'/>
			</fieldset>
		</form>";
		
		}
			
		else{
			print"<h2>Entra o registrati per accedere a più funzionalità</h2>
					<form class='formLogin' method='post' action='login.cgi' onsubmit='return login()'>
					<fieldset>
						<legend><span xml:lang='en'>Login</span></legend>
						<label for='username'><span xml:lang='en'>Username</span></label><input type='text' id='username'  name='username' />
						<label for='password'><span xml:lang='en'>Password</span></label><input type='password' id='password'  name='password' />
						<input type='submit' name='submit' id='submit' value='Entra'/>
					</fieldset>
				</form>
				<form class='formLogin' method='post' action='login.cgi'>
					<fieldset>
					<legend>Registrazione</legend>";
			if($controlli[0]eq "nv"){print"<label for='nome' class='erroreInserimento'>Nome non inserito correttamente</label><input type='text' id='nome'  name='nome' value=\"$nome\" />";}
			else {print"<label for='nome'>Nome</label><input type='text' id='nome'  name='nome' value=\"$nome\" />";}
			
			if($controlli[1]eq "nv"){print"<label for='cognome' class='erroreInserimento'>Cognome non inserito correttamente</label><input type='text' id='cognome'  name='cognome' value=\"$cognome\" />";}
			else {print"<label for='cognome'>Cognome</label><input type='text' id='cognome'  name='cognome' value=\"$cognome\" />";}
		
			if($controlli[2]eq "nv"){print"<label for='nascita' class='erroreInserimento'>Inserire un anno di nascita corretto</label><input type='text' id='nascita' name='nascita' value=\"$nascita\" />";}
			else{print"<label for='nascita'>Anno di nascita</label><input type='text' id='nascita' name='nascita'  value=\"$nascita\" />";}
			
			if($controlli[3] eq "nv"){print "<label for='usernameR' class='erroreInserimento'><span xml:lang='en'>Username</span> non inserito o già in utilizzo</label><input type='text' id='usernameR'  name='usernameR' value=\"$usernameR\" />";}
			else{print"<label for='usernameR'><span xml:lang='en'>Username</span></label><input type='text' id='usernameR'  name='usernameR' value=\"$usernameR\"/>";}
			
			if($controlli[4] eq "nv"){print "<label for='emailUtente' class='erroreInserimento'>Inserire una <span xml:lang='en'>email</span> valida</label><input type='text' id='emailUtente'  name='emailUtente' value=\"$emailUtente\"/>";}
			else{print "<label for='emailUtente'><span xml:lang='en'>Email</span></label><input type='text' id='emailUtente'  name='emailUtente' value=\"$emailUtente\"/>";}
			
			if($controlli[5] eq "nv"){print "<label for='passwordR' class='erroreInserimento'><span xml:lang='en'>Password</span> non inserita correttamente</label><input type='password' id='passwordR'  name='passwordR' value=\"$passwordR\"/>";}
			else{print "<label for='passwordR'><span xml:lang='en'>Password</span></label><input type='password' id='passwordR'  name='passwordR' value=\"$passwordR\"/>";}
			
			if($controlli[6] eq "nv"){print "<label for='confermaPassword' class='erroreInserimento'><span xml:lang='en'>Password</span> e conferma <span xml:lang='en'>password</span> non coincidono</label><input type='password' id='confermaPassword'  name='confermaPassword' value=\"$confermaPassword\" />";}
			else{print "<label for='confermaPassword'>Conferma password</label><input type='password' id='confermaPassword'  name='confermaPassword' value=\"$confermaPassword\"/>";}
			
			print "<input type='submit' name='submitR' id='submitR' value='Registrati'/>
			</fieldset>
		</form>";
		}	
	}
	
	
	}
	else{
	print"<h2>Entra o registrati per accedere a più funzionalità</h2>
		<form class='formLogin' method='post' action='login.cgi' onsubmit='return login()'>
			<fieldset>
				<legend><span xml:lang='en'>Login</span></legend>
				<label for='username'><span xml:lang='en'>Username</span></label><input type='text' id='username'  name='username' />
				<label for='password'><span xml:lang='en'>Password</span></label><input type='password' id='password'  name='password' />
				<input type='submit' name='submit' id='submit' value='Entra'/>
			</fieldset>
		</form>
		<form class='formLogin' method='post' action='login.cgi' onsubmit='return registrazione()'>
			<fieldset>
				<legend>Registrazione</legend>
				<label for='nome' >Nome</label><input type='text' id='nome'  name='nome' />
				<label for='cognome'>Cognome</label><input type='text' id='cognome'  name='cognome' />
				<label for='nascita'>Anno di nascita</label><input type='text' id='nascita'  name='nascita' />
				<label for='usernameR'><span xml:lang='en'>Username</span></label><input type='text' id='usernameR'  name='usernameR' />
				<label for='emailUtente'><span xml:lang='en'>Email</span></label><input type='text' id='emailUtente'  name='emailUtente' />
				<label for='passwordR'><span xml:lang='en'>Password</span></label><input type='password' id='passwordR'  name='passwordR' />
				<label for='confermaPassword'>Conferma <span xml:lang='en'>password</span></label><input type='password' id='confermaPassword'  name='confermaPassword' />
				<input type='submit' name='submitR' id='submitR' value='Registrati'/>
			</fieldset>
		</form>";
	
	}
}

printHead('Login - Biblioteca di Portobuffolè','Login del sito della biblioteca comunale di Portobuffolè','login biblioteca Portobuffolè');

printBody("Login",$session);



	
