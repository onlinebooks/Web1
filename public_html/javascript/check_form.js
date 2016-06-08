function contatti(){
		
		var n=document.querySelector("label[for='nome']");
		n.innerHTML="Nome";
		n.className="";
		var e=document.querySelector("label[for='email']");
		e.innerHTML="Email";
		e.className="";
		var m=document.querySelector("label[for='messaggio']");
		m.innerHTML="Messaggio";
		m.className="";
		
		var nome=document.getElementById("nome");
		var email=document.getElementById("email");
		var messaggio=document.getElementById("messaggio");
	
		var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
		
		var be=false;
		var bo=false;
		var bm=false;


		if (email.value=="" || !reg.test(email.value)){
				
				e.innerHTML="Inserire una <span xml:lang='en'>email</span>valida";
				e.className="erroreInserimento";
				be=true;	
			}
		

		if (nome.value==""){
		
				n.innerHTML="Nome non inserito correttamente";
				n.className="erroreInserimento";
				
				bo=true;
			}

		if (messaggio.value==""){
		
				m.innerHTML="Messaggio non inserito correttamente";
				m.className="erroreInserimento";
				bm=true;
			}
		if(be || bo || bm)
			return false;

		else return true;
}

function login(){
		var u=document.querySelector("label[for='username']");
		u.innerHTML="Username";
		u.className="";
		var p=document.querySelector("label[for='password']");
		p.innerHTML="Password";
		p.className="";
		var username=document.getElementById("username");
		var password=document.getElementById("password");
		var be=false;
		var bo=false;
		if (username.value==""){
		
				u.innerHTML="<span xml:lang='en'>Username</span> errato";
				u.className="erroreInserimento";
				
				be=true;
			}
		if (password.value==""){
		
				p.innerHTML="<span xml:lang='en'>Password</span> errata";
				p.className="erroreInserimento";
				
				bo=true;
			}
		if(be || bo )
			return false;

		else return true;
		
}

function registrazione(){
		var n=document.querySelector("label[for='nome']");
		n.innerHTML="Nome";
		n.className="";
		
		var c=document.querySelector("label[for='cognome']");
		c.innerHTML="Cognome";
		c.className="";
		
		var nn=document.querySelector("label[for='nascita']");
		nn.innerHTML="Anno di nascita";
		nn.className="";
		
		var u=document.querySelector("label[for='usernameR']");
		u.innerHTML="Username";
		u.className="";
		
		var e=document.querySelector("label[for='emailUtente']");
		e.innerHTML="Email";
		e.className="";
		
		var p=document.querySelector("label[for='passwordR']");
		p.innerHTML="Password";
		p.className="";
				
		var cp=document.querySelector("label[for='confermaPassword']");
		cp.innerHTML="Conferma password";
		cp.className="";
		
		var nome=document.getElementById("nome");
		var cognome=document.getElementById("cognome");
		var nascita=document.getElementById("nascita");
		var username=document.getElementById("usernameR");
		var email=document.getElementById("emailUtente");
		var password=document.getElementById("passwordR");
		var confermaPassword=document.getElementById("confermaPassword");

		
		
		
		var bn=false;
		var bc=false;
		var bnn=false;
		var bu=false;
		var be=false;
		var bp=false;
		var bcp=false;
		var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
		var reg2=/^\d{4}$/;
		
		if (nome.value==""){
		
				n.innerHTML="Nome non inserito correttamente";
				n.className="erroreInserimento";
				
				bn=true;
			}
		
		if (cognome.value==""){
		
				c.innerHTML="Cognome non inserito correttamente";
				c.className="erroreInserimento";
				
				bc=true;
			}
		
		if (nascita.value=="" || !reg2.test(nascita.value)){
		
				nn.innerHTML="Inserire un anno di nascita corretto";
				nn.className="erroreInserimento";
				
				bnn=true;
			}
		
		if(reg2.test(nascita.value)){
				if(nascita.value < 1916 || nascita.value > 2010 ){
					nn.innerHTML="Inserire un anno di nascita corretto";
					nn.className="erroreInserimento";
				
					bnn=true;
				}
			
		}
			
		if (username.value==""){
		
				u.innerHTML="<span xml:lang='en'>Username</span> non inserito o già in utilizzo";
				u.className="erroreInserimento";
				
				bu=true;
			}
			
		if (email.value=="" || !reg.test(email.value)){
		
				e.innerHTML="Inserire una <span xml:lang='en'>email</span> valida";
				e.className="erroreInserimento";
				
				be=true;
			}
			
		if (password.value==""){
		
				p.innerHTML="<span xml:lang='en'>Password</span> non inserita correttamente";
				p.className="erroreInserimento";
				
				bp=true;
			}
			
		if (confermaPassword.value=="" || confermaPassword.value!= password.value){
		
				cp.innerHTML="<span xml:lang='en'>Password</span> e conferma <span xml:lang='en'>password</span> non coincidono";
				cp.className="erroreInserimento";
				
				bcp=true;
			}
			

		if(bn || bc || bnn || bu || be || bp || bcp )
			return false;

		else return true;
	
}
