package unionFind;

import java.util.function.BiFunction;
import java.util.function.Function;
import java.util.function.IntBinaryOperator;

public class HigherOrderFunction {

	public static void main(String[] args) {

		IntBinaryOperator plusOperation = (a, b) -> a + b; //lambda expression
		System.out.println("Sum of 10,34 : " + plusOperation.applyAsInt(10, 34));
		
		/**
		 * Type Parameters:<T> the type of the first argument to the function<U> the type of the second argument to the function<R> the type of the result of the function
		 */
		BiFunction<Integer,Integer,Integer> adder = ( a, b ) -> a + b ;
		Function<Integer,Function<Integer,Integer>> currier = a -> b -> adder.apply( a, b ) ;
		Function<Integer,Integer> curried = currier.apply( 4 ) ;
		System.out.printf( "Curry : %d\n", curried.apply( 3 ) ) ;
	}
}
