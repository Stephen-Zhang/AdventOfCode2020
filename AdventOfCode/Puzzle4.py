import re

def open_input(filename, lambda_func):
  with open(f"PuzzleInputs/{filename}") as file:
    text = file.readlines()

  text = lambda_func(text)
  return text


def validate_passport(passport):
  return (validate_byr(passport["byr"]) and
          validate_iyr(passport["iyr"]) and
          validate_eyr(passport["eyr"]) and
          validate_hgt(passport["hgt"]) and
          validate_hcl(passport["hcl"]) and
          validate_ecl(passport["ecl"]) and
          validate_pid(passport["pid"]))


def validate_byr(input):
  return len(input) == 4 and int(input) >= 1920 and int(input) <= 2002


def validate_iyr(input):
  return len(input) == 4 and int(input) >= 2010 and int(input) <= 2020


def validate_eyr(input):
  return len(input) == 4 and int(input) >= 2020 and int(input) <= 2030


def validate_hgt(input):
  if len(input) <= 2:
    return False

  metric = input[-2:]
  val = int(input[:-2])
  out = False
  if metric == 'cm':
    out = val >= 150 and val <= 193
  elif metric == 'in':
    out = val >=59 and val <= 76

  return out


def validate_hcl(input):
  regex = re.compile("^#[0-9a-f]{6}$")
  match = regex.match(input)
  return match is not None


def validate_ecl(input):
  return input in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def validate_pid(input):
  regex = re.compile("^[0-9]{9}$")
  match = regex.match(input)
  return match is not None


def puzzleA(passports):
  required = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

  valid_passports = list(filter(lambda x: len(required.difference(set(x.keys()))) == 0, passports))

  return len(valid_passports)


def puzzleB(passports):
  required = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

  valid_passports = list(filter(lambda x: len(required.difference(set(x.keys()))) == 0 and validate_passport(x), passports))

  return len(valid_passports)


def parse_input(raw_text):
  converted = [x.replace("\n", " ").split(" ") for x in "".join(raw_text).split("\n\n")]
  output_map = []

  for row in converted:
    dictionary = {x.split(":")[0]: x.split(":")[1] for x in row}
    output_map.append(dictionary)

  return(output_map)


def main():
  file_input = open_input("Puzzle4", parse_input)
  outputA = puzzleA(file_input)
  outputB = puzzleB(file_input)

  print(f"Puzzle 4: {outputA}, Puzzle 4: {outputB}")


if __name__ == "__main__":
  main()
