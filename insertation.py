def insertaton(array):

    for num in range(1, len(array)):
        key = array[num]
        j = num - 1
        
        #moghayese har index ba index haye samt chap      
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        #ja gozari dar sorat kochak tar bodn
        array[j + 1] = key


test = [9, 5, 1, 4, 3]
insertaton(test)
print(test)