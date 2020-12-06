def open_input(filename, lambda_func):
  with open(f"PuzzleInputs/{filename}") as file:
    text = file.readlines()

  text = lambda_func(text)
  return text


def puzzleA(input):
  yes = list(map(lambda y: set([x for x in "".join(y)]), input))
  yes_sum = sum(list(map(lambda x: len(x), yes)))
  return yes_sum



def make_intersection(row):
  intersection = set([x for x in row[0]])

  for answers in row[1:]:
    intersection = intersection.intersection(set([x for x in answers]))
  return intersection

def puzzleB(input):
  yes = list(map(make_intersection, input))
  yes_sum = sum(list(map(lambda x: len(x), yes)))
  return yes_sum


def parse_input(raw_text):
  converted = [x.replace("\n", " ").split(" ") for x in "".join(raw_text).split("\n\n")]
  return converted


def main():
  file_input = open_input("Puzzle6", parse_input)
  outputA = puzzleA(file_input)
  outputB = puzzleB(file_input)

  print(f"Puzzle 6: {outputA}, Puzzle 6: {outputB}")


if __name__ == "__main__":
  main()