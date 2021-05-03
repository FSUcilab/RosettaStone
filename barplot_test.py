import matplotlib.pyplot as plt
import seaborn as sns

x = [10,11,12]
y = [20,25,30]
ax = sns.barplot(x=x, y=y)
ax.set_xlim(0, 20)
plt.show()
