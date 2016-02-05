function compose(f, g) {
	return function(x) { return f(g(x)); }
}

var plus1 = function plus1(x) {
	console.log("x:"+x);
	return x+1;}
var times2 = function times2(x) { return x*2;}

var composed = compose(plus1, times2);
console.log( "composed 3:"+composed(4) );
var composed2 = compose(times2, plus1);
console.log( "composed 3:"+composed2(4) );


console.log( [1,2,3].map(compose(plus1, times2)));

console.log(".split:"+"value".split(""));

function stringFunctor(value, fn) {
	var chars = value.split("");
	return chars.map(function(char){
		return String.fromCharCode(fn(char.charCodeAt(0)))
	}).join("");
}

console.log( stringFunctor("ABCD", plus1));

function functionFunctor(value, fn) {
	return function(initial) {
		return function() {
			return fn(value(initial));
		}
	}
}

var init = functionFunctor(times2, plus1);
var thefinal = init(3)
console.log("thefinal(3):"+thefinal);
console.log("3*2 +1="+thefinal()+ " = "+init(3)());

function maybe( value, fn) {
	if ( value === null)
		return null;
	else if ( value === undefined )
		return undefined;
	else return fn(value);
}

console.log("maybe null:"+maybe(null, compose(plus1, plus1)));
console.log("maybe(undefined, compose(plus1, times2)):"+maybe(undefined, compose(plus1, times2)));
console.log("maybe(maybe(undefined, compose(plus1, times2))):"+maybe(maybe(undefined, compose(plus1, times2))));
console.log("maybe(1, compose(plus1, times2)):"+maybe(1, compose(plus1, times2)));
console.log("maybe(maybe(1, plus1), plus1):"+maybe(maybe(1, plus1), plus1));

//functor must preserver composition - and identity:
console.log("map id"+[1,2,3].map(function(x){return x;})+" -> "+[1,2,3]);

//function signature functors: F: A -> B where e.g A= [int] and B=[String]
//function signature monads  : F: A -> A => so must return same type