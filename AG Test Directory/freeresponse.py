import json
import os
files = os.listdir()
for file in files:
    if file.endswith('.ipynb'):
        answers = ''
        with open(file) as data:    
            nb = json.load(data)
        for cell in nb['cells']:
            if cell['cell_type'] == 'markdown':
                if 'source' in cell and len(cell['source']) > 0:
                    if cell['source'][0].startswith("<font color='blue'> ANSWER:"):
                        answers += ''.join(cell['source']) + '\n'          
        f = open('responses for ' + file[:-6] + '.txt', 'w')
        f.write(answers)
        f.close()