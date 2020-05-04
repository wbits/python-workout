import json
import os

filename = input('class name: ') + '.json'
directory = 'sccores'
science = ()
literature = ()
math = ()

with open(os.path.join(directory, filename)) as json_file:
    scores = json.load(json_file)
    for score in scores:
        science += (score['science'],)
        literature += (score['literature'],)
        math += (score['math'],)

    print(f'scores {os.path.join(directory, filename)}:')
    print(f'\tscience: min {min(science)}, max {max(science)}, avg: {sum(science) / len(science)}')
    print(f'\tliterature: min {min(literature)}, max {max(literature)}, avg: {sum(literature) / len(literature)}')
    print(f'\tmath: min {min(math)}, max {max(math)}, avg: {sum(math) / len(math)}')

exit(0)
