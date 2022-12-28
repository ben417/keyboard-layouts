from pathlib import Path
import yaml

layouts = dict()

for file in Path(".").glob("*.yml"):
    with file.open('r') as stream:
        layouts[file.name] = yaml.safe_load(stream)

for layout in layouts.values():
    if layout['parent']:
        parent_layout = layouts[layout['parent']]
        layout['keys']


print(layouts)