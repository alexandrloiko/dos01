import math ##импорт математической библиотеки
print ("Введите координаты точки A: ") ##ввод для точки А
a_x = int(input('x: '))
a_y = int(input('y: '))

print ("Введите координаты точки B: ")  ##ввод для точки B
b_x = int(input('x: '))
b_y = int(input('y: '))

ab = math.sqrt ((b_x-a_x)**2 + (b_y-a_y)**2) ##формула расчета

print ("AB = ",'%.3f' % ab)  ##вывод до трех знаков после запятой
