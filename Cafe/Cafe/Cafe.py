import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('cafe.txt')

survived = data.groupby("Smoke").count()["Tip"]
print(survived)
survived.plot( kind="bar")
plt.show()


mor = data.query("Time == 'morning'").count()["PassengerId"]
aft = data.query("Time == 'afternoon'" ).count()["PassengerId"]
eve = data.query("Time == 'evening'").count()["PassengerId"]

survivedByAge = pd.Series([mor, aft,eve], index = ["Morning" , "Afternoon", "Evening"])
print(survivedByAge)
survivedByAge.plot(kind="bar")
plt.show()

mon = data.query("Day == 'monday'").count()["PassengerId"]
tu = data.query("Day == 'tuesday'" ).count()["PassengerId"]
wed = data.query("Day == 'wednesday'").count()["PassengerId"]
th = data.query("Day == 'thuersday'").count()["PassengerId"]
fr = data.query("Day == 'friday'" ).count()["PassengerId"]
sat = data.query("Day == 'saturday'").count()["PassengerId"]
sun = data.query("Day == 'sunday'").count()["PassengerId"]

survivedByDay = pd.Series([mon,tu,wed,th,fr,sat,sun], index = ["Mon" , "Tu", "Wed", "Th" , "Fr", "Sat", "Sun"])
print(survivedByDay)
survivedByDay.plot(kind="bar")
plt.show()


data.boxplot(column='Tip', by='Sex')
plt.show()

embarked = data.groupby("Tip").count()["PassengerId"]
print(embarked)
embarked.plot( kind="bar")
plt.show()

nosmok = data.query("Smoke == 0 and Tip").count()["PassengerId"]
smok = data.query("Smoke == 1 and Tip").count()["PassengerId"]


survivedByClass = pd.Series([nosmok, smok], index = ["No-Smoke" , "Smokee"])
print(survivedByClass)
survivedByClass.plot(kind="bar")
plt.show()
