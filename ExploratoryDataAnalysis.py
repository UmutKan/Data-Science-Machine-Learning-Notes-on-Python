import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

wine_data = pd.read_csv('13-WineQT.csv')
# print( wine_data.info())
# print( wine_data.corr())
# print( wine_data.groupby("quailty").mean())
# sns.heatmap(wine_data.corr(), annot=True)
# plt.show()
# #sns.pairplot(wine_data)

plt.subplot(1,2,1)
sns.boxplot(x="quality", y="alcohol", data= wine_data)
plt.title("Quality vs pH")
plt.subplot(1,2,2)
sns.barplot(x="quality", y="volatile acidity", data= wine_data)
plt.title("quality vs volatile acidity")
#plt.show()

columns = wine_data.columns
fig , ax = plt.subplots(4, 4, figsize=(16,15))
ax = ax.flatten()

for i, column in enumerate(columns):
    sns.kdeplot(
        data= wine_data,
        x= column,
        hue= wine_data.quality,
        ax= ax[i]
    )
    ax[i].set_title(f"{column} Distribution")
    ax[i].set_xlabel(None)

for i in range(i+1, len(ax)):
    ax[i].axis("off")

plt.show()