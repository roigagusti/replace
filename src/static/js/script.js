/*
* Title: Scripts
* Author: Aldasoro
* Template: Replace
* Version: 1.0
* Copyright 2023 Replace Inc.
* Url: https://www.replace.com
*/


// 1. Activar i desactivar botó registre
$(".input-settings").on('change', function() {
	$(".btn-cancel").removeClass("disabled");
	$(".btn-save").removeClass("disabled");
});
function termsChanged(){
	$(".btn-access").hasClass("disabled") ? $(".btn-access").removeClass("disabled") : $(".btn-access").addClass("disabled");
}

// 8. Amagar notifiació
$(document).ready(function(){
	setTimeout(function() {
		$("div.alert").removeClass("show");
	}, 5000);	
});