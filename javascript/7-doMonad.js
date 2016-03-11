function arrayMonad(mv, mf) {
	var result = [];
	mv.forEach(function(v) {
		Array.prototype.push.apply(result, mf(v));
	});
	return result;
}

arrayMonad.mResult = function(v) {return [v];}


/*
 * The arguments object is a local variable available within all functions. 
 * You can refer to a function's arguments within the function by using the arguments object. 
 * This object contains an entry for each argument passed to the function, 
 * the first entry's index starting at 0. For example, 
 * if a function is passed three arguments, you can refer to them as follows:
arguments[0]
arguments[1]
arguments[2]
*/

// curry function
function curry(fn, numArgs) {
    numArgs = numArgs || fn.length
    return function f(saved_args) {
        return function() {
            var args = saved_args.concat(Array.prototype.slice.call(arguments))
            return args.length === numArgs ? fn.apply(null, args) : f(args)
        }
    }([])
}

function doMonad(monad, values, cb) {
    function wrap(curriedCb, index) {
        return function mf(v) {
            return (index === values.length - 1) ?
                monad.mResult(curriedCb(v)) :
                monad(values[index + 1], wrap(curriedCb(v), index + 1))
        }
    }
    return monad(values[0], wrap(curry(cb), 0))       
}
var doM = doMonad(arrayMonad, [[1, 2], [3, 4]], function(x, y) {
    return x + y
})    


console.log(doM);

function FOR() {
    var args = [].slice.call(arguments)
        callback = args.pop()
    return doMonad(arrayMonad, args, callback)
}

var a = FOR([1, 2], [3, 4], function(x, y) {
    return x + y
})   
var b = FOR([1, 2], [3, 4], [5, 6], function(x, y, z) {
    return x + y + z
})   

console.log(a)
console.log(b)

