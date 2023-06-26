import time

kata = (2019, 9, 25, 3, 30)
time_tuple = kata + (0, 0, 0, 0)
#on a besoin d'un tuple de taille 9...
date_str = time.strftime("%m/%d/%Y %H:%M", time_tuple)
print(date_str)