var page=require('webpage').create(),
system=require('system'),
t,address;

if (system.args.length===1) {
	console.log('Usage:loadspeed.js<some URL>');
	phantom.exit();
};

t=Date.now();
address=system.args[1];
page.open(address,function(status){
	if (status!='success') {
		console.log('FAIL to load the address')
	}else{
		t=Date.now()-t;
		console.log('loading'+system.args[1]);
		console.log('loading time '+t+' msec');
	}
	phantom.exit();
})


var url="http://www.baidu.com"
page=require('webpage').create();


page.open(url,function(status){
	page.evaluate(function(message){
		console.log(document.title)
	})
})