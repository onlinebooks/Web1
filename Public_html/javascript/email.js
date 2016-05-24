function Email() {
  var email=document.getElementById("email").value;
  var oggetto = document.getElementById("oggetto").value;
  var messaggio = document.getElementById("messaggio").value;
  var controllo_email = email.search(/^([\w\-\+\.]+)@([\w\-\+\.]+).([\w\-\+\.])+$/);

  if (controllo_email != 0) {
   alert("campo EMAIL non valido");
   document.getElementById("email").focus();
	}
  if ((oggetto == "") || (oggetto == "undefined")) {
    alert("campo OGGETTO non valido");
    document.getElementById("oggetto").focus();
  }
  if ((messaggio == "") || (messaggio == "undefined")) {
    alert("campo MESSAGGIO non valido");
    document.getElementById("messaggio").focus();
  }
  else {
    location.href = "mailto:studioideaweb@gmail.com" + email + "?Subject=" + oggetto + "&Body=" + messaggio; 
  }
  return false
}
