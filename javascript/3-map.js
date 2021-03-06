var jsdom = require("jsdom");
var $ = require('jquery')(jsdom.jsdom().defaultView);

$("<h1>test passes</h1>").appendTo("body");
console.log($("body").html());

var legendLayers = [{'id':123, 'legend':'abc'},{'id':324, 'legend':'asdf'}]
console.log("ids:"+Object.keys(legendLayers));

var keys = $.map(legendLayers, function(v, i){
	console.log("v:"+v.id+" i:"+i);
	return v.id;
});
console.log(keys);

var anId = 123;
var object123 = $.map(legendLayers, function(v, i){
	console.log("anId:"+anId);
	if ( v.id == anId) {
		return v.legend;
	}
});
console.log("obj:"+object123);

//javascript only map:
var numbers = [1, 4, 9];
var roots = numbers.map(Math.sqrt);
console.log("roots:"+roots)
//roots is now [1, 2, 3], numbers is still [1, 4, 9]