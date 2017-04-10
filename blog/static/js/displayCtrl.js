'use strict';
var device_width=window.outerWidth;//outerWidth和outerHeight属性,可以获取浏览器窗口的整个宽高
// var device_heigth=window.outerHeight;//innerWidth和innerHeight属性，可以获取浏览器窗口的内部宽度和高度。
// 内部宽高是指除去菜单栏、工具栏、边框等占位元素后，用于显示网页的净宽高
var strong_ctrl=document.getElementsByTagName('strong');//设定在小屏幕(<700px)和大屏幕Home，Blog的大小
for (var i=0; i<strong_ctrl.length; i++){//对Home，Blog大小控制
	// strong_ctrl=li_ctrl[0].getElementsByTagName('*');
	if(device_width<700){
		strong_ctrl[i].style.fontSize='13px';
	}
	else{
		strong_ctrl[i].style.fontSize='26px';
	}
	// alert(strong_ctrl[0].style.fontFamily);
}
