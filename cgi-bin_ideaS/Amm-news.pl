
#-------------------------------------------
#
#------------------------------------------

use XML::LibXML;
use Time::localtime;
require "login-utils.pl";


sub nuovaNews{
my $data=localtime->mday();
my $mese=localtime->mon()+1;
if($mese<10){$mese="0".$mese;}
$data=$data."/".$mese;
$data=$data."/".(localtime->year()+1900);
print<<EOF

<div id="nuovaNews">
<h1>Inserimento notizia</h1>
<form action="Amministratore.cgi" method="post">
<fieldset><legend>Nuova notizia</legend>
<label for="datan">Data</label>
<input type="text" id="datan" name="datan" value="$data"/><br/>
<label for="titolo">Titolo</label>
<input type="text" id="titolo" name="titolo"/><fieldset><legend>Immagine (facoltativa)</legend>
<label for="copertina">Imm. copertina</label>
<input type="file" id="copertina" name="copertina" accept="image/*"/><br/>
<label for="copertinaAlt">Descrizione immagine</label>
<input type="text" id="copertinaAlt" name="copertinaAlt"/>
</fieldset>
<label for="testo">Contenuto (inserire anche eventuali tag html)</label>
<textarea id="testo" name="testo" rows="20" cols="80"></textarea><br/>
<label for="riassunto">Riassunto (inserire anche eventuali tag html)</label>
<textarea id="riassunto" name="riassunto" rows="5" cols="80"></textarea><br/>
<input type="submit" name="submitn" id="submitn" value="Pubblica notizia"/>
</fieldset>
</form>
</div>
EOF

}


sub inserimentoFisico{
my $data=$_[0];
my $titolo=$_[1];
my $copertina=$_[2];
my $alt=$_[3];
my $contenuto=$_[4];
my $riassunto=$_[5];

my $fileNotizie="../data/news.xml";
my $parser=XML::LibXML->new()||die("Errore nella creazione del parser");
my $doc=$parser->parse_file($fileNotizie)|| die("Errore nell'apertura del file xml");
my $radice=$doc->getDocumentElement();
$radice->setNamespace('http://www.IDEAStudioWeb.com','x');

my $id=$radice->findnodes("(//\@id[not(. < //\@id)])[1]")->get_node(1)->value;
$id=$id+1;
my $anno=substr $data,6,4;
my $mese=substr $data,3,2;
my $giorno=substr $data,0,2;
my $notizia="<notizia id=\"$id\" data=\"$anno-$mese-$giorno\"><titolo>$titolo</titolo>";
if($copertina){$notizia=$notizia."<copertina src=\"../resources/$copertina\" alt=\"$alt\" />";}
$notizia=$notizia."<testo>$contenuto</testo><riassunto>$riassunto</riassunto></notizia>";
utf8::encode($notizia);
my $nodo=$parser->parse_balanced_chunk($notizia);
$radice->appendChild($nodo);
open(OUT,">../data/news.xml");
print OUT $doc->toString;
close(OUT);
}

