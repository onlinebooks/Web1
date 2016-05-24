
#------------------------------------------------------
#	ricerca()
#	[TF()]
#	casellaRicerca()
#------------------------------------------------------


sub ricerca{
#CERCA LE NOTIZIE SULLA BASE DI UNA QUERY PASSATA IN INPUT
#si usa la funzione TF-IDF per valutare l'attinenza delle notizie alle keywords
my $q=$_[0];

$q=lc($q);
my $radice=$_[1];
my @keywords=split(" ",$q);
my @notizie=$radice->getElementsByTagName("notizia");

#calcolo IDF
my %idf=();
foreach my $keyw(@keywords){
	my $idfgrezzo=0;
	my $numDoc=0;
	foreach my $notiz(@notizie){
		$numDoc=$numDoc+1;
		my $testo=$notiz->toString();
		utf8::encode($testo);
		$testo=lc($testo);
		if(index($testo,$keyw)!=-1){
			$idfgrezzo+=1;
			}
		}
	if(!$idfgrezzo){$idfgrezzo=1;}
	$idfgrezzo=$numDoc/$idfgrezzo;
	$idf{$keyw}=2*log($idfgrezzo);
	}


#calcolo valutazioni
my %voti=();
foreach my $notiz(@notizie){
	my $voto=0;
	foreach my $k(@keywords){
		my $tfval=&TF($notiz,$k);
		$voto=$voto+($tfval*$idf{$k});
		}
	my $ii=$notiz->getAttribute("id");
	$voti{$ii}=$voto;
	#print "[$ii] ";
	}
my @risultato=();
my $maxVoto = 0;
foreach my $idn(sort{$voti{$b} <=> $voti{$a} } keys %voti){
	my $val=$voti{$idn};
	if($maxVoto==0){$maxVoto=$val;}
	if($val>$maxVoto){$maxVoto=$val;}
	if($val>0){		
		my $notiz=&getNotiziaDaId($idn,$radice);		
		push @risultato,$notiz;
		}
	}


print "	<div id=\"presentazione\">
			<h1 id=\"h1-news\">Risultati ricerca</h1>
		</div>";

if($maxVoto==0){
	print "<div id=\"contenitoreNews\">
	<p class=\"news\">Nessuna notizia trovata in relazione alla query \"$q\"</p>
	<p class=\"news\"><a href=\"news.cgi\" title=\"torna all'elenco delle ultime notizie\">Torna alle ultime notizie</a></p></div>";
	}
else{
	print "<div id=\"contenitoreNews\"><dl>";
	foreach my $n(@risultato){
		&stampaNotizia($n);
		}
	print "</dl><a href=\"news.cgi\" title=\"torna all'elenco delle ultime notizie\">Torna alle ultime notizie</a>
	</div>";
	}

}

sub getNotiziaDaId{
my $id=$_[0];
my $radice=$_[1];
$radice->setNamespace('http://www.IDEAStudioWeb.com','x');
my $notizia=$radice->findnodes("//x:notizia[\@id=\"$id\"]")->get_node(1);
return $notizia;
}


sub TF{
my $notizia=$_[0];
my $keyword=$_[1];
my $testo=$notizia->toString();
utf8::encode($testo);
$testo=lc($testo);
my @parole=split(" ",$testo);
my $tf=0;
foreach my $parola(@parole){
	my $simile=(length($keyword)>4);
	$simile=$simile && (index($parola,$keyword)!=-1);
	if($parola eq $keyword){$tf+=2;}
	elsif($simile){$tf+=1;}
	}
return $tf;
}

sub casellaRicerca{
#CREA IL CODICE HTML DELLA COLONNA DI RICERCA
	my $annocorrente=localtime;
	$annocorrente=$annocorrente->year+1900;
	my $cercaAnni="";
	#formato: <li><a href="">Notizie del 2013</a></li>

	for(my $i=0;$i<4 && $annocorrente-$i>=2014;$i++){
	#2014 è anno della notizia più vecchia
		$anno=$annocorrente-$i;
		$cercaAnni.="<li><a href=\"news.cgi?anno=$anno\" title=\"cerca le notizie del $anno\">Notizie del $anno</a></li>"
		}

	print<<EOF

<div id="ricerca">
		
			<h2 class="titolo-news">Archivio</h2>
			<a href=\"#header\" class=\"navigazione\" title=\"torna a inizio pagina\">torna a inizio pagina</a>
			
			<p>Puoi trovare tutte le notizie da noi pubblicate nel tempo, sfruttando la 
			funzionalità di ricerca per keywords o l'elenco annuale sottostante.</p>
			
			<form id="ricercaNews" action="news.cgi" method="get">
			<fieldset>
				<legend>Ricerca per keywords</legend>
				<label for="queryNews" id="labelRicerca">Query:</label>
				<input type="text" name="queryNews" id="queryNews" />
				<input type="submit" name="cerca" id="cerca" value="Cerca" />			
			</fieldset>
			</form>
			
			<ol id="ricercaData">
				$cercaAnni					
			</ol>			
			
	</div>	
EOF
}

return 1;
