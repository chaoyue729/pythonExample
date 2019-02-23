from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
y = ['A', 'B', 'A', 'A', 'B', 'C', 'C', 'A', 'C', 'B']
le.fit(y)
print(le.classes_)

y2 = le.transform(y) 
print(y2)
y3 = le.transform(['C'])
print(y3)

print(le.inverse_transform(y2))
print(le.inverse_transform(2))