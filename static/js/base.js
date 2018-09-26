var id = "";
function ReproducirAlerta(e){
	var rep = new Audio();
	rep.src = "../static/sonidos/"+e+".mp3";
	rep.play();
};
function setModalAdvertencia(type, title, mensaje){
	ReproducirAlerta(type);
	$("#modalAdvertenciaTitle").text(title);
	$("#modalAdvertenciaMensaje").text(mensaje);
	$("#modalAdvertencia").modal('show');
};
function cerrarModal(){
	$('#modalAdvertencia').modal('hide');
	$("#"+focusId+"").focus();
}
function validar_fecha(id,nomb){
	var campo = document.getElementById(id).value;
	var letra = "";
	if (campo.length < 16) {
		setModalAdvertencia("Error","Error al Validar Fecha:","Mensaje: "+nomb+", NO Tiene el Formato Correcto: 'DD-MM-YYYY HH:Mi (24HH/AM-PM)'");
		letra = nomb+": "+campo.length;
	}
	return letra;
};
function validar_hora(id,nomb){
	var campo = document.getElementById(id).value;
	var letra = "";
	if (campo.length < 5) {
		setModalAdvertencia("Error","Error al Validar Hora:","Mensaje: "+nomb+", NO Tiene el Formato Correcto: 'HH:Mi (24HH/AM-PM)'");
		letra = nomb+": "+campo.length;
	}
	return letra;
};
function validar_number(id,nomb){
	var lista = ['1','2','3','4','5','6','7','8','9','0'];
	var campo = document.getElementById(id).value;
	var letra = "";
	for (x in campo) {
		if(!(lista.indexOf(campo[x]) > -1)){
			setModalAdvertencia("Error","Error al Validar Number:","Mensaje: "+nomb+", Tiene Caracteres NO Válidos: '"+campo[x]+"'");
			letra = nomb+": "+campo[x];
			break;
		}
	}
	return letra;
};
function validar_texto(id,nomb){
	var lista = ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L',
	'm','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z',
	'1','2','3','4','5','6','7','8','9','0','-','_','(',')','+','=',',',';','.',':','#',' ','\n'];
	var campo = document.getElementById(id).value;
	var letra = "";
	for (x in campo) {
		if(!(lista.indexOf(campo[x]) > -1)){
			setModalAdvertencia("Error","Error al Validar Texto:","Mensaje: "+nomb+", Tiene Caracteres NO Válidos: '"+campo[x]+"'");
			letra = nomb+": "+campo[x];
			break;
		}
	}
	return letra;
};