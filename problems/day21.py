from problems.common import get_input_of_day


def process_input(input_list):
    foods = []
    for line in input_list:
        clean = line.strip()
        split = clean.split('(')
        ingredients = set()
        for word in split[0].split(' '):
            clean_word = word.strip()
            if clean_word != '':
                ingredients.add(clean_word)
        allergens = set()
        for word in split[1][8:-1].split(','):
            clean_word = word.strip()
            if clean_word != '':
                allergens.add(clean_word)
        foods.append((ingredients, allergens))
    return foods


def build_allergen_map(foods):
    allergen_map = {}
    for ingredients, allergens in foods:
        for allergen in allergens:
            if allergen not in allergen_map:
                allergen_map[allergen] = ingredients
            else:
                allergen_map[allergen] = allergen_map[allergen].intersection(ingredients)
    return allergen_map


def solve_part1(input_list):
    foods = process_input(input_list)
    allergen_map = build_allergen_map(foods)
    potential_allergenic_foods = {x for value in allergen_map.values() for x in value}
    return len([x for ingredients, allergens in foods for x in ingredients if x not in potential_allergenic_foods])


def solve_part2(input_list):
    foods = process_input(input_list)
    allergen_map = build_allergen_map(foods)
    new_allergen_map = {}
    while len(allergen_map) != 0:
        for key, values in allergen_map.items():
            if len(values) == 1:
                break
        new_allergen_map[key] = values.pop()
        del allergen_map[key]
        for other_key, other_values in allergen_map.items():
            if new_allergen_map[key] in other_values:
                other_values.remove(new_allergen_map[key])
    sorted_allergens = sorted(list(new_allergen_map.items()))
    return ','.join([ingredient for _, ingredient in sorted_allergens])


if __name__ != 'main':
    print(solve_part1(get_input_of_day(21)))
    print(solve_part2(get_input_of_day(21)))
