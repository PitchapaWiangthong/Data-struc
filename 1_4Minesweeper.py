print("*** Minesweeper ***")
lst_input = []
input_list = input("Enter input(5x5) : ").split(",")

def num_grid(lst):
  count = 0
  for i in range(0,5):
    for j in range(0,5):
      if lst[i][j] != '#':
        if j == 0 :
          if lst[i][j+1] == '#' : count+=1 #check center right (edge)
        if j == 4 :
          if lst[i][j-1] == '#' : count+=1 #check center left (edge)
        if i == 0 :
          if lst[i+1][j] == '#' : count+=1 #check bottom (edge)
        if i == 4 :
          if lst[i-1][j] == '#' : count+=1 #check top (edge)
        if (i >= 1 and i <= 3) and (j >= 1 and j <= 3) :
          if lst[i][j+1] == '#' : count+=1 #check center right
          if lst[i][j-1] == '#' : count+=1 #check center left
          if lst[i-1][j] == '#' : count+=1 #check top center
          if lst[i+1][j] == '#' : count+=1 #check bottom center
        if (i >= 1 and i <= 4) and (j >= 0 and j <= 3) : 
          if lst[i-1][j+1] == '#' : count+=1 #check top right
        if (i >= 1 and i <= 4) and (j >= 1 and j <= 4) :
          if lst[i-1][j-1] == '#' : count+=1 #check top left
        if (i >= 0 and i <= 3) and (j >= 0 and j <= 3) :
          if lst[i+1][j+1] == '#' : count+=1 #check bottom right
        if (i >= 0 and i <= 3) and (j >= 1 and j <= 4) :
          if lst[i+1][j-1] == '#' : count+=1 #check bottom left
        if (i >= 1 and i <= 3) and (j == 0 or j == 4):
          if lst[i-1][j] == '#' : count+=1 #check top 
          if lst[i+1][j] == '#' : count+=1 #check bottom 
        if (i == 0 or i == 4) and (j >= 1 and j <= 3) :
          if lst[i][j-1] == '#' : count+=1 #check left
          if lst[i][j+1] == '#' : count+=1 #check right
        lst[i][j] = str(count)
        count = 0 
  return lst
for e in input_list:
  lst_input.append([i for i in e.split()])
print("\n",*lst_input,sep = "\n")
print("\n",*num_grid(lst_input),sep = "\n")
