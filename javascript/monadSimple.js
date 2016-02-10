// functor:
// type signature inner:	f: int -> int
// type signature inner:	map: [int] -> [int]
// type signature outer:	f: int -> [int]
// type signature outer 	map: [int] -> [[int]] 
var result = [1, 2].map(function(i) {
    return [3, 4].map(function(j) {
       return i + j;
    });
});
console.log(result) 


// type signature monads: f: [T] -> [T]
// type signature of function passed to monad: f: T -> [T]
// function passed to monad is called lift - or monadic function
function arrayMonad(mv, mf) {
	var result = [];
	mv.forEach(function(v) {
		result = result.concat(mf(v));
	});
	return result
}


var result0 = arrayMonad([1,2], (function(i) {return i+1;})); 
console.log( result0 );
var result2 = arrayMonad([1, 2], function(i) {
    return [3, 4].map(function(j) {
       return i + j;
    });
});
console.log(result2);

var lift = function(i) {
	return [i];
}
var liftPlus1 = function(i) {
	return [i+1];
}
var result3 = arrayMonad([1,2,3], lift);
console.log(result3);

var result4 = arrayMonad([1,2,3], liftPlus1);
console.log(result4);

var liftTwoArrays = arrayMonad([1,2], function(i) {
	return arrayMonad([3,4], function(j) {
		return [i+j];
	}) 
});

console.log(liftTwoArrays);
