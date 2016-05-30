function check_registrazione() {
  var nome = document.getElementById("nome").value;
  var cognome = document.getElementById("cognome").value;
  var giorno = document.getElementById("giorno").value;
  var mese = document.getElementById("mese").value;
  var anno = document.getElementById("anno").value;
  var e_mail = document.getElementById("email").value;
  var check_email = e_mail.search(/^([\w\-\+\.]+)@([\w\-\+\.]+).([\w\-\+\.])+$/);
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;
  var repeat_password = document.getElementById("repeat_password").value;

  if ((nome == '') || (nome == 'undefined')) {
    alert('campo NOME non può essere vuoto');
    document.getElementById('nome').focus();
  }
  if ((cognome == '') || (cognome == 'undefined')) {
    alert('campo COGNOME non può essere vuoto');
    document.getElementById('cognome').focus();
  }
  if (anno % 4 == 0) {
    if (mese == 'Feb') {
      if (giorno > 29) {
        alert('Febbraio negli anni bisestili non può avere più di 29 giorni');
        document.getElementById('giorno').focus();
      }
    } 
    else if ((mese == 'Apr') || (mese == 'Giu') || (mese == 'Set') || (mese == 'Nov')) {
      if (giorno == 31) {
        alert('Aprile, Giugno, Settembre e Novembre hanno 30 giorni ');
        document.getElementById('giorno').focus();
      }
    }
  } 
  else if (anno % 4 != 0) {
  	if(mese == 'Feb'){
    if (giorno > 28) {
      alert('Febbraio negli anni non bisestili non ha più di 28 giorni');
      document.getElementById('giorno').focus();
  	  }
    }
  	else if (mese == 'Apr' || mese == 'Giu' || mese == 'Set' || mese == 'Nov') {
   	 if (giorno == 31) {
    	  alert('Aprile, Giugno, Settembre e Novembre hanno 30 giorni ');
    	  document.getElementById('giorno').focus();
   	 }
  	}
  }
  if (check_email != 0) {
    alert('MAIL non valida');
    document.getElementById('email').focus();
  }
  if ((username == '') || (username == 'undefined')) {
    alert('campo USERNAME non può essere vuoto');
    document.getElementById('username').focus();
  }
  if (password != repeat_password) {
    alert('PASSWORD e REINSERISCI PASSWORD devono essere uguali');
    document.getElementById('repeat_password').focus();
  } 
  else if ((password == '') || (password == 'undefined')) {
    alert('campo PASSWORD non può essere vuoto');
    document.getElementById('password').focus();
  } 
  else if ((repeat_password == '') || (repeat_password == 'undefined')) {
    alert('campo REINSERISCI PASSWORD non può essere vuoto')
    document.getElementById('repeat_password').focus();
  }
  return false;
}


