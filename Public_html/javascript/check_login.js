function check_login() {

var username = document.getElementById("username").value;
var password = document.getElementById("password").value;

if (username == "" || username == "undefined") {
	alert("USERNAME non corretto o vuoto");
	document.getElementById("username").focus();	
	}

if (password == "" || password == "undefined") {
	alert("PASSWORD non corretta o vuota")
	document.getElementById("password").focus();
}

return false;
}
