def open_input(filename):
    with open(f"PuzzleInputs/{filename}") as file:
        text = file.readlines()

    text = list(map(lambda x: int(x.strip('\n')), text))

    text.sort()
    print(text)
    return text


def puzzle1A(list, target):
    start_ptr = 0
    end_ptr = len(list) - 1
    curr_total = list[start_ptr] + list[end_ptr]
    while curr_total != target:
        print(curr_total)
        if curr_total > target:
            end_ptr -= 1
        elif curr_total < target:
            start_ptr += 1
        else:
            break

        curr_total = list[start_ptr] + list[end_ptr]

    print(f"start: {start_ptr}, end: {end_ptr}")

    return list[start_ptr] * list[end_ptr]


def puzzle1B(list, target):
    ptr_1 = 0
    ptr_2 = 1
    end_ptr = len(list) - 1
    curr_total = list[ptr_1] + list[ptr_2] + list[end_ptr]
    while curr_total != target:
        print(curr_total)
        if curr_total > target:
            end_ptr -= 1
        elif curr_total < target:
            if (list[ptr_1+1] + list[ptr_2] > list[ptr_1] + list[ptr_2 + 1]):
                ptr_2 += 1
            else:
                ptr_1 += 1
                ptr_2 = ptr_1 + 1
        else:
            break

        curr_total = list[ptr_1] + list[ptr_2] + list[end_ptr]

    print(f"ptr 1: {ptr_1}, ptr 2: {ptr_2}, end: {end_ptr}")

    return list[ptr_1] * list[ptr_2] * list[end_ptr]


def main():
    file_input = open_input("Puzzle1A")
    outputA = puzzle1A(file_input, 2020)
    outputB = puzzle1B(file_input, 2020)
    print(f"Puzzle 1A: {outputA}, Puzzle 1B: {outputB}")


if __name__ == "__main__":
    main()
