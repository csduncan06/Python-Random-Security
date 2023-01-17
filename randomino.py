import string
import random

random_chars = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(1000))

character_appearances = {}
for character in random_chars:
    if character in character_appearances:
        character_appearances[character] += 1
    else:
        character_appearances[character] = 1


for character, count in character_appearances.items():
    print(f'{character}: {count}')
