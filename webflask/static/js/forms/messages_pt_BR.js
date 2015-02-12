(function( factory ) {
	if ( typeof define === "function" && define.amd ) {
		define( ["jquery", "../jquery.validate"], factory );
	} else {
		factory( jQuery );
	}
}(function( $ ) {

/*
 * Translated default messages for the jQuery validation plugin.
 * Locale: PT (Portuguese; português)
 * Region: BR (Brazil)
 */
$.extend($.validator.messages, {

	required: "(Precisamos dessa informa&ccedil;&atilde;o)",
	email: "(Algo estranho nesse email)",
	number: "(S&oacute; n&uacute;meros)",
    range: $.validator.format("(Valores entre {0} e {1})"),
    max: $.validator.format("(Valor m&aacute;ximo &eacute; {0})"),
	min: $.validator.format("(Valor m&iacute;nimo &eacute; {0})"),

    url: "Por favor, forne&ccedil;a uma URL v&aacute;lida.",
    remote: "Por favor, corrija este campo.",
	date: "Por favor, forne&ccedil;a uma data v&aacute;lida.",
	dateISO: "Por favor, forne&ccedil;a uma data v&aacute;lida (ISO).",
	digits: "Por favor, forne&ccedil;a somente d&iacute;gitos.",
	creditcard: "Por favor, forne&ccedil;a um cart&atilde;o de cr&eacute;dito v&aacute;lido.",
	equalTo: "Por favor, forne&ccedil;a o mesmo valor novamente.",
	extension: "Por favor, forne&ccedil;a um valor com uma extens&atilde;o v&aacute;lida.",
	maxlength: $.validator.format("Por favor, forne&ccedil;a n&atilde;o mais que {0} caracteres."),
	minlength: $.validator.format("Por favor, forne&ccedil;a ao menos {0} caracteres."),
	rangelength: $.validator.format("Por favor, forne&ccedil;a um valor entre {0} e {1} caracteres de comprimento."),
	nifES: "Por favor, forne&ccedil;a um NIF v&aacute;lido.",
	nieES: "Por favor, forne&ccedil;a um NIE v&aacute;lido.",
	cifEE: "Por favor, forne&ccedil;a um CIF v&aacute;lido.",
	postalcodeBR: "Por favor, forne&ccedil;a um CEP v&aacute;lido."
});

}));