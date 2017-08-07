package coding.kata.hackerrank;

import java.util.*;
import java.io.*;

public class Solutions {

	static int height(Node root) {
      	if ( root == null ) return -1;
      	return Math.max(1+height(root.left), 1+height(root.right));
    }
	
	public static void levelTraverse(Node root) {
		Queue<Node> queue = new LinkedList<Node>(); 
		queue.add(root); 
		while( !queue.isEmpty() ) { 
			Node tempNode = queue.poll(); 
			System.out.print(tempNode.data+" "); 
			if ( tempNode.left != null ) 
				queue.add(tempNode.left); 
			if ( tempNode.right != null ) 
				queue.add(tempNode.right); 
		}
	}
	
	public static Node insert(Node root, int data) {
        if(root == null){
            return new Node(data);
        }
        else {
            Node cur;
            if(data <= root.data){
                cur = insert(root.left, data);
                root.left = cur;
            }
            else{
                cur = insert(root.right, data);
                root.right = cur;
            }
            return root;
        }
    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        Node root = null;
        while(t-- > 0){
            int data = scan.nextInt();
            root = insert(root, data);
        }
        scan.close();
        //int height = height(root);
        //System.out.println(height);
        System.out.println("traverse");
        levelTraverse(root);
        
    }	

}
