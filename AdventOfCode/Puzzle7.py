import re


def open_input(filename, lambda_func):
  with open(f"PuzzleInputs/{filename}") as file:
    text = file.readlines()

  text = lambda_func(text)
  return text


def reverse_mapping(map_of_colors):
  reversed_map = {x: [] for x in map_of_colors.keys()}

  for (entry, value) in map_of_colors.items():
    value_keys = value.keys()
    for bag in value_keys:
      reversed_map[bag].append(entry)

  return reversed_map

def puzzleA(input):
  tree = reverse_mapping(input)

  queue = ['shiny gold']

  found = set(['shiny gold'])

  count = 0

  while len(queue) != 0:
    next = queue.pop()

    for item in tree[next]:
      if item not in found:
        count += 1
        queue.append(item)
        found.add(item)

  return count


def get_all_sub_bags(input, bag_name):
  print(f"{bag_name}: {input[bag_name]}")

  total = 1
  for (bag, amount) in input[bag_name].items():
    total += amount * get_all_sub_bags(input, bag)

  print(f"{bag_name} total: {total}")
  return total


def puzzleB(input):
  return get_all_sub_bags(input, 'shiny gold') - 1


def parse_regex(line):
  regex = re.compile("(.*?) bags contain (.*?) bags?\.")
  match = regex.match(line)

  owner = match.group(1)
  contents = [x.strip() for x in match.group(2).replace("bags", "").replace("bag", "").split(",") if "no other" not in match.group(2)]
  contents = {x[1:].strip(): int(x[:1]) for x in contents}

  return (owner, contents)


def parse_input(raw_text):
  parsed = {x[0]: x[1] for x in list(map(parse_regex, raw_text))}
  return parsed


def main():
  file_input = open_input("Puzzle7", parse_input)
  outputA = puzzleA(file_input)
  outputB = puzzleB(file_input)

  print(f"Puzzle 7: {outputA}, Puzzle 7: {outputB}")


if __name__ == "__main__":
  main()