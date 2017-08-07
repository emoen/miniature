package coding.kata.hackerrank;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class Contacts {
	
	public static Map<String, Integer> names = new HashMap<String, Integer>();
	
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            String command = in.next();
            String text = in.next();
        
            
            if ( command.equals("add") ) {
	            Integer count = names.get( text );
	            if ( count == null )
	            	names.put( text, 1);
	            else names.put( text, count+1);
	            for ( int i=0; i < text.length(); i++ ) {
	            	String sub = text.substring(0, i);
	            	Integer aCount = names.get(sub);
	            	if ( aCount ==  null ) {
	            		names.put( sub,  1);
	            	} else {
	            		names.put( sub, aCount+1);
	            	}
	            }
            } else if ( command.equals("find") ) {   	
	            Integer result = findContact( text );
	            System.out.println(result);
            }
        }
        in.close();
    }
    
    public static Integer findContact(String fragment) {
    	Integer theCount = names.get(fragment);
    	if ( theCount == null ) return 0;
    	return theCount;
    }
}
