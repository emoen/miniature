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
	return result;
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

function forEach2d(array1, array2, callback) {
	return arrayMonad(array1, function(i) {
		return arrayMonad(array2, function(j) {
			return [callback(i,j)];
		})
	})
};

console.log(forEach2d([1,2], [3,4], function(i, j) {return i+j+1;}));

console.log([1,2].concat(3));
console.log([1,2].concat([3])); //concat lifts elements to array

function arrayMonadWithPush(mv, mf) {
	var result = [];
	mv.forEach(function(v) {
		Array.prototype.push.apply(result, mf(v));
	});
	return result;
}

function forEach2dV2(array1, array2, callback) {
	return arrayMonadWithPush(array1, function(i) {
		return arrayMonadWithPush(array2, function(j) {
			return [callback(i,j)];
		})
	})
};

console.log(forEach2dV2([1,2], [3,4], function(i, j) {return i+j+1;}));

arrayMonadWithPush.mResult = function(v) {return [v];}

function forEach2dV3(array1, array2, callback) {
	return arrayMonadWithPush(array1, function(i) {
		return arrayMonadWithPush(array2, function(j) {
			return arrayMonadWithPush.mResult(callback(i,j));
		})
	})
};

console.log(forEach2dV3([1,2], [3,4], function(i, j) {return i+j+1;}));

//The arrayMonad is a monadic function and is otherwise known as bind or mbind. 
//For a function to be a monad it must define atleast the functions mbind and mresult.

