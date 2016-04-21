function libri() {

var Rtitolo = document.getElementById("Rtitolo").value;
var Rautore = document.getElementById("Rautore").value;
var Rgenere = document.getElementById("Rgenere").value;

if (username == "" && Rautore=="" && Rgenere == "") {
	alert("Nessun campo inserito");
	document.getElementById("Rtitolo").focus();	
	}

return false;
}
