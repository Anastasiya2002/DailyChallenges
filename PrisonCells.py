#There are 8 prison cells in a row, and each cell is either occupied or vacant.

#Each day, whether the cell is occupied or vacant changes according to the following rules:

#If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
#Otherwise, it becomes vacant.
def prisonAfterDays(cells,N):
    new_cells = [0]
    for i in range(N):
        for j in range(1,len(cells)-1):
            if (cells[j-1]== 1 and cells[j+1]==1 ) or  (cells[j-1]== 0 and cells[j+1]==0) :
                new_cells[j:]=[1,cells[j+1]]
            else:
                new_cells[j:]= [0,cells[j+1]]
        cells = new_cells[:-1] +[0]
        print(cells)
        new_cells= [0]
    return cells

print(prisonAfterDays([0,1,0,1,1,0,0,1], N = 7))

