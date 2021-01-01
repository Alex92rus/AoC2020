import string

passport_details = ['byr', 'iyr', 'eyr', 'hcl', 'ecl', 'hgt', 'pid']

def get_file_content(filename):
    with open(filename, 'r+') as f:
        return f.read().splitlines()

def check_if_all_details_present(passport_dict):
    return sum([1 if passport_detail in passport_dict  else 0 for passport_detail in passport_details]) == 7

def check_if_all_details_valid(passport_dict):
    if (check_if_all_details_present(passport_dict)):
        valid = True
        valid = valid and int(passport_dict['byr']) <= 2002
        valid = valid and int(passport_dict['byr']) >= 1920
        valid = valid and int(passport_dict['iyr']) >= 2010
        valid = valid and int(passport_dict['iyr']) <= 2020
        valid = valid and int(passport_dict['eyr']) >= 2020
        valid = valid and int(passport_dict['eyr']) <= 2030
        valid = valid and passport_dict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        valid = valid and passport_dict['pid'].isnumeric() and len(passport_dict['pid']) == 9
        valid = valid and passport_dict['hcl'][0] == '#'
        valid = valid and all(c in set(string.hexdigits) for c in passport_dict['hcl'][1:]) and len(passport_dict['hcl']) == 7
        hgt_valid = len(passport_dict['hgt']) > 2 and\
                    (passport_dict['hgt'][-2:] == 'cm' and 150 <= int(passport_dict['hgt'][:-2]) <= 193 or
                     (passport_dict['hgt'][-2:] == 'in' and 59 <= int(passport_dict['hgt'][:-2]) <= 76))
        valid = valid and hgt_valid
    else:
        return False
    return valid

def passports_filter(lines, predicate):
    result = 0
    passport_dict = {}
    for line in lines:
        key_pairs = line.split(" ")
        if len(line) < 2:
            if predicate(passport_dict):
                result += 1
            passport_dict = {}
            continue
        for pair in key_pairs:
            key_value = pair.split(':')
            passport_dict[key_value[0]] = key_value[1]
    return result

def solve_part_two(filename):
    lines = get_file_content(filename)
    detail_count = passports_filter(lines, predicate=check_if_all_details_valid)
    print('There are {} valid passports'.format(detail_count))

def solve_part_one(filename):
    lines = get_file_content(filename)
    detail_count = passports_filter(lines, predicate=check_if_all_details_present)
    print('There are {} passports with all required details'.format(detail_count))

if __name__ == '__main__':
    solve_part_one('day_4.txt')
    solve_part_two('day_4.txt')