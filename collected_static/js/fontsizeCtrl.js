'use strict';
var device_width=window.outerWidth;
var device_heigth=window.outerHeight;
var strong_ctrl=document.getElementsByTagName('strong');
// var strong_ctrl;
for (var i=0; i<strong_ctrl.length; i++){
	// strong_ctrl=li_ctrl[0].getElementsByTagName('*');
	if(device_width<700){
		strong_ctrl[i].style.fontSize='13px';
	}
	else{
		strong_ctrl[i].style.fontSize='26px';	
	}
	// alert(strong_ctrl[0].style.fontFamily);
}