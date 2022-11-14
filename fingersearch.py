'''
Implementation of Finger Search on a list 
We are doing static fingers in this
'''
import math
import plotly.express as px
import pandas as pd

def binary_search(array, value, count = 0, first=0):
    #print(array, first)
    count += 1
    mid = len(array)//2
    if len(array) == 0:
        print("empty array found")
        return None
    if array[mid] == value:
        return first + mid, count
    elif array[mid] < value:
        return binary_search(array[mid + 1: ], value, count, first = first + mid + 1)
    else:
        return binary_search(array[:mid], value, count, first)

'''
Simple Static Finger Search on a Sorted Array. 
d = log(n) fingers are created on the array and we binary search the fingers for the value. 
Then we binary search the element between the fingers. 
'''
def finger_search(array, value, count=0):
    
    n_fingers = math.ceil(math.log2(len(array))) # total number of fingers
    fingers = [int(math.pow(2, i) - 1) for i in range(n_fingers)]

    if fingers[-1] < array[len(array) - 1]: # basically the last finger should be the last element
        fingers.append(len(array) - 1)
 
    if value < array[0] or value > array[-1]:
        print("beyond the given array range")
        return None, None
    else:
        # binary search on the fingers and then binary search in the range
        first, last = 0, len(fingers)
        while first <= last:
            count += 1
            mid =  first + (last - first)//2
            if array[fingers[mid]] == value:
                return fingers[mid], count
            elif array[fingers[mid]] < value:
                first = mid + 1
                continue 
            else:
                last = mid - 1
                continue 
        print("found range : ", fingers[last], fingers[first], array[fingers[last] + 1 : fingers[first]])
        index, val = binary_search(array[fingers[last] + 1 : fingers[first]], value)
        #print(fingers[last] + 1 + index, count + val)
        return fingers[last] + 1 + index, count + val
        

if __name__ == "__main__":
    f_counts, b_counts = list(), list()
    indices = [math.pow(2,i) for i in range(5, 20)]
    for i in range(5, 20):
        array = sorted([j * 7 for j in range(2**i)])
        search_value = (int(math.pow(2, i)) - 1) * 7
        #cprint(search_value)
        f_index, f_count = finger_search(array, search_value)
        b_index, b_count = binary_search(array, search_value)
        if f_index != search_value/7:
            f_counts.append(0)
        else:
            f_counts.append(f_count)
        if b_index != search_value/7:
            b_counts.append(0)
        else:
            b_counts.append(b_count)
    print(f_counts, b_counts)
    px.line(pd.DataFrame({
        "indices": indices, 
        "f_counts": f_counts, 
        "b_counts": b_counts
    }), x="indices", y=["f_counts", "b_counts"]).show()

        
        