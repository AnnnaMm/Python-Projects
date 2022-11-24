
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('titanic.txt')

#a) Przeżyli – ile osób przeżyło, a ile zginęłosurv = data.groupby("Survived").count()["PassengerId"]
surv = data.groupby("Survived").count()["PassengerId"]
print("Przeżyli(Survived)-nie przeżyli - ile osób przeżyło, a ile zginęło")
print(surv)
surv.plot( kind="pie")
plt.show()


#b) przetrwały według klasy, w wartościach bezwzględnych i względnych
v = data.query("Pclass==1 and Survived==1").count()["PassengerId"]
m = data.query("Pclass==2 and Survived==1").count()["PassengerId"]
c = data.query("Pclass==3 and Survived==1").count()["PassengerId"]
surv_by_class = pd.Series([v, m, c], index = ["Vip" , "Middle", "Cheap"])
print("przeżył według klas, w wartościach bezwzględnych i względnych")
print(surv_by_class)
surv_by_class.plot(kind="bar", color = "green")
plt.show()

#c) przeżył wiek (Age) - młody - do 30 lat, w średnim wieku - do 60 lat, starszy > 60
y = data.query("Age < 30").count()["PassengerId"]
m = data.query("Age >= 30 and Age < 60").count()["PassengerId"]
o = data.query("Age >= 60").count()["PassengerId"]

surv_by_age = pd.Series([y, m, o], index = ["Young" , "Mid", "Old"])
print("przeżył wiek (Age) – młody – do 30 lat, średni – do 60 lat, starszy > 60")
print(surv_by_age)
surv_by_age.plot(kind="line", color = "purple")
plt.show()


#d) według pochodzenia - znajdź, skąd przybyło najwięcej pasażerów (Embarked)
emb = data.groupby("Embarked").count()["PassengerId"]
print("według pochodzenia - sprawdź, skąd przybyło najwięcej pasażerów (Embarked)")
print(emb)
emb.plot( kind="bar")
plt.show()


#e) jaka opłata zależy od klasy kabiny (Pclass) -> boxplot
data.boxplot(column='Fare', by='Pclass')
plt.show()

