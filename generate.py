#!/usr/bin/env python3
import json
import os
from pathlib import Path
import shutil


root = Path.cwd() / 'build'

if os.path.exists(root):
    shutil.rmtree(root)

# make build dir
os.mkdir(root)

# copy folder
shutil.copytree('recipes', root / 'recipes')
shutil.copytree('images', root / 'images')

# copy individual files
shutil.copy2('index.html', root)
shutil.copy2('recipe.html', root)
shutil.copy2('stylesheet.css', root)

# create json of recipes for nav-list
with open(root / 'recipelist.json', 'w') as f:
    # filter out dumb .DS_Store
    recipes = [fname for fname in os.listdir('recipes') if not fname.startswith('.')]
    f.write(json.dumps(recipes))
