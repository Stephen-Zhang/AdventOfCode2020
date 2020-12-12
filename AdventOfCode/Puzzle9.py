import bisect

def open_input(filename, lambda_func):
  with open(f"PuzzleInputs/{filename}") as file:
    text = file.readlines()

  text = lambda_func(text)
  return text


def find_pair(arr, v):
  start = 0
  end = len(arr)-1

  while start != end:
    if arr[start] + arr[end] == v:
      return True
    elif arr[start] + arr[end] > v:
      end -= 1
    elif arr[start] + arr[end] < v:
      start += 1
  return False


def puzzleA(input):
  sorted_sliding = sorted(input[0:25])

  for i in range(25, len(input)):
    first_ele = input[i - 25]
    new_ele = input[i]

    if not find_pair(sorted_sliding, new_ele):
      return input[i]

    bisect.insort(sorted_sliding, new_ele)
    sorted_sliding.remove(first_ele)

  return -1


def puzzleB(input, target):
  ptr = 2
  start = 0
  sliding_window = sorted(input[start:ptr])
  while ptr < len(input):
    total = sum(sliding_window)

    if total == target:
      return sliding_window[0] + sliding_window[-1]
    if total < target:
      bisect.insort(sliding_window, input[ptr])
      ptr += 1
    elif total > target:
      sliding_window.remove(input[start])
      start += 1

  return -1

def parse_input(raw_text):
  parsed = list(map(lambda x: int(x.strip("\n")), raw_text))
  return parsed

def main():
  file_input = open_input("Puzzle9", parse_input)
  outputA = puzzleA(file_input)
  outputB = puzzleB(file_input, outputA)

  print(f"Puzzle 9: {outputA}, Puzzle 9: {outputB}")


if __name__ == "__main__":
  main()