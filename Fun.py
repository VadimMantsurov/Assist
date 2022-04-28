import numpy as np
import matplotlib.pyplot as plt

while True :
    name_fun = input("Введите функцию: ")

    if "косинус" in name_fun :
        y = lambda x: np.cos(x)
        fig = plt.subplots()
        x = np.arange(-10, 10, 0.5)
        plt.plot(x, y(x))
        plt.show()
    elif "экспонента" in name_fun:
        y = lambda x: np.exp(x)
        fig = plt.subplots()
        x = np.arange(-10, 10, 0.5)
        plt.plot(x, y(x))
        plt.show()
    elif "синус" in name_fun:
        y = lambda x: np.sin(x)
        fig = plt.subplots()
        x = np.arange(-10, 10, 0.5)
        plt.plot(x, y(x))
        plt.show()
    #     По такому принципу можно добавить и другие функции
    else:
        print("Unknown command")
        break



