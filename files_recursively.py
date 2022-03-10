from pathlib import Path
import os


path = "~/PROJECTS/NEURA_NETW/"
# Recursively walk the tree
for root, dirs, files in os.walk(path):
    for file in files:
        Path(os.path.join(root, file)).touch()
