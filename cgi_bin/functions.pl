
my @pagine=(
	{
		nome => "Home",
		url => "../cgi_bin/index.cgi",
		lang => "en",
	},
	{
		nome => "Catalogo",
		url => "../cgi_bin/catalogo.cgi",
		lang => "it",
	},
	{
		nome => "Contatti",
		url => "../cgi_bin/contatti.cgi",
		lang => "it",
	},
	{
		nome => "Servizi",
		url => "../cgi_bin/servizi.cgi",
		lang => "it",
	},
	{
		nome => "Login",
		url => "../cgi_bin/login.cgi",
		lang => "it",
	},
	);



sub printHead{
$title=$_[0];
$description=$_[1];
$keywords=$_[2];

print"
<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Strict//EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd'>
<html xmlns='http://www.w3.org/1999/xhtml' xml:lang='it' lang='it'>
<head>
	<title>$title</title>
	<meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />
	<meta name='viewport' content='width=device-width, initial-scale=1.0'/>
	<meta name='title' content='$title' />
	<meta name='description' content='$description' />
	<meta name='keywords' content='$keywords' />
	<meta name='language' content='italian it' />
	<meta name='author' content='ideastudioweb' />
	<meta http-equiv='Content-Script-Type' content='text/javascript'/>
	<link href='../Public_html/style.css' rel='stylesheet' type='text/css' media='screen'/>
	<link rel='stylesheet' href='../Public_html/printstyle.css' type='text/css' media='print'/>	
	<link rel='stylesheet' href='../Public_html/mobilestyle.css' type='text/css' media='handheld, screen and (max-width:480px), only screen and (max-device-width:480px)'/>
	<link href='https://fonts.googleapis.com/css?family=Montserrat%7cMontserrat+Subrayada%7cIndie+Flower' rel='stylesheet' type='text/css' />
	<link href='https://fonts.googleapis.com/css?family=Fredoka+One%7cShadows+Into+Light+Two%7cCherry+Cream+Soda%7cCinzel+Decorative' rel='stylesheet' type='text/css' />
</head>
";
}



sub printHeader{
	print"<div id='header'>
		<img id='logo' src='../Public_html/resources/img/logo_comune.png' alt='logo comune di Portobuffole'/>			
		<div id='titolo'>
			<h1>Biblioteca di Portobuffolè</h1>
			<span id='infoLuogoHeader'>Comune di Portobuffolè (TV) - Piazza Vittorio Emanuele II, 31040</span>
			<span id='infoContattiHeader'>Telefono: 0422 850020 - email:</span>
		</div>
	</div>";
}

sub printMenu{
	my $pag=$_[0];
	my @pagine=@{$_[1]};

	print"<div id='menu'>
			<ul>";
	#			<li><span class='selected' xml:lang='en'>Home</span></li>
	#			<li><a href='catalogo.cgi' tabindex='1'>Catalogo</a></li>
	#			<li><a href='contatti.html' tabindex='2'>Contatti</a></li>	
	#			<li><a href='registrazione.html' tabindex='3'>Registrati</a></li>
	#			<li><a href='login.html' tabindex='4'>Entra</a></li>
	my $indexnum=1;
	for(my $zz=0;$zz<@pagine;$zz++) {
		my %p=%{$pagine[$zz]};
		my $nome=$p{nome};
		my $urlpag=$p{url};
		my $lingua=$p{lang};
		print "<li>";
		if($nome eq $pag){
			print "<span class='selected'";
			if(! $lingua eq "it" ){print " xml:lang=\"$lingua\"";}
			print ">$nome</span>";
		}
		else{
			print "<a href=\"$urlpag\" tabindex=\"$indexnum\"";
			$indexnum=$indexnum+1;
			if(! $lingua eq "it" ){print " xml:lang=\"$lingua\"";}
			print ">$nome</a>";
		}
		print "</li>";
	}
	print "</ul>
		</div>";

}

