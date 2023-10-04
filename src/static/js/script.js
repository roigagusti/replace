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
var dropArea = document.getElementById('drop-area');
var fileInput = document.getElementById('fileinput');

['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
	dropArea.addEventListener(eventName, preventDefaults, false);
});
function preventDefaults(e) {
	e.preventDefault();
	e.stopPropagation();
}
['dragenter', 'dragover'].forEach(eventName => {
	dropArea.addEventListener(eventName, highlight, false);
});
['dragleave', 'drop'].forEach(eventName => {
	dropArea.addEventListener(eventName, unhighlight, false);
});
function highlight() {
	dropArea.classList.add('highlight');
}
function unhighlight() {
	dropArea.classList.remove('highlight');
}
dropArea.addEventListener('click', function() {
	fileInput.click();
});
dropArea.addEventListener('drop', handleDrop, false);
function handleDrop(e) {
	var file = e.dataTransfer.files[0];
	fileInput.files = e.dataTransfer.files;
	console.log(file.name);
	var dropArea = document.getElementById("drop-area");
	if (file.name.length > 20) {
	text = file.name.substring(0, 15) + "...";
	}else{
	text = file.name;
	}
	dropArea.innerText = text;
}
fileInput.addEventListener('change', handleFiles, false);
function handleFiles(e) {
	var files = e.target.files;
	for (var i = 0; i < files.length; i++) {
		var file = files[i];
		console.log(file.name);
		var dropArea = document.getElementById("drop-area");
		if (file.name.length > 20) {
		text = file.name.substring(0, 15) + "...";
		}else{
		text = file.name;
		}
		dropArea.innerText = text;
	}
}
$("#fileinput").change(function(){
	var inputHiddenValue = $(this).val();
	inputHiddenValue = inputHiddenValue.split('\\').pop();
	$("#drop-area").html(inputHiddenValue);
});

// 3. Afegir variables
var pairCounter = 4;
function addPair() {
	var newReplacePair = document.createElement('div');
	newReplacePair.classList.add('replace-pair');

	var inputReplace = document.createElement('input');
	inputReplace.type = 'text';
	inputReplace.classList.add('form-control', 'input-replace');
	inputReplace.placeholder = '*variable*';
	inputReplace.name = 'variable00' + pairCounter;

	var inputWith = document.createElement('input');
	inputWith.type = 'text';
	inputWith.classList.add('form-control', 'input-with');
	inputWith.placeholder = 'new content';
	inputWith.name = 'variable00' + pairCounter;

	newReplacePair.appendChild(inputReplace);
	newReplacePair.appendChild(inputWith);

	var container = document.querySelector('.pairs-container');
	container.appendChild(newReplacePair);
	pairCounter++;
}

// 8. Amagar notifiació
$(document).ready(function(){
	setTimeout(function() {
		$("div.alert").removeClass("show");
	}, 5000);	
});