
some_string = "I LOVE THE NIGHTS WHEN I AM ALONE AT 3AM AND THATS THE BEST TIME TO THINK ABOUT LIFE FR"
x = 5
res=[some_string[y-x:y] for y in range(x, len(some_string)+x,x)]
print(res)