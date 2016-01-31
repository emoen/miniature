jQuery is not an Applicative.
Lets see an example of actual functors and applicatives in javascript to contrast.
First, lets define a simple argument-at-a-time, under-application-only currying combinator:

function curry2(f) {
var that = this;
return function(a) {
return function(b) {
return f.call(that,a,b);
}
}
}

Then we can define a Functor.

function Functor(map) { this.map = curry2(map); }

/**
map is required to be able to take two arguments. 
The first should be any function from a -> b, 
and in exchange itll give f a -> f b for some f specific to your particular Functor instance.
A simple example of a Functor is one that takes an array, and gives back a new array, 
having mapped every element through a function.
Our choice of 'f' is basically Array.
Well ignore anything exotic, and just pretend length is good enough to scan the elements. 
*/

var array = new Functor(
function(f,a) {
var b=[];
for (var i=0;i<a.length;i++)
b[i] = f(a[i]);
return b;
}
);

Now you can map just fine over arrays.
If you give me an function from numbers to numbers, I can take an array of numbers, and give you an array of numbers.

> array.map(function(x) { return x + 1 })([1,2,3])
[2,3,4]

But map is required to work for everything, not just HTMLElements, or whatever 
jQuery's designers decided to let it wrap today.
Now lets define Applicative.

function Applicative(pure, ap) {
this.pure = pure;
this.ap = curry2(ap);
}

Here pure takes any value of any type a, and generates an f a, for some f particular to the applicative.
And ap takes an f (a -> b), and an f a, and generates an f b.
Every Applicative is a Functor, so we'll chain the prototypes.

Applicative.prototype = new Functor(
function(f,a) {
return this.ap(this.pure(f))(a);
}
);

Now to demonstrate, we can make the reader applicative out of functions:

var reader = new Applicative(
function(a) {
return function(e) { return a; }
},
function(mf,ma) {
return function(e) {
return mf(e)(ma(e));
}
}
);

You can bolt the traditional reader combinators like ask, directly into reader.

reader.ask = function(e) { return e; };

Notice we take pure values and return fresh new values, clearIds on the other hand is just mutating some HTMLElement.
We can also define the state applicative.

var state = new Applicative(
function(a) {
return function(s) {
return [a,s];
};
},
function(mf,ma) {
return function(s) {
var t = mf(s);
var u = ma(t[1]);
return [t[0](u[0]),u[1]];
}
}
);