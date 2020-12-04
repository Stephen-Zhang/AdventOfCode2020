def open_input(filename, lambda_func):
  with open(f"PuzzleInputs/{filename}") as file:
    text = file.readlines()

  text = list(map(lambda_func, text))
  return text


def tree_collision_check(file_input, moveRight, moveDown):
  across = len(file_input[0])
  sum = 0
  current = 0

  for i in range(0, len(file_input), moveDown):
    row = file_input[i]
    if row[current] == '#':
      sum += 1
    current = (current + moveRight) % across

  return sum


def puzzleA(file_input):
  return tree_collision_check(file_input, 3, 1)


def puzzleB(file_input):
  return (tree_collision_check(file_input, 1, 1)
          * tree_collision_check(file_input, 3, 1)
          * tree_collision_check(file_input, 5, 1)
          * tree_collision_check(file_input, 7, 1)
          * tree_collision_check(file_input, 1, 2))


def main():
  file_input = open_input("Puzzle3", lambda x: x.strip('\n'))
  outputA = puzzleA(file_input)
  outputB = puzzleB(file_input)

  print(f"Puzzle 3A: {outputA}, Puzzle 3B: {outputB}")


if __name__ == "__main__":
  main()
