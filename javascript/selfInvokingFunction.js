var invokeFunction = (function (){
	console.log("hello invoke");
});

invokeFunction();

var selfInvoke = ( function() {
	var dummy = "hello selfinvoke closure";
	return function() { console.log(dummy);}
})();

selfInvoke();

var selfSelfInvoke = ( function() {
	var closure1 = "hello selfinvoke closure1";
	return function() {
		var closure2 = "hello selfinvoke closure2";
		return function() { console.log("closure1:"+closure1+" closure2:"+closure2);}
	}();
})();

selfSelfInvoke();

var add = (function () {
	//javascript closure
	// A closure is a function having access to the parent scope, even after the parent function has closed. 
    var counter = 0;
    return function () {return counter += 1;}
})();

console.log(add());
console.log(add());
console.log(add());
console.log(add);

function doSomething(x) {
	var y = 4;
	return function addThem(z) {
		return z+4;
	}(x);
}

console.log(doSomething(4));


