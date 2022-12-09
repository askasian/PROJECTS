import seaborn as sns

palette = sns.color_palette(None, 4, desat=None)


def init_colors():
    return palette.as_hex()


colors = init_colors()
print(colors)