sub inserimentoNews{
my $page=$_[0];
my $data=$page->param("datan");
#utf8::encode($data);
my $titolo=$page->param("titolo");
#utf8::encode($titolo);
my $copertina=$page->param("copertina");
#utf8::encode($copertina);
my $contenuto=$page->param("testo");
#utf8::encode($contenuto);
my $riassunto=$page->param("riassunto");
#utf8::encode($copertina);
my $alt=$page->param("copertinaAlt");
#utf8::encode($alt);

my $ckdata=$data=~m/^([0123][0123456789]\/[01][0123456789]\/2[01][0123456789][0123456789])$/;
my $cktitolo=$titolo=~m/^(.{3,})$/;
my $ckcopertina=$copertina=~m/^((.{1,}\.jpg)?)$/;
my $ckcontenuto=$contenuto=~m/^(.{1,})$/;
my $ckriassunto=$riassunto=~m/^(.{1,})$/;
my $ckalt=1;
if(length($copertina)>3){$ckalt=$alt=~m/^(.{1,})$/;}

if($ckdata && $cktitolo && $ckcopertina && $ckcontenuto && $ckriassunto && $ckalt){
	#inserimento

	&inserimentoFisico($data,$titolo,$copertina,$alt,$contenuto,$riassunto);

	&headerAmministratore();	
	print "<div id='ammNotizieInsN'>
	<h1>Inserimento notizia</h1><p>Notizia memorizzata con successo!</p>
	<a href='Amministratore.cgi'>BACK</a></div>";
	&footerAmministratore();
	}
else{
	&headerAmministratore();
	print "<div id='ammNotizie'><div id=\"nuovaNews\">
<h1>Inserimento notizia</h1>
<form action=\"Amministratore.cgi\" method=\"post\">
<fieldset><legend>Nuova notizia</legend>";

if($ckdata){
	print "<label for=\"datan\">Data</label>
	<input type=\"text\" id=\"datan\" name=\"datan\" value=\"$data\"/>";
}
else{
	print "<label for=\"datan\" class=\"erroreForm\">Inserire una data: gg/mm/aaaa</label>
	<input type=\"text\" id=\"datan\" name=\"datan\" />";
}

if($cktitolo){
	print "<br/><label for=\"titolo\">Titolo</label>";	
	print "<input type=\"text\" id=\"titolo\" name=\"titolo\" value=\"$titolo\"/>"
}
else{
	print "<br/><label for=\"titolo\" class=\"erroreForm\">Inserire un titolo con almeno 3 caratteri</label>";
	print "<input type=\"text\" id=\"titolo\" name=\"titolo\" />";
}
print "<fieldset><legend>Immagine (facoltativa)</legend>";
if($ckcopertina){
	print "<label for=\"copertina\">Imm. copertina</label>";
	print "<input type=\"file\" id=\"copertina\" name=\"copertina\" value=\"$copertina\" accept=\"image/*\"/>";
}
else{
	print "<label for=\"copertina\" class=\"erroreForm\">Inserire un file jpg o lasciare vuoto</label>";
	print "<input type=\"file\" id=\"copertina\" name=\"copertina\" accept=\"image/*\" />";
}
if($ckalt){
	print "<br/><label for=\"copertinaAlt\">Descrizione immagine</label>
<input type=\"text\" id=\"copertinaAlt\" name=\"copertinaAlt\"value=\"$alt\"/>";
}
else{
	print "<label for=\"copertinaAlt\" class=\"erroreForm\">Descrizione immagine (almeno 1 carattere)</label> 
<input type=\"text\" id=\"copertinaAlt\" name=\"copertinaAlt\"/>";
}
print "</fieldset>";
if($ckcontenuto){
	print "<label for=\"testo\">Contenuto (inserire anche eventuali tag html)</label>";
	print "<textarea id=\"testo\" name=\"testo\" rows=\"20\" cols=\"80\">$contenuto</textarea>";
}
else{
	print "<label for=\"testo\" class=\"erroreForm\">Contenuto (almeno 1 carattere)</label>";
	print "<textarea id=\"testo\" name=\"testo\" rows=\"20\" cols=\"80\">$contenuto</textarea>";
}
if($ckriassunto){
	print "<br/><label for=\"riassunto\">Riassunto (inserire anche eventuali tag html)</label>
	<textarea id=\"riassunto\" name=\"riassunto\" rows=\"5\" cols=\"80\">$riassunto</textarea><br/>";
}
else{
	print "<br/><label for=\"riassunto\" class=\"erroreForm\">Riassunto (almeno 1 carattere)</label>
	<textarea id=\"riassunto\" name=\"riassunto\" rows=\"5\" cols=\"80\">$riassunto</textarea><br/>";
}
print "<input type=\"submit\" name=\"submitn\" id=\"submitn\" value=\"Pubblica notizia\"/>
</fieldset>
</form>
</div></div>";
	&footerAmministratore();
	}

}

