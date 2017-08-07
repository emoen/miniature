package unionFind;

public class UnionFind {

    int id[] = new int[10];
    
    int sz[] = new int[10];
    
    public UnionFind() {
        for ( int i=0; i < 10; i++) { id[i] = i;sz[i] = 1;}
    }
    
    public void connect(int a, int b) {
    	int ida = id[a];
        for (int i=0; i < id.length; i++) {
            if ( id[i] == ida ) id[i] = id[b];
        }
    }
    
    public boolean unionFind( int a, int b ) {
        return id[a] == id[b];
    }
    
    public int root(int a) {
        return 0;
    }
    
    public static void main(String[] args) {
        UnionFind u = new UnionFind();
        u.connect(1,2);
        u.connect(1,8);
        u.connect(2,7);
        
        boolean istrue = u.unionFind(1, 2);
        boolean isfalse = u.unionFind(1, 3);
        
        System.out.println("istrue:"+istrue+" isfalse:"+isfalse);
        
        UnionFind u2 = new UnionFind();
        u2.quickConnect(1,2);
        u2.quickConnect(1,8);
        u2.quickConnect(2,7);
        
        boolean istrueQ = u.quickFind(1, 2);
        boolean isfalseQ = u.quickFind(1, 3);
        
        System.out.println("istrue:"+istrueQ+" isfalse:"+isfalseQ);
        
        UnionFind u3 = new UnionFind();
        u2.weightedConnect(1,2);
        u2.weightedConnect(1,8);
        u2.weightedConnect(2,7);
        
        boolean istrueW = u.weightedFind(1, 2);
        boolean isfalseW = u.weightedFind(1, 3);
        
        System.out.println("istrue:"+istrueW+" isfalse:"+isfalseW);
    }
    
    public int quickRoot(int i) {
    	while( i != id[i] ) i = id[i];
    	return i;
    }
    
    public void quickConnect(int a, int b) {
    	int i = quickRoot(a);
    	int j = quickRoot(b);
    	id[i] = j; 
    }
    
    public boolean quickFind(int a, int b) {
    	return quickRoot(a) == quickRoot(b);
    }
    
    public int weightedRoot(int i) {
    	while( i != id[i] ) i = id[i];
    	return i;    	
    }
    
    public void weightedConnect(int a, int b) {
    	int i = quickRoot(a);
    	int j = quickRoot(b);
    	if (sz[i] > sz[j] ) {id[j] = i; sz[i] = sz[i] + sz[j];}
    	else {id[i] = j; sz[j] = sz[j] + sz[i];}
    }
    
    public boolean weightedFind(int a, int b) {
    	return weightedRoot(a) == quickRoot(b);
    }    
}
