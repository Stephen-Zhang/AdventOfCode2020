def open_input(filename, lambda_func):
  with open(f"PuzzleInputs/{filename}") as file:
    text = file.readlines()

  text = lambda_func(text)
  return text


def puzzleA(input):
  pass


def puzzleB(input):
  pass

def parse_input(raw_text):
  pass


def main():
  file_input = open_input("PuzzleX", parse_input)
  outputA = puzzleA(file_input)
  outputB = puzzleB(file_input)

  print(f"Puzzle X: {outputA}, Puzzle X: {outputB}")


if __name__ == "__main__":
  main()