var page=require('webpage').create();
var url="http://www.sample.com"
page.open(url,function(){
	page.includeJs('http://ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.min.js',function(){
		page.evaluate(function(){
			$("#button").click();
		});
			phantom.exit();
	});
});