import os
from PIL import Image

for path, currentDirectory, files in os.walk("/usr/share/backgrounds"):

    for file in files:
        print(os.path.join(path, file))
        input_image = Image.open(os.path.join(path, file))

        output = input_image.resize((1920, 1080))
        output.save(os.path.join(path, file) + "_resized.png")
