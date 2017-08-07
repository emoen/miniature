package coding.kata.amazon;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;

/**
 * Question part 2 in Amazon 
 * @author endrem
 *
 */
public class AStarSeach {
	public static int[][] aField = {{1,1,1,12,1,1},
                             		{1,0,0,0,0,1 },
                         			{1,1,1,14,1,1},
                         			{1,1,1,1,1,1 },
                         			{1,1,1,1,1,1 },
                         			{15,1,1,1,1,1}};

	public static void main(String[] args ) {
		shortestPath( 6, 6, aField );
	}
	
	public static int shortestPath(int numRows, int numColumns, int[][] field) {
		
		List<Tree> trees = new ArrayList<Tree>();
		for ( int i=0; i < aField.length; i++ ) {
			for ( int j=0; j < aField[i].length; j++ ) {
				if ( field[i][j] > 1 ) {
					trees.add( new Tree(i, j, field[i][j]) );
				}
			}
		}
		Collections.sort(trees);
		for (int i=0; i<trees.size(); i++) {
			System.out.println(""+trees.get(i));
		}
		
		for ( int i=1; i < trees.size(); i++) {
			Astar(trees, field, numRows, numColumns, i);
		}
		
		
		return 0;
	}
	
	static LinkedList<Tree> openList = new LinkedList<Tree>();
	static LinkedList<Tree> closedList = new LinkedList<Tree>();
	
	public static void Astar ( List<Tree> trees, int[][] field, int numRows, int numColumns, int targetIndex ) {
		
		int targetIdx = targetIndex;
		int startIdx = targetIndex -1;
		Tree target = trees.get( targetIdx );
		Tree start = trees.get( startIdx );
		
		openList.addFirst( trees.get(0) );
		while ( isMemberOfList( target, closedList ) == null || openList.isEmpty() ) {
			List<Tree> legalMoves = new ArrayList<Tree>(4);
			if ( start.row + 1 < numRows && field[start.row+1][start.col] > 0 ) {
				legalMoves.add( createNewMove( start, start.row+1, start.col, target, field) );
			}
			if ( start.row - 1 >= 0 && field[start.row-1][start.col] > 0 ) {
				legalMoves.add( createNewMove( start, start.row-1, start.col, target, field) );
			}
			if ( start.col + 1 < numColumns && field[start.row][start.col+1] > 0 ) {
				legalMoves.add( createNewMove( start, start.row, start.col+1, target, field) );
			}
			if ( start.col - 1 >= 0 && field[start.row][start.col-1] > 0) {
				legalMoves.add( createNewMove( start, start.row, start.col-1, target, field) );
			}
			closedList.addLast(start);
			openList.remove(start); //should remove start;
			
//			Collections.sort( legalMoves, new TreeNodeGscore() );
			int lowestHscore = Integer.MAX_VALUE;
			Tree lowestHscoreNode = null;
			for ( Tree legalMove : legalMoves) {
				Tree compareMoveTo = isMemberOfList( legalMove, closedList );
				if ( compareMoveTo == null ) {
					openList.addFirst( legalMove );
					lowestHscoreNode = getLowestHscore( lowestHscore, lowestHscoreNode, legalMove );
					lowestHscore = lowestHscoreNode.H;
				} else {
					if ( compareMoveTo.G > legalMove.G ) { //new node found has better G (accum traveling cost)
						compareMoveTo = legalMove;
						
						lowestHscoreNode = getLowestHscore( lowestHscore, lowestHscoreNode, legalMove );
						lowestHscore = lowestHscoreNode.H;
					}
				}
			}
			start = lowestHscoreNode;
			System.out.println("G:"+start.H+" (row, col):"+start.row+ ", "+start.col+" val:"+start.height+" target.val:"+target.height);
		}
		
		printPath( closedList );
	}
	
	public static Tree getLowestHscore( int lowestHscore, Tree lowestHscoreNode, Tree legalMove ) {
		if ( legalMove.H < lowestHscore ) {
			lowestHscoreNode = legalMove;
		}
		return lowestHscoreNode;
	}
	
	private static Tree createNewMove( Tree start, int newRow, int newCol, Tree target, int[][] field ) {
		Tree legalMove = new Tree( newRow, newCol, field[newRow][newCol] );
		legalMove.parent = start;
		legalMove.G = start.G + 1;
		legalMove.H = Math.abs( legalMove.row - target.row ) + Math.abs( legalMove.col - target.col );
		return legalMove;
	}
	
	/**
	 * returns Tree if member found (true) else returns null (for false)
	 */
	private static Tree isMemberOfList( Tree tree, LinkedList<Tree> target ) {
		for ( Tree member : target ) {
			if ( tree.row == member.row && tree.col == member.col ) {
				return member;
			}
		}
		return null;
	}
	
	public static void printPath( List<Tree> closedList ) {
		for ( Tree next : closedList) {
			System.out.print("("+next.col+", "+next.row+") -> ");
		}
		System.out.println("");
	}
	
	static class TreeNodeGscore implements Comparator<Tree> {
		@Override
		public int compare( Tree a, Tree b ) {
			return a.G - b.G;
		}
	}
	
	static class  Tree implements Comparable<Tree>{
		public Tree parent = null;
		public int G = 0;
		public int H = 0;
		public int F = G+H;
		
		public int row;
		public int col;
		public int height;
		
		public Tree(int row, int col, int height) {
			this.row = row;
			this.col = col;
			this.height = height;
		}
		
		@Override
		public String toString() {
			return ""+height;
		}
		
		@Override
		public boolean equals( Object other ) {
			if ( other instanceof Tree && this.row == ((Tree)other).row && this.col == ((Tree)other).col )
				return true;
			return false;
		}
		
		@Override
		public int compareTo( Tree other ) {
			return Integer.compare(this.height, other.height);
		}
	}
}
