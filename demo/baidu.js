// var url = 'http://www.baidu.com';
// var page = require('webpage').create();
// // page.onConsoleMessage = function (msg) {
// //     console.log(msg);
// // };
// page.open(url, function(status) {
//    page.evaluate(function() {
//   	console.log('Page title is ' + document.title);
//     // return document.title;
//   });
//  // console.log('Page title is ' + title);
//   phantom.exit();
// });

var url="http://www.douban.com";
var page=require('webpage').create();
page.onConsoleMessage=function(msg){
	console.log(msg);
}
page.open(url,function(status){
	var title=page.evaluate(function(){
		return document.title;
	});
	console.log(title)
	phantom.exit();
});

