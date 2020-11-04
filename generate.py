#!/usr/bin/python3
import os, json, shutil
if os.path.exists("build"):
    shutil.rmtree("build")
os.mkdir("build")
shutil.copytree("recipes", "build/recipes")
shutil.copytree("images", "build/images")
shutil.copy2("index.html", "build")
shutil.copy2("recipe.html", "build")
shutil.copy2("stylesheet.css", "build")
f = open("build/recipelist.json", "w")
f.write(json.dumps(os.listdir("recipes")))
