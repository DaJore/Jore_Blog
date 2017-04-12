'use strict';
var device_width=window.outerWidth;//outerWidth和outerHeight属性,可以获取浏览器窗口的整个宽高
// var device_heigth=window.outerHeight;//innerWidth和innerHeight属性，可以获取浏览器窗口的内部宽度和高度。
// 内部宽高是指除去菜单栏、工具栏、边框等占位元素后，用于显示网页的净宽高
var strong_ctrl1=document.getElementById('ctrl1');//设定在小屏幕(<700px)和大屏幕Home，Blog的大小
var strong_ctrl2=document.getElementById('ctrl2');
if(device_width<700){//对Home，Blog大小控制
	strong_ctrl1.style.fontSize='13px';
	strong_ctrl2.style.fontSize='13px'
}
else{
	strong_ctrl1.style.fontSize='26px';
	strong_ctrl2.style.fontSize='26px';
}
	// alert(strong_ctrl[0].style.fontFamily);
