import matplotlib.pyplot as plt

labels = ["Important/Very Important", "Not Important", "Other"]
values = [80, 6, 14]

fig, ax = plt.subplots()
ax.pie(values, labels=labels)
ax.show()
