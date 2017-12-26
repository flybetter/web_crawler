var page=require('webpage').create();
var url='http://www.dota2.com.cn/index.htm'
page.viewportSize={width:1024,height:768};
page.clipRect={top:0,left:0,width:1024,height:768};

console.log("coming");
page.open(url,function(status){
	console.log("status:"+status);
	page.render('dota2.png');
	phantom.exit();
});