sub stampaModificaNews{


print<<EOF

<div id="modificaNews">
<h1>Modifica notizia</h1>
<form action="Amministratore.cgi" method="post">
<fieldset><legend>Modifica notizia</legend>
<fieldset><legend>Cerca per data</legend>
<label for="cercaData">Data</label>
<input type="text" name="cercaData" id="cercaData"/>
<input type="submit" name="cercaN" id="cercaN" value="Cerca"/>
</fieldset><fieldset><legend>Cerca per ID</legend>
<label for="idn">ID notizia</label>
<input type="text" name="idn" id="idn"/>
<input type="submit" name="modN" id="modN" value="Modifica"/>
</fieldset>
</fieldset>
</form>
</div>
EOF

}

sub cercaDataMod{
my $data=$_[0];
if($data=~m/^([0123][0123456789]\/[01][0123456789]\/2[01][0123456789][0123456789])$/){
	my $anno=substr $data,6,4;
	my $mese=substr $data,3,2;
	my $giorno=substr $data,0,2;
	$data=$anno.'-'.$mese.'-'.$giorno;
	my $fileNotizie="../data/news.xml";
	my $parser=XML::LibXML->new()||die("Errore nella creazione del parser");
	my $doc=$parser->parse_file($fileNotizie)|| die("Errore nell'apertura del file xml");
	my $radice=$doc->getDocumentElement();
	$radice->setNamespace('http://www.IDEAStudioWeb.com','x');
	my @nodi=$radice->findnodes("//x:notizia[\@data=\"$data\"]");
	if(@nodi.length()>0){
		&headerAmministratore();
print "<div id=\"ammNotizie\"><div id=\"modificaNews\"><h1>Seleziona la notizia da modificare</h1><ul>";
foreach my $n(@nodi){
	my $titolo=$n->getElementsByTagName("titolo")->get_node(1)->textContent();
	#utf8::encode($titolo);
	my $id=$n->getAttribute("id");
	print "<li><a href=\"Amministratore.cgi?modificaNdaid=$id\">$titolo</a></li>";
}
print "</ul></div><a href='Amministratore.cgi'>BACK</a></div>";
		&footerAmministratore();
		}else{
		&headerAmministratore();	
		print "<div id='ammNotizieInsN'>
		<h1>Cerca notizia</h1><p>Non &egrave; stata trovata alcuna notizia pubblicata in data $giorno\/$mese\/$anno.</p>
		<a href='Amministratore.cgi'>BACK</a></div>";
		&footerAmministratore();
		}
}else{
&headerAmministratore();
print '<div id="ammNotizie"><div id="modificaNews">
<h1>Modifica notizia</h1>
<form action="Amministratore.cgi" method="post">
<fieldset><legend>Modifica notizia</legend>
<fieldset><legend>Ricerca ID</legend>
<label for="cercaData" class="erroreForm">Cerca per data (inserire data gg/mm/aaaa)</label>
<input type="text" name="cercaData" id="cercaData"/>
<input type="submit" name="cercaN" id="cercaN" value="Cerca"/>
</fieldset>
<label for="idn">ID notizia</label>
<input type="text" name="idn" id="idn"/>
<input type="submit" name="modN" id="modN" value="Modifica"/>
</fieldset>
</form>
</div><a href="Amministratore.cgi">BACK</a></div>';
&footerAmministratore();
}
}

