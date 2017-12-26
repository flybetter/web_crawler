var url='http://www.httpuseragent.org';
var page=require('webpage').create();
console.log('the default user agent is '+page.settings.userAgent);
page.settings.userAgent='SpecialAgent';
page.open(url,function(status){
	if (status != 'success'){
		console.log('Unable to connect network')
	}else{
		var ua=page.evaluate(function(){
			var all=  document.getElementsByTagName('div');
			for (var i=0;i<all.length;i++){
				if (all[i].className=='info') {
					return all[i].innerHTML;	
				};	
			}
			return document.title;
		});
		console.log(ua)
	}
	phantom.exit();
});