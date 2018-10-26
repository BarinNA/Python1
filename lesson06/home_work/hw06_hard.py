# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import module_hard
import os



#Прочитаем сотрудников
path_workers = os.path.join(os.getcwd(),'lesson06','home_work','data', 'workers.txt')  
info = module_hard.readfile(path_workers)

Workers = module_hard.workers()

for l in info[1:]:
    worker = module_hard.worker(l)
    Workers.add_worker(worker)

#Прочитаем табель
path_table = os.path.join(os.getcwd(),'lesson06','home_work','data', 'hours_of.txt')  
info = module_hard.readfile(path_table)

for l in info[1:]:
    table = module_hard.table(l, Workers)
    Workers.add_table(table)

Workers.calculate()
Workers.printcalculation()



    
