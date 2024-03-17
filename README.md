# Lab-7
Лабораторная работа №7

Использование NumPy и MatPlotLib

**Задание**

1. Библиотека NumPy имеет очень быстрые алгоритмы работы с массивами. Убедитесь в этом, сравнив время выполнения операции поэлементного перемножения стандартных списков
и массивов NumPy (```numpy.array```). Для каждого случая создайте два массива в 1 миллион элементов, заполненных случайными значениями чисел, и перемножьте их (в NumPy 
для этого служит функция ```numpy.multiply()```). Чтобы замерить время выполнения, воспользуйтесь функцией ```perf_counter``` из библиотеки ```time```.

2. Подгрузите один из двух приложенных файлов ```data1.csv``` и ```data2.csv```. Выделите данные из столбцов, указанных в вашем варианте и сгенерируйте из них график
(для ```data1.csv```) или гистограмму (для ```data2.csv```). В первом случае необходимо вывести два графика, наложенные друг на друга, а также график корреляции.
Во втором случае: гистограмму и среднеквадратичное отклонение. Количество столбцов в гистограмме произвольное, но не менее 16. Каждый график должен содержать заголовок и подписи по осям.

3. Постройте трёхмерный график согласно формуле из вашего варианта. Используйте ```Axes3d```. В интервалах потребуется ```np.linspace()```.

**Варианты**

| Вариант | Файл | Столбец(-цы) | Формулы |
| ------- | ---- | ------------ | ------- |
| 1 | data1.csv | 1 от 4 и 1 от 5 | x∈(-п;п); y=x; z=tg(x) |
| 2 | data2.csv | 1 | x∈(-2п;2п); y=sin(x)cos(x); z=sin(x)cos(x) |
| 3 | data1.csv | 1 от 4 и 1 от 18 | x∈(-5п;5п); y=cos(x); z=sin(x) |
| 4 | data2.csv | 2 | x∈(-5;5); y∈(-5;5); z=sin(x^y) |
| 5 | data1.csv | 1 от 4 и 1 от 16 | x∈(-п;п); y=sin(x)cos(x); z=sin(x) |
| 6 | data2.csv | 3 | x∈(-п;п); y=1/x; z=sin(x) |
| 7 | data1.csv | 1 от 4 и 1 от 10 | x∈(-10;10); y∈(-0,5;0,5); z=tg(x+y) |
| 8 | data2.csv | 4 | x∈(-3п;3п); y=cos(x); z=x/sin(x) |
| 9 | data1.csv | 1 от 10 и 1 от 16 | x∈(-5п;5п); y∈(-5п;5п); z=y cos(x) |
| 10 | data2.csv | 5 | x∈(-3п;3п); y=x cos(x); z=sin(x) |


**Дополнительное задание**

Создайте анимированный график функции y = sin(x) при помощи ```PillowWriter```.

**Полезные ссылки**  
NumPy:          https://habr.com/ru/post/352678/  
MatPlotLib:     https://matplotlib.org/stable/users/explain/quick_start.html  
PillowWriter:   https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.PillowWriter.html  