sub printFooter{
print"
<div id='footer'>
		<span id='infoFooter'>
			<span id='infoLuogo'>Comune di Portobuffolè (TV) - Piazza Vittorio Emanuele II, 31040</span>
			<span id='infoContatti'>Telefono: 0422 850020 - email:</span>
		</span>
</div>
";
}

sub printMain{
	my $pag=$_[0];
	print "<div id='main'>";
	printMenu($pag,\@pagine);
	print "<div id='contenuto'><span id='path'>Ti trovi in:";
	if($pag eq "Home"){
		print " <span xml:lang='en'>Home</span> ";
	}
	else{
		print" <span xml:lang='en'>Home &gt;&gt; $pag </span> ";
	}
	print "</span>";
	printContenuto();	
	print "</div></div>";
}


sub printBody{
	my $pag=$_[0];
	print "<body>";
	printHeader();
	printMain($pag);
	printFooter();
	print "</body></html>";
}

#my @controlli=(
#	{
#		parametro => "isbn",
#		expr => "\\d{3}-\\d{1,7}-\\d{1,7}-\\d{1,7}-\\d{1}",
#		valido => 1,
#		mex => "Inserire il corretto codice ISBN del libro (con i caratteri -)",
#	},
sub checkForm{	
	my $page=$_[0];
	my @controlli=@{$_[1]};

	my $validForm=1;
	for(my $zz=0;$zz<@controlli;$zz++) {
		my %p=%{$controlli[$zz]};
		my $nome=$p{parametro};
		my $expr=$p{expr};
		my $contenuto=$page->param($nome);
		my $vv=0;
		if($contenuto =~ /$expr/){$vv=1;}
		$validForm=($validForm * $vv);
		$controlli[$zz]{valido}=$vv;
		$controlli[$zz]{valore}=$contenuto;
	}
	return $validForm;
}

sub inserimentoSuXML{
my $valore=$_[0];
my $tipo=$_[1];#tipi: libro utente prenotazione prestito voto commento
my $isbn=$_[2];#solo per libri

my $fileNotizie="../data/dati.xml";
my $parser=XML::LibXML->new()||die("Errore nella creazione del parser");
my $doc=$parser->parse_file($fileNotizie)|| die("Errore nell'apertura del file xml");
my $radice=$doc->getDocumentElement();
$radice->setNamespace('http://www.bibliotecadiportobuffole.com','x');

utf8::decode($valore);
my $nodo=$parser->parse_balanced_chunk($valore);
my $padre=$radice;
if($tipo eq "libro"){$padre=$radice->findnodes("//x:Libri")->get_node(1);}
elsif($tipo eq "utente"){$padre=$radice->findnodes("//x:Utenti")->get_node(1);}
elsif($tipo eq "prenotazione"){$padre=$radice->findnodes("//x:Prenotazioni")->get_node(1);}
elsif($tipo eq "prestito"){$padre=$radice->findnodes("//x:Prestiti")->get_node(1);}
elsif($tipo eq "voto"){$padre=$radice->findnodes("//x:Voti")->get_node(1);}
elsif($tipo eq "commento"){$padre=$radice->findnodes("//x:Commenti")->get_node(1);}
$padre->appendChild($nodo);
open(OUT,">../data/dati.xml");
print OUT $doc->toString;
close(OUT);
}

sub login{
	my $session=$_[0];
	my $password=$_[1];
	$password=sha1($password);
	$session->param("password",$pass);
	$session->expire('+8h');
	$session->flush();
}


sub logged{
	my $session=$_[0];
	if($session->is_expired || $session->is_empty){return 0;}
	my $username=$session->param("username");
	my $password=$session->param("password");
	$password=sha1($password);
	my $file="../data/dati.xml";
	my $parser=XML::LibXML->new()||die("Errore nella creazione del parser");
	my $doc=$parser->parse_file($file)|| die("Errore nell'apertura del file xml");
	my $radice=$doc->getDocumentElement();
	$radice->setNamespace('http://www.bibliotecadiportobuffole.com','x');
	
	
	

	utf8::decode($username);
	my $user=$radice->findnodes("//u:utente[user=\"$username\"]")->get_node(1);
	
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


return 1;
