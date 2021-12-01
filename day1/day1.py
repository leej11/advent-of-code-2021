import input_handler as ih

input = ih.read_input('input.txt')
input = [int(i) for i in input]

def calculate_element_wise_differences(input_list):
    differences = []
    for i in range(1,len(input_list)):
        differences.append(input_list[i] - input_list[i-1])

    return differences

def increase_classifier(x):
    return x > 0

def calculate_number_of_increases(differences_list):
    return sum(map(increase_classifier, differences_list))

def main():
    input = ih.read_input('input.txt')
    input = [int(i) for i in input]
    differences_list = calculate_element_wise_differences(input)
    print(calculate_number_of_increases(differences_list))

def get_trio_sums_from_list(input_list):

    trio_sums = []
    for i in range(0, len(input_list)-2):
        trio_sums.append(sum([input_list[i], input_list[i+1], input_list[i+2]]))

    return trio_sums


def part2():
    input = ih.read_input('input.txt')
    input = [int(i) for i in input]
    # Calculate a new list that is just a rolling sum of three elements
    input = get_trio_sums_from_list(input)

    # With that, the steps are exactly the same as before
    differences_list = calculate_element_wise_differences(input)
    print(f"Answer to Part 2: {calculate_number_of_increases(differences_list)}")



if __name__ == '__main__':
    part2()



