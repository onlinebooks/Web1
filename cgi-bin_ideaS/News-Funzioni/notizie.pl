
#------------------------------------------
#	stampaNotizie()
#	stampaNotizia()
#	mostraDettagli()
#	stampaNotizieAnno()
#------------------------------------------


sub sdata{
my $d=$_[0];
my $s=substr $d,0,4;
$s=$s.(substr $d,5,2);
$s=$s.(substr $d,8,2);
return $s;
}


sub stampaNotizie{
#CREA L'ELENCO DI NOTIZIE DELLA PAGINA PRINCIPALE
	my $radice=$_[0];
	my @elNotizie=sort{&sdata($b->getAttribute("data")) <=> &sdata($a->getAttribute("data"))}$radice->getElementsByTagName("notizia");

	print "	<div id=\"presentazione\">
			<h1 id=\"h1-news\">Notizie Recenti</h1>
		</div><div id=\"contenitoreNews\"><dl>";

	for($i=0;$i<10 && $i<@elNotizie.length();$i++){
		&stampaNotizia($elNotizie[$i]);
		#if($i<9 && $i<@elNotizie.length()-1){print "<div class=\"separatoreN\"></div>";}
		}
		
	print<<EOF
			
	</dl>
	<a href="#ricerca" class="scomparsa" title="vai alla funzionalità di ricerca">Cerca notizie meno recenti</a>
	</div>
EOF
}

sub stampaNotizia{
#CREA IL CODICE HTML DI UNA NOTIZIA PER LA FUNZIONE stampaNotizie
	my $notizia=$_[0];
	if(defined $notizia){
	my $idNews=$notizia->getAttribute("id");
	my $data=$notizia->getAttribute("data");
	my @dataG=split "-", $data;
	$data=$dataG[2]."/".$dataG[1]."/".$dataG[0];
	my $titolo=$notizia->getElementsByTagName("titolo")->get_node(1)->textContent();
	utf8::encode($titolo);
	my $copertinaSrc=$notizia->getElementsByTagName("copertina")->get_node(1);
	if($copertinaSrc){
		$copertinaSrc=$copertinaSrc->getAttribute("src");
		utf8::encode($copertinaSrc);}
	my $copertinaAlt=$notizia->getElementsByTagName("copertina")->get_node(1);
	if($copertinaAlt){
		$copertinaAlt=$copertinaAlt->getAttribute("alt");
		utf8::encode($copertinaAlt);}
	my @paragrafi=$notizia->getElementsByTagName("riassunto")->get_node(1)->getChildnodes();
	#inserire gestione copertina e valuta se mettere span per data anzichè div
	print "<dt class=\"titoloNews\">$titolo</dt>
	<dd class=\"news\">";
	
	if($copertinaSrc){
	print "<img class=\"nascosto\" id=\"copertina$idNews\" src=\"$copertinaSrc\" alt=\"$copertinaAlt\" />";
	}

	print "<div class=\"data\">$data</div>
	<div id=\"notizia$idNews\">";

	foreach my $p(@paragrafi){
	my $para=$p->toString();
	utf8::encode($para);
	print $para;
	}

	@paragrafi=$notizia->getElementsByTagName("testo")->get_node(1)->getChildnodes();

	my $testo="";
	foreach my $para(@paragrafi){
		my $parat=$para->toString();
		utf8::encode($parat);
		$testo=$testo.$parat;
		}

	print "<a href=\"news.cgi?dettagli=$idNews\" title=\"mostra il testo completo della notizia $idNews\" 
	onclick=\"dettagliNews(\'$idNews\');return false;\">Leggi di più</a></div>
	<div id=\"dettagli$idNews\" class=\"nascosto\">$testo</div>
	</dd>";
	}
}

sub mostraDettagli{
#MOSTRA IL TESTO ESTESO DI UNA NOTIZIA (PRENDE IN INPUT L'ID E LA RADICE DEL DOCUMENTO XML)
	my $id=$_[0];
	my $radice=$_[1];
	$radice->setNamespace('http://www.IDEAStudioWeb.com','x');
	my $notizia=$radice->findnodes("//x:notizia[\@id=\"$id\"]")->get_node(1);
	my $data=$notizia->getAttribute("data");
	my @dataG=split "-", $data;
	$data=$dataG[2]."/".$dataG[1]."/".$dataG[0];
	my $titolo=$notizia->getElementsByTagName("titolo")->get_node(1)->textContent();
	utf8::encode($titolo);
	my @paragrafi=$notizia->getElementsByTagName("testo")->get_node(1)->getChildnodes();
	my $copertinaSrc=$notizia->getElementsByTagName("copertina")->get_node(1);
	if($copertinaSrc){
		$copertinaSrc=$copertinaSrc->getAttribute("src");
		utf8::encode($copertinaSrc);}
	my $copertinaAlt=$notizia->getElementsByTagName("copertina")->get_node(1);
	if($copertinaAlt){
		$copertinaAlt=$copertinaAlt->getAttribute("alt");
		utf8::encode($copertinaAlt);}

	print "<div id=\"contenitoreNews\">
	<h3 class=\"titoloNews\">$titolo</h3>
	<div class=\"news\">";
	
	if($copertinaSrc){
	print "<img class=\"picNotizia\" id=\"copertina$idNews\" src=\"$copertinaSrc\" alt=\"$copertinaAlt\" />";
	}	

	print "<div class=\"data\">$data</div>";
	
	foreach my $p(@paragrafi){
	my $para=$p->toString();
	utf8::encode($para);
	print $para;
	}
			
	print "</div><a href=\"news.cgi\" title=\"Torna all'elenco delle ultime notizie\">Torna alle notizie</a></div>";
}

sub stampaNotizieAnno{
	my $anno=$_[0];
	my $radice=$_[1];
	$radice->setNamespace('http://www.IDEAStudioWeb.com','x');
	my @notizie=$radice->findnodes("//x:notizia[contains(\@data,\"$anno\")]");
	
	print "	<div id=\"presentazione\">
			<h1 id=\"h1-news\">Notizie del $anno</h1></div>";

	if(@notizie.length()==0){
		print "<div id=\"contenitoreNews\">
	<p class=\"news\">Nessuna notizia è stata pubblicata nel $anno</p>
	<p class=\"news\"><a href=\"news.cgi\" title=\"Torna all'elenco delle ultime notizie\">Torna alle ultime notizie</a></p></div>";
	}
	else{
	print "<div id=\"contenitoreNews\"><dl>";
	foreach my $n(sort{&sdata($b->getAttribute("data"))<=>&sdata($a->getAttribute("data"))}@notizie){
		&stampaNotizia($n);
		}

	print "</dl><a href=\"news.cgi\" title=\"Torna all'elenco delle ultime notizie\">Torna alle ultime notizie</a></div>";
	}
}

return 1;
