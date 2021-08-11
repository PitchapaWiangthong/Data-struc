print("*** Minesweeper ***")
lst_input = []
input_list = input("Enter input(5*5) : ").split(",")

def num_grid(lst):
  n=5
  count = 0
  for i in range(0,n):
    for j in range(0,n):
      #check above 
      



      if lst[i][j] != '#':
        lst[i][j] = str(count)
  return lst


for e in input_list:
  lst_input.append([i for i in e.split()])

print("\n",*lst_input,sep = "\n")
print("\n",*num_grid(lst_input),sep = "\n")
