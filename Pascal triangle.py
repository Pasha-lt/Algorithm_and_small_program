n = int(input('size'))
listb = [] # Create list
for i in range(n+1):
    listb.append([1] + [0]*n) #in the first column we put '1'. other column we put '0'.

for i in range(1,n): # first column don't touch.
    for j in range(1,i): # if we write 'i' we don't calculate above the main diagonal (dont calculate right triangle)
        listb[i][j]=listb[i-1][j]+listb[i-1][j-1] #In the index we write the sum of indexes above.

for i in range(n):
    for j in range(i): # if we use i+1 we output only needfull numbers without empty elements
        print(listb[i][j], end=' ')
    print()