sub Modform{
my $id=$_[0];
if($id=~m/^(\d{1,})$/){
#caricamento file xml
	my $fileNotizie="../data/news.xml";
	my $parser=XML::LibXML->new()||die("Errore nella creazione del parser");
	my $doc=$parser->parse_file($fileNotizie)|| die("Errore nell'apertura del file xml");
	my $radice=$doc->getDocumentElement();
	$radice->setNamespace('http://www.IDEAStudioWeb.com','x');
	my $nodo=$radice->findnodes("//x:notizia[\@id=\"$id\"]")->get_node(1);
	if($nodo){
		my $data=$nodo->getAttribute("data");
		my @dataG=split "-", $data;
		$data=$dataG[2]."/".$dataG[1]."/".$dataG[0];
		my $titolo=$nodo->getElementsByTagName("titolo")->get_node(1)->textContent();
		utf8::decode($titolo);
		my $testo=join("",$nodo->getElementsByTagName("testo")->get_node(1)->getChildnodes);
		utf8::decode($testo);
		my $riassunto=join('',$nodo->getElementsByTagName("riassunto")->get_node(1)->getChildnodes);
		utf8::decode($riassunto);
		my $copertina=$nodo->getElementsByTagName("copertina")->get_node(1);
		my $copertinaSrc="";
		my $copertinaAlt="";
		if($copertina){
			$copertinaSrc=$copertina->getAttribute("src");
			utf8::decode($copertinaSrc);
			$copertinaAlt=$copertina->getAttribute("alt");
			utf8::decode($copertinaAlt);
			}
		&headerAmministratore();
print "<div id='ammNotizie'><div id='modificaNews'>
<h1>Modifica notizia $id</h1>
<form action=\"Amministratore.cgi\" method=\"post\">
<fieldset><legend>Modifica notizia</legend>
<label for=\"dataMod\">Data</label>
<input type=\"text\" id=\"dataMod\" name=\"dataMod\" value=\"$data\"/><br/>
<label for=\"titoloMod\">Titolo</label>
<input type=\"text\" id=\"titoloMod\" value=\"$titolo\" name=\"titoloMod\"/>
<fieldset><legend>Immagine (facoltativa)</legend>
<label for=\"copertinaMod\">Imm. copertina</label>
<input type=\"text\" id=\"copertinaMod\" name=\"copertinaMod\" value=\"$copertinaSrc\" /><br/>
<label for=\"copertinaAltMod\">Descrizione immagine</label>
<input type=\"text\" id=\"copertinaAltMod\" name=\"copertinaAltMod\" value=\"$copertinaAlt\"/>
</fieldset>
<label for=\"testoMod\">Contenuto (inserire anche eventuali tag html)</label>
<textarea id=\"testoMod\" name=\"testoMod\" rows=\"20\" cols=\"80\">$testo</textarea><br/>
<label for=\"riassuntoMod\">Riassunto (inserire anche eventuali tag html)</label>
<textarea id=\"riassuntoMod\" name=\"riassuntoMod\" rows=\"5\" cols=\"80\">$riassunto</textarea><br/>
<input type='text' name='idMod' id='idMod' value=\"$id\" hidden='hidden'/>
<input type=\"submit\" name=\"submitnMod\" id=\"submitnMod\" value=\"Modifica notizia\"/>
</fieldset>
</form><h1>Cancella notizia $id</h1>
<form action='Amministratore.cgi' method='post'><fieldset><legend>Cancella notizia</legend>
<input type='text' name='idcn' id='idcn' value=\"$id\" hidden='hidden'/>
<input type='submit' name='cancellaN' id='cancellaN' value='Cancella'/><label for='cancellaN'>Cancella la notizia $id</label></fieldset></form>
<a href='Amministratore.cgi'>BACK</a>
</div></div>";
		&footerAmministratore();
	}else{
		&headerAmministratore();	
		print "<div id='ammNotizieInsN'>
		<h1>Modifica notizia</h1><p>Non &egrave; stata trovata alcuna notizia avente id=$id.</p>
		<a href='Amministratore.cgi'>BACK</a></div>";
		&footerAmministratore();
	}
}else{
&headerAmministratore();
print '<div id="ammNotizie"><div id="modificaNews">
<h1>Modifica notizia</h1>
<form action="Amministratore.cgi" method="post">
<fieldset><legend>Modifica notizia</legend>
<fieldset><legend>Ricerca ID</legend>
<label for="cercaData">Cerca per data</label>
<input type="text" name="cercaData" id="cercaData"/>
<input type="submit" name="cercaN" id="cercaN" value="Cerca"/>
</fieldset>
<label for="idn" class="erroreForm">ID notizia (deve essere un numero)</label>
<input type="text" name="idn" id="idn"/>
<input type="submit" name="modN" id="modN" value="Modifica"/>
</fieldset>
</form>
</div><a href="Amministratore.cgi">BACK</a></div>';
&footerAmministratore();
}

}

