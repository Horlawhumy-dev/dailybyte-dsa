
def gameWinner(colors):
    # Write your code here
    
    
    colors_list = []

    for i in range(len(colors)):

        colors_list.append(colors[i])

    w_list = [color for color in colors_list if color == "w"]
    b_list =  [color for color in colors_list if color == "b"]
    
    if (len(w_list) - len(b_list)) % 2 == 0:
        return "bob" 
    else:
        return "wendy"
        

print(gameWinner("bbwwwwbbbwbwbwwbbbbbwwbwwbbwbwwbwwbwwbbwwbwbwbbwbbwwbwbbwbbwwbwwbwbwbbwwwbwwbbwbbbbbwwwwwbwbwbwwbwbbbwbbbbwbwbwwbbwbwbbbwbwwwwwwbbwbwbwwwbwbwwwbbwwbwbbwwwbbbbwwbbbwbbbbwwwwwbbwwbbwwwwwwbwbbwwwbbbwbbwwwwwwbbwwbbwwwbbbbwwbbbbbbwwbbbbbwbwbwbwwbbbwbwbbwbbbbwwwwwbbwbwbbbbbwwbwwbwwwwbwwbbbbbbwbbbwwwwbwbbwbbbwwwwbwwwbbwwwbwwwbwbwbbbwbwwwbwwbwwwwbwbwwbwwwwwbwbwbwwbwbbbwbbwbwbwwbbbwwwbbbbwwwwwbbbbwwwwwbbbbwwwwbbwbbwbbwwwbwbbwbbwwbbbbbwbbwbwbwbwwwbwwwwwbwbwwbwbwbwbbwbbbbbbbwwbbwbbwwbwbbbbwbwwbbbwbwwbwbbwwwwwbwbwwbwbwwbbwwbbbwbwwwbbwwwwwbbbbbbbbwwbwwwwbbbbwwbbbbbbwwwbbbbbwbwbbbwwwwbbwwwbwwwwwwwbwbbbbwwwbwwwwbwbwwwbwwbwwwbwwbbbwbwbwwwbbbbwwwbbbwwbwbwwbwwbbbwbwbwwwbbwwbbwwbwbwbwwbwwwbwbwbwbbbwwbwbwbbwbwwwwbbbwbbbwwwwbwbbwbbwwwbwwwbbbbwbwbwwwwbbbwbwwbwbbwwwbbbwwbbbbwbwwbwbwwwwwbbwwbwwbwwbbbbwwbwwwbwwwwwwbbbbwbbbwbbwbwbwbbwbbbwwwbbbbbwbwwwwbbbwbwwbbwbwwbwwbwbbbwwbwwwbbbwbbwwwbbbbbwwbwwwbbwbbwbwwwbbwbwwwbwwbwwwwbbwwbbwwwwwbwwbbwwbwbwbbbwwbbwbbwwbbbwwbwbwbwbbwwwwwbbbwwwbbwbbwwwbwwwbwwbwwbbbbbwbbwwwwbb"))
   