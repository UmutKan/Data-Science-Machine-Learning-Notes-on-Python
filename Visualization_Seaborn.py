# https://github.com/atilsamancioglu/PythonForDataScienceNotebooks/blob/main/11-VisualizationSeaborn.ipynb
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("athlete_events.csv")

# plt.scatter("Height", "Weight", data= data)
# plt.xlabel("Height")
# plt.ylabel("Weight")
# plt.show()

sns.set_style("whitegrid")
sns.scatterplot(x="Height", y="Weight", data= data)
plt.xlabel("Height of Athletes")
plt.ylabel("Weight of Athletes")
plt.title("Athletes' Weight vs Height")
plt.show()

sns.set_style("whitegrid")
sns.scatterplot(x="Height", y="Weight", hue="Sex", data= data)
plt.xlabel("Height of Athletes")
plt.ylabel("Weight of Athletes")
plt.title("Athletes' Weight vs Height")
plt.show()

#print(data["Medal"].unique()) # [nan 'Gold' 'Bronze' 'Silver']

sns.set_style("whitegrid")
sns.scatterplot(x="Height", y="Weight", hue="Sex", style="Medal", data= data)
plt.xlabel("Height of Athletes")
plt.ylabel("Weight of Athletes")
plt.title("Athletes' Weight vs Height")
plt.show()

sns.set_style("whitegrid")
sns.scatterplot(x="Height", y="Weight", hue="Sex", style="Medal",size="Age", data= data)
plt.xlabel("Height of Athletes")
plt.ylabel("Weight of Athletes")
plt.title("Athletes' Weight vs Height")
plt.show()

sns.set_style("whitegrid")
sns.lineplot(x="Height", y="Weight", hue="Sex", data= data)
plt.xlabel("Height of Athletes")
plt.ylabel("Weight of Athletes")
plt.title("Athletes' Weight vs Height")
plt.show()

sns.set_style("dark")
#sns.displot(x="Height", hue="Sex", data= data)
sns.displot(x="Height", hue="Sex", data= data, kind="kde") # kernel density estimate
plt.ylabel("Frequency")
plt.title("Athletes' Weight vs Height")
plt.show()

sns.barplot(x="Medal", y="Height", hue="Sex", data= data)
plt.title("Medals by Height")
plt.show()

sns.catplot(x="Medal", y="Height", hue="Sex", col="Season", data= data)
plt.show()

#print(data.corr(numeric_only=True))

sns.heatmap(data.corr(numeric_only=True), annot=True)
plt.show()