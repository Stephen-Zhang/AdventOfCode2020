def open_input(filename, lambda_func):
  with open(f"PuzzleInputs/{filename}") as file:
    text = file.readlines()

  text = lambda_func([x.strip("\n") for x in text])
  return text


def get_bin_search(code, min_code, max_code, min, max):
  if code == "":
    return min

  if code[0] == min_code:
    return get_bin_search(code[1:], min_code, max_code, min, int((min+max)/2))
  elif code[0] == max_code:
    return get_bin_search(code[1:], min_code, max_code, int((min+max)/2)+1, max)
  else:
    raise RuntimeError(f"Next letter {code[0]} was not {min_code} or {max_code}")


def get_seat_id(input):
  row = get_bin_search(input[0], 'F', 'B', 0, 127)
  col = get_bin_search(input[1], 'L', 'R', 0, 7)

  return (row * 8 + col)


def puzzleA(input):
  val = [get_seat_id(x) for x in input]
  return max(val)


def puzzleB(input):
  val = sorted([get_seat_id(x) for x in input])
  min = val[0]

  for i in range(len(val)):
    if i != val[i] - min:
      return val[i] - 1

  return -1


def parse_input(raw_text):
  return [(x[:-3], x[-3:]) for x in raw_text]


def main():
  file_input = open_input("Puzzle5", parse_input)
  outputA = puzzleA(file_input)
  outputB = puzzleB(file_input)

  print(f"Puzzle 5: {outputA}, Puzzle 5: {outputB}")


if __name__ == "__main__":
  main()