sub cancella{
my $id=$_[0];
my $Stampa=$_[1];
my $fileNotizie="../data/news.xml";
my $parser=XML::LibXML->new()||die("Errore nella creazione del parser");
my $doc=$parser->parse_file($fileNotizie)|| die("Errore nell'apertura del file xml");
my $radice=$doc->getDocumentElement();
$radice->setNamespace('http://www.IDEAStudioWeb.com','x');
my $nodo=$radice->findnodes("//x:notizia[\@id=$id]")->get_node(1);
my $padre=$nodo->parentNode;
$padre->removeChild($nodo);
open(OUT,">../data/news.xml");
print OUT $doc->toString;
close(OUT);

if($Stampa){
&headerAmministratore();	
print "<div id='ammNotizieInsN'>
<h1>Cancellazione notizia</h1><p>Notizia cancellata con successo!</p>
<a href='Amministratore.cgi'>BACK</a></div>";
&footerAmministratore();}
}

sub inserisciModifiche{
my $page=$_[0];

my $data=$page->param("dataMod");
my $titolo=$page->param("titoloMod");
#utf8::encode($titolo);
my $copertina=$page->param("copertinaMod");
#utf8::encode($copertina);
my $contenuto=$page->param("testoMod");
#utf8::encode($contenuto);
my $riassunto=$page->param("riassuntoMod");
#utf8::encode($riassunto);
my $alt=$page->param("copertinaAltMod");
#utf8::encode($alt);
my $id=$page->param("idMod");

my $ckdata=$data=~m/^([0123][0123456789]\/[01][0123456789]\/2[01][0123456789][0123456789])$/;
my $cktitolo=$titolo=~m/^(.{3,})$/;
my $ckcopertina=$copertina=~m/^((.{1,}\.jpg)?)$/;
my $ckcontenuto=$contenuto=~m/^(.{1,})$/;
my $ckriassunto=$riassunto=~m/^(.{1,})$/;
my $ckalt=1;
if(length($copertina)>3){$ckalt=$alt=~m/^(.{1,})$/;}

if($ckdata && $cktitolo && $ckcopertina && $ckcontenuto && $ckriassunto && $ckalt){

	&cancella($id,0);
	&inserimentoFisico($data,$titolo,$copertina,$alt,$contenuto,$riassunto);

	&headerAmministratore();	
	print "<div id='ammNotizieInsN'>
	<h1>Modifica notizia</h1><p>Notizia modificata con successo!</p>
	<a href='Amministratore.cgi'>BACK</a></div>";
	&footerAmministratore();
	}
else{
	&headerAmministratore();
	print "<div id='ammNotizie'><div id=\"modificaNews\">
<h1>Modifica notizia</h1>
<form action=\"Amministratore.cgi\" method=\"post\">
<fieldset><legend>Modifica notizia</legend>";

if($ckdata){
	print "<label for=\"dataMod\">Data</label>
	<input type=\"text\" id=\"dataMod\" name=\"dataMod\" value=\"$data\"/>";
}
else{
	print "<label for=\"dataMod\" class=\"erroreForm\">Inserire una data: gg/mm/aaaa</label>
	<input type=\"text\" id=\"dataMod\" name=\"dataMod\" />";
}

if($cktitolo){
	print "<br/><label for=\"titoloMod\">Titolo</label>";	
	print "<input type=\"text\" id=\"titoloMod\" name=\"titoloMod\" value=\"$titolo\"/>"
}
else{
	print "<br/><label for=\"titoloMod\" class=\"erroreForm\">Inserire un titolo con almeno 3 caratteri</label>";
	print "<input type=\"text\" id=\"titoloMod\" name=\"titoloMod\" />";
}
print "<fieldset><legend>Immagine (facoltativa)</legend>";
if($ckcopertina){
	print "<label for=\"copertinaMod\">Imm. copertina</label>";
	print "<input type=\"text\" id=\"copertinaMod\" name=\"copertinaMod\" value=\"$copertina\"/>";
}
else{
	print "<label for=\"copertinaMod\" class=\"erroreForm\">Inserire un file jpg o lasciare vuoto</label>";
	print "<input type=\"text\" id=\"copertinaMod\" name=\"copertinaMod\" />";
}
if($ckalt){
	print "<br/><label for=\"copertinaAltMod\">Descrizione immagine</label>
<input type=\"text\" id=\"copertinaAltMod\" name=\"copertinaAltMod\"value=\"$alt\"/>";
}
else{
	print "<label for=\"copertinaAltMod\" class=\"erroreForm\">Descrizione immagine (almeno 1 carattere)</label> 
<input type=\"text\" id=\"copertinaAltMod\" name=\"copertinaAltMod\"/>";
}
print "</fieldset>";
if($ckcontenuto){
	print "<label for=\"testoMod\">Contenuto (inserire anche eventuali tag html)</label>";
	print "<textarea id=\"testoMod\" name=\"testoMod\" rows=\"20\" cols=\"80\">$contenuto</textarea>";
}
else{
	print "<label for=\"testoMod\" class=\"erroreForm\">Contenuto (almeno 1 carattere)</label>";
	print "<textarea id=\"testoMod\" name=\"testoMod\" rows=\"20\" cols=\"80\">$contenuto</textarea>";
}
if($ckriassunto){
	print "<br/><label for=\"riassuntoMod\">Riassunto (inserire anche eventuali tag html)</label>
	<textarea id=\"riassuntoMod\" name=\"riassuntoMod\" rows=\"5\" cols=\"80\">$riassunto</textarea><br/>";
}
else{
	print "<br/><label for=\"riassuntoMod\" class=\"erroreForm\">Riassunto (almeno 1 carattere)</label>
	<textarea id=\"riassuntoMod\" name=\"riassuntoMod\" rows=\"5\" cols=\"80\">$riassunto</textarea><br/>";
}
print "<input type='text' name='idMod' id='idMod' value=\"$id\" hidden='hidden'/>
<input type=\"submit\" name=\"submitnMod\" id=\"submitnMod\" value=\"Modifica notizia\"/>
</fieldset></form><h1>Cancella notizia $id</h1><form action='Amministratore.cgi' method='post'><fieldset><legend>Cancella notizia</legend>
<input type='text' name='idcn' id='idcn' value=\"$id\" hidden='hidden'/>
<input type='submit' name='cancellaN' id='cancellaN' value='Cancella'/><label for='cancellaN'>Cancella la notizia $id</label></fieldset></form>
<a href='Amministratore.cgi'>BACK</a></div></div>";
	&footerAmministratore();
	}


}


