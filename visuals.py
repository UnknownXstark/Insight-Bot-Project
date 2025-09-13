# import pandas as pd

# df = pd.read_csv("output.csv")

# print(df.head())

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_csv("output.csv")


text = " ".join(df["Headline"].astype(str))


wc = WordCloud(width=800, height=400, background_color="white").generate(text)

plt.figure(figsize=(10,5))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.title("BBC Headlines Word Cloud", fontsize=16)
plt.show()
