package coding.kata.hackerrank;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class RunningMedian {
	
	private static LinkedList<Integer> running = new LinkedList<Integer>();
	
    public static void main(String args[] ) throws Exception {

	    Scanner in = new Scanner(System.in);
	    int t = in.nextInt();
	    for(int a0 = 0; a0 < t; a0++){
	        String s = in.next();
	        float result = runningMedian(s);
	        System.out.printf("%.1f ", result);
	    }
	    in.close();
    }
    
    public static float runningMedian( String s) {
    	Integer next = new Integer(s);
    	
    	if ( running.size() == 0 ) {
    		running.add(next);
    	} else {
	    	for ( int i=0; i < running.size(); i++ ) {
	    		if ( running.get(i) > next) { 
	    			if ( i > 0) {
	    				running.add(i, next);
	    			}else {
	    				running.addFirst( next);
	    			}
	    			break;
	    		} else if ( i+1 == running.size() ) {
	    			running.addLast( next );
	    			break;
	    		}
	    	}
    	}
    	
    	
    	int mid = running.size() / 2;
    	if ( (running.size() & 1) == 0) { //even
    		return (running.get(mid-1) + running.get(mid)) / 2.0f;
    	}
		return running.get(mid);
    }
}
