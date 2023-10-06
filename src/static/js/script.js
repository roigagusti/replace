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

// 2. Drop area
// al arxiu templates/index.html

// 3. Afegir variables
function addPair(element){
	pairCounter = element.getAttribute('value');
	var newReplacePair = document.createElement('div');
	newReplacePair.classList.add('replace-pair');

	var inputReplace = document.createElement('input');
	inputReplace.type = 'text';
	inputReplace.classList.add('form-control', 'input-replace', 'input-add');
	inputReplace.placeholder = '*variable*';
	if (pairCounter < 10) {
		inputReplace.name = 'r_variable00' + pairCounter;
	}else if (pairCounter < 100) {
		inputReplace.name = 'r_variable0' + pairCounter;
	}else{
		inputReplace.name = 'r_variable' + pairCounter;
	}

	var inputWith = document.createElement('input');
	inputWith.type = 'text';
	inputWith.classList.add('form-control', 'input-with');
	inputWith.placeholder = 'new content';
	if (pairCounter < 10) {
		inputWith.name = 'w_variable00' + pairCounter;
	}else if (pairCounter < 100) {
		inputWith.name = 'w_variable0' + pairCounter;
	}else{
		inputWith.name = 'w_variable' + pairCounter;
	}

	newReplacePair.appendChild(inputReplace);
	newReplacePair.appendChild(inputWith);

	var container = document.querySelector('.pairs-container');
	container.appendChild(newReplacePair);

	var newValue = parseInt(pairCounter) + 1;
    element.setAttribute("value", newValue);
}

// 8. Amagar notifiació
$(document).ready(function(){
	setTimeout(function() {
		$("div.alert").removeClass("show");
	}, 5000);	
});