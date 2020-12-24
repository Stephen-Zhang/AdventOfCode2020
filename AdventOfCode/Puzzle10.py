import math

def open_input(filename, lambda_func):
  with open(f"PuzzleInputs/{filename}") as file:
    text = file.readlines()

  text = lambda_func(text)
  return text


def puzzleA(input):
  sj = sorted(input + [0])
  sj.append(sj[-1]+3)  # target value
  sums = [0, 0, 0]
  for i in range(0, len(sj)-1):
    diff = sj[i+1] - sj[i]
    sums[diff-1] += 1

  print(sums)

  return sums[0] * sums[-1]


def puzzleB(input):
  sj = sorted(input + [0])
  sj.append(sj[-1]+3)  # target value

  possible_paths = [0] * len(sj)
  possible_paths[0] = 1
  for index in range(1, len(sj)):
    curr_value = sj[index]

    possible = list(map(lambda x: curr_value - sj[index - x] <= 3, [x for x in [3, 2, 1]]))

    if index < 2:
      possible[0] = False
    if index == 1:
      possible[1] = False

    func = lambda x: possible_paths[x] if (curr_value - sj[x] <= 3) else 0

    total_paths = sum(list(map(func, [index - x for x in [3, 2, 1]])))
    possible_paths[index] = total_paths

  return possible_paths[-1]

def parse_input(raw_text):
  parsed = list(map(lambda x: int(x.strip("\n")), raw_text))
  return parsed


def main():
  file_input = open_input("Puzzle10", parse_input)
  outputA = puzzleA(file_input)
  outputB = puzzleB(file_input)

  print(f"Puzzle 10: {outputA}, Puzzle 10: {outputB}")


if __name__ == "__main__":
  main()