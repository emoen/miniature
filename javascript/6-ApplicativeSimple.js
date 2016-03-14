/**
 * Applicative takes functors to the next level
 * With applicative our values are wrapped in  a context, just like functors
 * And our functions (to sent to functors are wrapped in context too)
 * 
 * So - Applicative: knows how to apply a function-wrapped-in-context to
 * a value-wrapped-in-context
 */


// the mayby type as functor
var none = {
		map: function(func) {
			return none;
		},
		bind: function(func) {
			return none;
		},
		toString: function() {
			return "none";
		}
}

console.log("none.map:"+none.map(console.log));
console.log("none.bind:"+none.bind(console.log));
console.log("none.toString:"+none.toString());

function some(value) {
	return {
		map: function(func) {
			return some(func(value));
		},
		bind: function(func) {
			return func(value);
		},
		toString: function() {
			return "some("+value+")";
		}
	}
}

console.log("some.map:"+some(3).map(console.log));
console.log("some.bind:"+some(3).bind(console.log));
console.log("some.toString:"+some(3).toString());

function thatReturnsSomething() {return "tre"; }
console.log("some(thatReturnsSomething).map:"+some(3).map((thatReturnsSomething)));
console.log("some(thatReturnsSomething).bind:"+some(3).bind((thatReturnsSomething)));
console.log("some(thatReturnsSomething).toString:"+some(3).toString());

var functor = {
		map: function(func, option) {
			return option.map(func);
		},
		unit: some,
	    applyFunctor: function(funcOption, argOption) {
	        return funcOption.bind(function(func) {
	            return argOption.map(func);
	        });
	    }
};

var four = some(4)
var fourThatReturnsTree = some(thatReturnsSomething)

console.log("functor.map:"+functor.map(thatReturnsSomething, four));
console.log("functor.unit:"+functor.unit(4));
//console.log("functor.applyFunction:"+functor.applyFunction(fourThatReturnsTree,four));

var six = some(6);
function add(first, second) {
	return first + second;
}

function curry(func, numberOfArguments) {
    return function(value) {
        if (numberOfArguments === 1) {
            return func(value);
        } else {
            return curry(func.bind(null, value), numberOfArguments - 1);
        }
    };
}

var aa = functor.applyFunctor(functor.map(curry(add, 2), four), six);
//=> some(10)

console.log("a:"+aa)


function curry2(f) {
	var that = this;
	return function(a) {
		return function(b) {
			return f.call(that,a,b);
		}
	}
}

var first = curry2(add)
//console.log("first:"+first);
var second = functor.map( first, four );
//console.log("second:"+second);
var third = functor.applyFunctor( second, six )
console.log("third:"+third);

var a = functor.applyFunctor(functor.map( curry2(add), four ), six );
//=> some(10)
var b = functor.applyFunctor(functor.map(curry2(add), none), six);
//=> none
var c = functor.applyFunctor(functor.map(curry2(add), four), none);
//=> none

console.log(" "+a);
console.log(" "+b);
console.log(" "+c);

