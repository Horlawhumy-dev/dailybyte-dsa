

def remove_all_adjacent_duplicates(s: str):

    letters  = dict()
    letters_list  = list()

    for _, val in enumerate(s):

        letters_list.append(val)

    # print(letters_list)

    for i in range(len(letters_list)):
        index = letters.get(letters_list[i], -1)
        print(index)
        if index == -1:
            letters[letters_list[i]] = i
            print(letters)
            
        else:
            del letters[letters_list[i]]
            del letters_list[i]
            del letters_list[index]

    # print(letters)
            
    return " ".join(letters_list)

print(remove_all_adjacent_duplicates("abbaca"))



