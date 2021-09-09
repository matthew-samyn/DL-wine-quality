import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from functions import *

sns.set_style("darkgrid")

df = pd.read_csv("assignment-files/wine.csv")
df["target_text"] = df["target"].apply(lambda x: binary_to_text(x))

sns.catplot(data=df, x="target_text",kind="count")
plt.xlabel("Target")
plt.title("Distribution of data points")
plt.savefig("visuals/uneven_data.png",bbox_inches="tight")
plt.show()