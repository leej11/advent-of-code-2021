import input_handler as ih
from typing import List

input = ih.read_input('input.txt')

def input_splitter(input_list: List[str]):
    instructions = []
    for ins in input_list:
        instructions.append([int(i) if i.isdigit() else i for i in ins.split()])
    return instructions


def part1_instruction_parsing(instructions, h, d):

    for instruction in instructions:
        if instruction[0] == 'forward':
            h += instruction[1]
        elif instruction[0] == 'down':
            d += instruction[1]
        elif instruction[0] == 'up':
            d -= instruction[1]
        else:
            raise ValueError(f"Could not handle {instruction[0], instruction[1]}")

    return h, d

def part2_instruction_parsing(instructions, h, d, a):

    for instruction in instructions:
        if instruction[0] == 'forward':
            h += instruction[1]
            d += instruction[1] * a
        elif instruction[0] == 'down':
            a += instruction[1]
        elif instruction[0] == 'up':
            a -= instruction[1]

    return h, d, a

def parse_instructions(instructions, h, d, a=None):

    if a != None:
        print("Using part 2 parser")
        h, d, _ = part2_instruction_parsing(instructions, h, d, a)
    else:
        print("Using part 1 parser")
        h, d = part1_instruction_parsing(instructions, h, d)

    return h, d

def part1():

    instructions = input_splitter(input)
    h, d = parse_instructions(instructions, 0, 0)
    print(f"End Horizontal: {h}\nEnd Depth: {d}\nMultiplication: {h*d}")

def part2():

    instructions = input_splitter(input)
    h, d = parse_instructions(instructions, h=0, d=0, a=0)
    print(f"End Horizontal: {h}\nEnd Depth: {d}\nMultiplication: {h * d}")

if __name__ == '__main__':
    print("Part 1")
    part1()
    print("Part 2")
    part2()




