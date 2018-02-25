import numpy as np
import math
import sys

def read_file(filename):
    '''
    Read the file.
    Return the pizza as a binary matrix: Tomatoes = 1, Mushrooms = 0
    Also, return the minimum ingredients required for each slice,
    and the maximum cells allowed for each slice.
    '''
    
    with open(filename, 'r') as f:
        line = f.readline()
        rows, cols, min_ings, max_cells = [int(n) for n in line.split()]
        
        pizza = np.zeros([rows, cols])
        for row in range(rows):
            for ing, col in zip(f.readline(), range(cols)):
                if ing == 'T':
                    pizza[row, col] = 1
                else:
                    pizza[row, col] = 0
    
    return pizza, min_ings, max_cells
    
def main(argv):
    pizza, min_ings, max_cells = read_file('example.in')
    print(""+str(pizza))
    print("min_ings:"+str(min_ings))
    print("max_cells:"+str(max_cells))
    
    slices = 0
    rows, cols = pizza.shape
    print(rows)
    print(cols)
    

    slice_from_row = 0
    slice_from_col = 0
    row_step = 1
    
    #out_rader = 
    out_matrix = np.zeros((rows*cols, 4)) #rows*cols
    
    out = False
    out_count = 0
    
    #print("max_"+str(max_cells))
    if max_cells > cols:
        max_cells = cols
    #print("max_"+str(max_cells))
    while not out:
        a_slice = pizza[slice_from_row:slice_from_row+row_step,slice_from_col: slice_from_col+max_cells]   
        #print("a_slice"+str(a_slice))
        valid = is_valid(a_slice, min_ings)
        if valid == True:
            valid_array = [slice_from_row, slice_from_col, slice_from_col+row_step, max_cells]
            out_matrix = out_matrix + valid_array
            out_count += 1
            slice_from_col += max_cells
        elif valid == False:
            slice_from_col += 1
        
        if slice_from_col >= cols:
            
            slice_from_row += row_step
            slice_from_cols = 0
            print(slice_from_row)

        if slice_from_row == rows:
            out = True

    print(out_matrix[0:out_count,:])   
    F = open("workfile.out","w")
    F.writelines(str(out_count)+"\n")
    F.write(str(out_matrix[0:out_count,:]))
            
def is_valid(a_slice, min_ings):
    count_T = 0
    count_M = 0
    
    #print("a_slice:"+str(a_slice.shape))
    arow, acol = a_slice.shape
    #print(arow)
    #print(acol)
    for i in range(arow):
        for j in range(acol):
            #print("i:"+str(i)+" j:"+str(j)+" v:"+str(a_slice[i][j] ))
            if a_slice[i][j] == 1:
                count_T +=1
            if a_slice[i][j] == 0:
                count_M +=1
    if count_T >= min_ings and count_M >= min_ings:
        print("tomatos:"+str(count_T))
        print("mush:"+str(count_M))
        return True
    else:
        print("tomatos:"+str(count_T))
        print("mush:"+str(count_M))    
        return False
            

    
if __name__ == "__main__":
    main(sys.argv)