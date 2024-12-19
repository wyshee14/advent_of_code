def sum_of_min_distances(left_list, right_list):
    #Sort both lists
    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)

    #Calculate the sum of distances
    total_distance = sum(abs(l - r) for l, r in zip(sorted_left, sorted_right))

    return total_distance

def read_numbers(file):
    # initialize as empty list to store numbers
    left_list = []
    right_list = []

    # open the file in read mode 'r'
    with open(file, 'r') as file:
        for line in file:
            #split into parts 
            parts = line.split()
            # convert the split strings into float decimals
            if len(parts) == 2:
                left_list.append(float(parts[0]))
                right_list.append(float(parts[1]))
    return left_list, right_list

if __name__ == "__main__":
    file = "input.txt"
    left,right = read_numbers(file)
    result = sum_of_min_distances(left, right)
    print("Sum of distances:", result)