# FEEDBACK 

sub cancellaFeedback{

my $page=$_[0];
my $file='../data/commenti.xml';
my $parser=XML::LibXML->new();

my $doc=$parser->parse_file($file);

my $radice=$doc->getDocumentElement;
$radice->setNamespace('http://www.ideastudioweb.com','x');
my @values = $page->param('feed[]'); 

my $size=scalar @values;
if($size>0){
		for($i=0;$i<$size;$i++){
			foreach my $s($doc->findnodes('//x:listaTestimonianze/singolaTestimonianza')){
			my $c = $s->getElementsByTagName('Commento');
    			utf8::encode($n);
			if($c eq @values[$i]){
				my $r=$s->parentNode;
				$r->removeChild($s);
				}
				}
			}
 		open(OUT,">$file");
		print OUT $doc->toString;
		close(OUT);

}


print'

<div id="modificaFeedback">
<h1>Cancella Feedback</h1>
<form action="Amministratore.cgi" method="post">
<fieldset><legend>Elenco Feedback</legend>';

my @array=$doc->findnodes('//x:listaTestimonianze/singolaTestimonianza');
my $size2=scalar @array;

if($size2>0){
foreach my $singoloCommento($doc->findnodes('//x:listaTestimonianze/singolaTestimonianza')) {
	
    my $comm = $singoloCommento->getElementsByTagName('Commento');
    utf8::decode($comm);
	
    my $length = 30;
    my $fragment =  substr $comm, 0, $length;	
	
    $fragment=$fragment."...";
   print "<input type='checkbox' name='feed[]' id='feed-adm' value='$comm'/> $fragment <br /> ";


  }

print<<EOF;

<input type="submit" name="submit-feedback" id="submit-adm" value="Elimina"/>

EOF

}

else  {print"Nessun commento presente";}

print<<EOF

</fieldset>
</form>
</div>

EOF

}




return true;
