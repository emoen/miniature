//jQuery is not an Applicative.
//Lets see an example of actual functors and applicatives in javascript to contrast.
//First, lets define a simple argument-at-a-time, under-application-only currying combinator:

function curry2(f) {
	var that = this;
	console.log("function:"+f);
	return function(a) {
		console.log("a:"+a);
		return function(b) {
			console.log("b:"+b);
			console.log("that:"+that);
			return f.call(that,a,b);
		}
	}
}

/**
map is required to be able to take two arguments. 
The first should be any function from a -> b, 
and in exchange itll give f a -> f b for some f specific to your particular Functor instance.
A simple example of a Functor is one that takes an array, and gives back a new array, 
having mapped every element through a function.
Our choice of 'f' is basically Array.
Well ignore anything exotic, and just pretend length is good enough to scan the elements. 
*/
var add4 = function(a ){
	return function(b) { 
		return 4+b;
	}();
};

console.log(add4(5));