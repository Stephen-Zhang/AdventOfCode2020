def open_input(filename, lambda_func):
  with open(f"PuzzleInputs/{filename}") as file:
    text = file.readlines()

  text = lambda_func(text)
  return text


def run_program(input):
  visited = [False] * len(input)
  ptr = 0
  acc = 0

  while ptr != len(input) - 1:
    if visited[ptr]:
      return (acc, False)

    (action, num) = input[ptr].split(" ")
    if action == 'acc':
      visited[ptr] = True
      acc += int(num)
      ptr += 1
    elif action == 'jmp':
      visited[ptr] = True
      ptr += int(num)
    elif action == 'nop':
      visited[ptr] = True
      ptr += 1

  return (acc, True)

def puzzleA(input):
  return run_program(input)


def puzzleB(input):
  all_possible_inputs = []

  for i in range(len(input)):
    (action, num) = input[i].split(" ")
    if action == 'acc':
      continue
    elif action == 'jmp':
      new_input = input.copy()
      new_input[i] = f"nop {num}"
      all_possible_inputs.append(new_input)
    elif action == 'nop':
      new_input = input.copy()
      new_input[i] = f"jmp {num}"
      all_possible_inputs.append(new_input)

  for possibility in all_possible_inputs:
    (result, noloop) = run_program(possibility)
    if noloop:
      return result

  return -1


def parse_input(raw_text):
  return [x.strip("\n") for x in raw_text]


def main():
  file_input = open_input("Puzzle8", parse_input)
  outputA = puzzleA(file_input)
  outputB = puzzleB(file_input)

  print(f"Puzzle 8: {outputA}, Puzzle 8: {outputB}")


if __name__ == "__main__":
  main()