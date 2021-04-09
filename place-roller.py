#!/usr/bin/python3

'''A small utility to roll 3 random natures for a new place to visit in wanderhome'''

import random

natures = {
    'Comfortable': ['Farm', 'Garden', 'Market', 'Monastery', 'Tower', 'Workshop'],
    'Verdant': ['Field', 'Glen', 'Hallow', 'Hillock', 'Lagoon', 'Swamp'],
    'Liminal': ['Bridge', 'Island', 'Lake', 'Port', 'Road', 'Tavern'],
    'Sprawling': ['Carnival', 'Castle', 'Furnace', 'Metropolis', 'Palace', 'University'],
    'Lonely': ['Cave', 'Graveyard', 'Mirage', 'Mirror', 'Moor', 'Wilderness'],
    'Desolate': ['Desert', 'Labyrinth', 'Maelstrom', 'Montain', 'Ruin', 'Waste']
    }

def rollPlace(First = False):
    d6_1 = random.randint(0, 5)
    d6_2 = random.randint(0, 5)
    d6_3 = random.randint(0, 5)
    d6s = (d6_1, d6_2, d6_3)
    if First:
        rolledNatures = [natures[key][d6] for key, d6 in zip(list(natures.keys())[:3], d6s)]
    else:
        rolledCategories = list(natures.keys())
        random.shuffle(rolledCategories)
        rolledNatures = [natures[key][d6] for key, d6 in zip(rolledCategories[:3], d6s)]
    return f"you rolled a {rolledNatures[0]}, a {rolledNatures[1]} and a {rolledNatures[2]}."


if __name__ == "__main__":
    print('Random starting place:', rollPlace("First"))
    print('Random place including rare natures:', rollPlace())


