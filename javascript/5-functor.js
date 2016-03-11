function curry2(f) {
	var that = this;
	return function(a) {
		return function(b) {
			return f.call(that,a,b);
		}
	}
}

//Then we can define a Functor.
function Functor(map) { this.map = curry2(map); }


//map is required to be able to take two arguments. the first should be any function from a -> b, and in exchange it'll give f a -> f b for some f specific to your particular Functor instance.
//A simple example of a Functor is one that takes an array, and gives back a new array, having mapped every element through a function.
//Our choice of 'f' is basically Array.
//We'll ignore anything exotic, and just pretend length is good enough to scan the elements. 

var array = new Functor(
		function(f,a) {
			var b=[];
			for (var i=0;i<a.length;i++)
				b[i] = f(a[i]);
			return b;
		}
	);

//Now you can map just fine over arrays.
//If you give me an function from numbers to numbers, I can take an array of numbers, and give you an array of numbers.

var result = array.map(function(x) { return x + 1 })([1,2,3])
//[2,3,4]
console.log("result:"+result)

//But map is required to work for everything, not just HTMLElements, or whatever jQuery's designers decided to let it wrap today.
//Now lets define Applicative.

function Applicative(pure, ap) {
	this.pure = pure;
	this.ap = curry2(ap);
}