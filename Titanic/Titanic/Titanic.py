import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter


data = pd.read_csv('titanic.txt', sep = ",")


survived = data.groupby("Survived").count()["PassengerId"]
print(survived)
survived.plot( kind="bar", title = "Amount of survived passangers")
plt.gca().yaxis.set_major_formatter(PercentFormatter(sum(survived)))
plt.show()



young = data.query("Age < 30").count()["PassengerId"]
mid = data.query("Age >= 30 and Age < 60").count()["PassengerId"]
old = data.query("Age >= 60").count()["PassengerId"]

survivedByAge = pd.Series([young, mid,old], index = ["Young" , "Mid", "Old"])
print(survivedByAge)
survivedByAge.plot(kind="bar", color='pink', title = "Passangers age")
plt.show()


data.boxplot(column='Fare', by='Pclass')
plt.show()

embarked = data.groupby("Embarked").count()["PassengerId"]
print(embarked)
embarked.plot( kind="line")
plt.show()

vip = data.query("Pclass==1 and Survived==1").count()["PassengerId"]
middle = data.query("Pclass==2 and Survived==1").count()["PassengerId"]
cheap = data.query("Pclass==3 and Survived==1").count()["PassengerId"]

survivedByClass = pd.Series([vip, middle, cheap], index = ["VIP" , "Middle", "Cheap"])
print(survivedByClass)
survivedByClass.plot(kind="pie")
plt.show()

vart=data["Fare"].mean()
print(vart)