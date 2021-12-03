import input_handler as ih
from collections import Counter

input = ih.read_input('input.txt')
# input = [int(i) for i in input]

def calc_power_consumption(gamma_rt, epsilon_rt):

    return gamma_rt * epsilon_rt


def get_diagnostic_counter(diagnostic_report):

    counter_dict = {}

    for binary_number in diagnostic_report:
        for pos, bit in enumerate(binary_number):

            # My theory is that provided we know the total number of
            # binary numbers in the input list, then if I just
            # calculate a total sum of the 1s in each column,
            # if that sum <= 0.5(nrows), then 0 prevails, else 1 prevails
            if pos in counter_dict.keys():
                counter_dict[pos] += int(bit)
            else:
                counter_dict[pos] = int(bit)

    return counter_dict


def get_gamma_rate(diagnostic_counter):

    binary_gamma_rate = ''

    for pos in diagnostic_counter.keys():

        if diagnostic_counter[pos] < 500:
            binary_gamma_rate += '0'
        elif diagnostic_counter[pos] > 500:
            binary_gamma_rate += '1'

    decimal_gamma_rate = int(binary_gamma_rate, 2)

    return binary_gamma_rate, decimal_gamma_rate

# Super duplicative... :/
def get_epsilon_rate(diagnostic_counter):

    binary_epsilon_rate = ''

    for pos in diagnostic_counter.keys():

        if diagnostic_counter[pos] > 500:
            binary_epsilon_rate += '0'
        elif diagnostic_counter[pos] < 500:
            binary_epsilon_rate += '1'

    decimal_epsilon_rate = int(binary_epsilon_rate, 2)

    return binary_epsilon_rate, decimal_epsilon_rate


def part1():

    input = ih.read_input('input.txt')
    diagnostic_counter = get_diagnostic_counter(input)
    binary_gamma_rate, gamma_rate = get_gamma_rate(diagnostic_counter)
    binary_epsilon_rate, epsiolon_rate = get_epsilon_rate(diagnostic_counter)
    power_consumption = calc_power_consumption(gamma_rate, epsiolon_rate)
    print(binary_gamma_rate)
    print(binary_epsilon_rate)
    print(power_consumption)


def get_life_support_rating(oxygen_generator_rating, co2_scrubber_rating):

    return oxygen_generator_rating * co2_scrubber_rating


def get_rating(diagnostic_report, common_or_uncommon):

    tmp_list = diagnostic_report
    i = 0
    while len(tmp_list) > 1:

        counter_dict = Counter(s[i] for s in tmp_list)

        if common_or_uncommon == 'common':

            # Find the mode of position i
            max_value_tuple = max(counter_dict.items(), key=lambda x:x[1])

            # If there are 2 modes (i.e. 500 0s, 500 1s in list of 1000)
            # then set criterion_value to 1
            if max_value_tuple[1] == sum(counter_dict.values()) / 2:
                criterion_value = 1
            else:
                criterion_value = max_value_tuple[0]

        elif common_or_uncommon == 'uncommon':
            # Find the least frequent of position i
            min_value_tuple = min(counter_dict.items(), key=lambda x: x[1])

            # If there are equal least frequent (i.e. 500 0s, 500 1s in list of 1000)
            # then set criterion_value to 0
            if min_value_tuple[1] == sum(counter_dict.values()) / 2:
                criterion_value = 0
            else:
                criterion_value = min_value_tuple[0]

        tmp_list = [x for x in tmp_list if x[i] == str(criterion_value)]

        i+=1

    return tmp_list[0]


def part2():

    input = ih.read_input('input.txt')

    oxygen_generator_rating = get_rating(input, common_or_uncommon='common')
    co2_scrubber_rating = get_rating(input, common_or_uncommon='uncommon')

    life_support_rating = get_life_support_rating(
        int(oxygen_generator_rating,2),
        int(co2_scrubber_rating,2)
    )

    print(life_support_rating)


if __name__ == '__main__':

    part2()

