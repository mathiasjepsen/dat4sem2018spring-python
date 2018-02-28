import matplotlib.pyplot as plt


squares = [x ** 2 for x in range(1,6)]  # [1, 4, 9, 16, 25]
plt.plot(squares)
plt.show()