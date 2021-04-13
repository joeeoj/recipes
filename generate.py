#!/usr/bin/env python3
import json
import os
import shutil


if os.path.exists("build"):
    shutil.rmtree("build")

# make build dir
os.mkdir("build")

# copy folder
shutil.copytree("recipes", "build/recipes")
shutil.copytree("images", "build/images")

# copy individual files
shutil.copy2("index.html", "build")
shutil.copy2("recipe.html", "build")
shutil.copy2("stylesheet.css", "build")

# create json of recipes for nav-list
with open('build/recipelist.json', 'w') as f:
    f.write(json.dumps(os.listdir("recipes")))
