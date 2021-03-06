import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

# SubTask 1

# Рассмотрим все ту же функцию из задания по линейной алгебре: f(x) = sin(x / 5) exp(x / 10) + 5 exp(-x / 2),
# но теперь уже на промежутке [1, 30]
#
# В первом задании будем искать минимум этой функции на заданном промежутке с помощью scipy.optimize.
# Разумеется, в дальнейшем вы будете использовать методы оптимизации для более сложных функций,
# а f(x) мы рассмотрим как удобный учебный пример.
#
# Напишите на Питоне функцию, вычисляющую значение f(x) по известному x.
# Будьте внимательны: не забывайте про то,
# что по умолчанию в питоне целые числа делятся нацело, и о том,
# что функции sin и exp нужно импортировать из модуля math.


f = lambda x: np.sin(x / 5.0) * np.exp(x / 10.0) + 5 * np.exp(-x / 2.0)

x = np.arange(1.0, 30.0, 0.25)  # Массив значений аргумента
# plt.plot(x, f(x))  # Построение графика
# plt.xlabel('$x$')  # Метка по оси x в формате TeX
# plt.ylabel('$f(x)$')  # Метка по оси y в формате TeX
# plt.grid(True)  # Сетка
# plt.legend(('$f(x)$',))
# plt.show()  # Показать график

# Изучите примеры использования scipy.optimize.minimize в документации Scipy (см. "Материалы")
# Попробуйте найти минимум, используя стандартные параметры в функции scipy.optimize.minimize
# (т.е. задав только функцию и начальное приближение).
# Попробуйте менять начальное приближение и изучить, меняется ли результат.

x0 = np.random.choice(range(1, 31))
print("Начальное приближение x0 =", x0)
scipy.optimize.minimize(f, x0=x0)

# Укажите в scipy.optimize.minimize в качестве метода
# BFGS (один из самых точных в большинстве случаев градиентных методов оптимизации),
# запустите из начального приближения x=2.
# Градиент функции при этом указывать не нужно – он будет оценен численно.
# Полученное значение функции в точке минимума - ваш первый ответ по заданию 1,
# его надо записать с точностью до 2 знака после запятой.

answer1 = scipy.optimize.minimize(f, x0=2, method='BFGS')

# Теперь измените начальное приближение на x=30. Значение функции в точке минимума -
# ваш второй ответ по заданию 1, его надо записать через пробел после первого, с точностью до 2 знака после запятой.

answer2 = scipy.optimize.minimize(f, x0=30, method='BFGS')

with open('submission-1.txt', 'w') as file_obj:
    file_obj.write('%.2f %.2f' % (answer1.fun, answer2.fun))

# SubTask 2

# Теперь попробуем применить к той же функции f(x) метод глобальной оптимизации — дифференциальную эволюцию.
#
# Изучите документацию и примеры использования функции scipy.optimize.differential_evolution.
#
# Обратите внимание, что границы значений аргументов функции представляют собой
# список кортежей (list, в который помещены объекты типа tuple).
# Даже если у вас функция одного аргумента, возьмите границы его значений в квадратные скобки,
# чтобы передавать в этом параметре список из одного кортежа,
# т.к. в реализации scipy.optimize.differential_evolution длина этого списка
# используется чтобы определить количество аргументов функции.
#
# Запустите поиск минимума функции f(x) с помощью дифференциальной эволюции на промежутке [1, 30].
# Полученное значение функции в точке минимума - ответ в задаче 2.
# Запишите его с точностью до второго знака после запятой. В этой задаче ответ - только одно число.


answer = scipy.optimize.differential_evolution(f, bounds=[(1, 30)])

with open('submission-2.txt', 'w') as file_obj:
    file_obj.write('%.2f' % answer.fun)

# SubTask 3

# Теперь рассмотрим функцию h(x) = int(f(x)) на том же отрезке [1, 30],
# т.е. теперь каждое значение f(x) приводится к типу int и функция принимает только целые значения.


h_v = lambda x: int(f(x))

h = np.vectorize(h_v)

# Такая функция будет негладкой и даже разрывной, а ее график будет иметь ступенчатый вид.
# Убедитесь в этом, построив график h(x) с помощью matplotlib

# Такая функция будет негладкой и даже разрывной, а ее график будет иметь ступенчатый вид.
# Убедитесь в этом, построив график h(x) с помощью matplotlib


plt.plot(x, h(x))  # Построение графика
plt.xlabel('$x$')  # Метка по оси x в формате TeX
plt.ylabel('$h(x)$')  # Метка по оси y в формате TeX
plt.grid(True)  # Сетка
plt.legend(('$h(x)$',))
plt.show()  # Показать график

# Попробуйте найти минимум функции h(x) с помощью BFGS, взяв в качестве начального приближения x=30.
# Получившееся значение функции – ваш первый ответ в этой задаче.

answer1 = scipy.optimize.minimize(h, x0=30, method='BFGS')
print(answer1)

# еперь попробуйте найти минимум h(x) на отрезке [1, 30] с помощью дифференциальной эволюции.
# Значение функции h(x) в точке минимума – это ваш второй ответ в этом задании.
# Запишите его через пробел после предыдущего.

answer2 = scipy.optimize.differential_evolution(h, bounds=[(1, 30)])
print(answer2)

with open('submission-3.txt', 'w') as file_obj:
    file_obj.write('%.2f %.2f' % (answer1.fun, answer2.fun))
