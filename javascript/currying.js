//jQuery is not an Applicative.
//Lets see an example of actual functors and applicatives in javascript to contrast.
//First, lets define a simple argument-at-a-time, under-application-only currying combinator:

function curry2(f) {
	var that = this;
//	console.log("function:"+f);
	return function(a) {
//		console.log("a:"+a);
		return function(b) {
//			console.log("b:"+b);
//			console.log("that:"+that);
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
var add = function(a, b ){
	return a + b;
};

console.log("curry2:"+curry2(add));
var curry1 = curry2(add)(4);
console.log("curry1:"+curry1);
console.log("curryed:"+curry1(5));           // curryed 9
console.log("curryed:"+(curry2(add)(2))(3)); // curryed 5

var greetCurried = function(greeting) {
	return function(name) {
		console.log(greeting + ", " + name);
	};
};

var greetHello = greetCurried("Hello");
greetHello("Heidi"); //"Hello, Heidi"
greetHello("Eddie"); //"Hello, Eddie"
greetCurried("Hi there")("Howard"); //"Hi there, Howard"

var greetDeeplyCurried = function(greeting) {
	return function(separator) {
		return function(emphasis) {
			return function(name) {
				console.log(greeting + separator + name + emphasis);
			};
		};
	};
};
var greetAwkwardly = greetDeeplyCurried("Hello")("...")("?");
greetAwkwardly("Heidi"); //"Hello...Heidi?"