package coding.kata.hackerrank;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Brackets {

    static String isBalanced(String s) {

    	List<Character> balance = new ArrayList<Character>();
    	
    	char[] ss = s.toCharArray();
    	for ( int i=0; i < ss.length; i++ ) {
    		balance.add(i, ss[i]);
    	}
    	Character char2 = balance.get(balance.size()-1);
    	Character char1 = null;
    	for (int i=balance.size()-2; i >= 0; i-- ) {
    		char1 = balance.get(i);
    		
			if( char1.equals('(') && char2.equals(')') ||
					char1.equals('[') && char2.equals(']') || 
					char1.equals('{') && char2.equals('}') ) {
				balance.remove( i +1 );
				balance.remove( i );
//				System.out.println("new size:"+balance.size());
				if ( balance.size() > 0 ) {
					char2 = balance.get(balance.size()-1);
					i = balance.size()-1;
				}
			} else {
				char2 = char1;
			}
    	}
    	
    	if (balance.size() == 0) return "YES";
    	return "NO";
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            String s = in.next();
            String result = isBalanced(s);
            System.out.println(result);
        }
        in.close();
    }

}
