#!/usr/bin/env python3

from termcolor import colored

mt = float(input(colored('> Введіть масу пацієнта в кг? ', 'blue')))
deficit_percents = float(input(colored('> Введіть степінь втрати оцк в відсотках (30% за замовчуванням)? ', 'blue')) or 30.0)
print(colored('Степінь втрати оцк {} відсотків.'.format(deficit_percents), 'green'))
deficit_ock = mt*65*deficit_percents/100
pat_vtraty = float(input(colored('> Введіть в мл об\'єм патологічних втрат (0 мл за замовчуванням)? ', 'blue')) or 0.0) 
print(colored('Патологічні втрати {} мл.'.format(pat_vtraty), 'green'))
print(colored('Дефіцит оцк - {} мл.'.format(deficit_ock), 'red'))

kristalloids_volume = deficit_ock*3
print(colored('Щоб відновити дефіцит оцк в {} мл, потрібно ввести {} мл кристалоїдів в/в.'.format(deficit_ock, kristalloids_volume), 'yellow'))

dobova_potreba = float(65 * mt)
dobova_potreba_v_chysty_vodi = dobova_potreba / 2
dobova_potreba_v_elektrolitah = dobova_potreba / 2

print('Добова фізіологічна потреба в рідині {} мл. \nПотреба в чистій воді - {} мл. \nПотреба в електролітах - {} мл.'.format(dobova_potreba, dobova_potreba_v_chysty_vodi, dobova_potreba_v_elektrolitah))

# потреба в електролітах 
# необхідний обєм кристалоїдів
# дефіцит оцк
# kristalloids_volume - deficit_ock те що з введеного об'єму кристалоїдів піде на добову потребу в електролітах
# dobova_potreba_v_elektrolitah - (kristalloids_volume - deficit_ock) 

add_electrolits = float(dobova_potreba_v_elektrolitah - (kristalloids_volume - deficit_ock) )
print('Щоб покрити добову потребу в електролітах {} мл, до об\'єму кристалоїдів {} мл, необхідного для покриття дефіциту оцк, слід додати ще {} мл електролітів.'.format(dobova_potreba_v_elektrolitah, kristalloids_volume, add_electrolits))


day_volume_elektrolits = float( kristalloids_volume + add_electrolits + pat_vtraty / 2)
day_volume_water = float( dobova_potreba_v_chysty_vodi + pat_vtraty / 2)

print(colored('Загальна добова потреба в електролітах - {} мл.'.format(day_volume_elektrolits), 'green'))
print(colored('Загальна добова потреба в чистій воді - {} мл.'.format(day_volume_water ), 'green'))

print('За перші 10 год ввести {} мл електролітів.'.format(float(day_volume_elektrolits*0.8)))
print('За перші 10 год ввести {} мл чистої води.'.format(float(day_volume_water*0.8)))

interval = float(input(colored('> Введіть мінімально допустимий інтервал між каплями в с (20 с за замовчуванням)? ', 'blue')) or 20.0) 
print(colored('Мінімально допустимий інтервал між каплями {} c.'.format(interval), 'green'))
speed = float(60*60/interval/20)
print('Швидкість ваша - {} мл/год.'.format(speed))
speed_needed = float(day_volume_elektrolits*0.8/10)
print('Швидкість необхідна - {} мл/год.'.format(speed_needed))
print('Необхідний інтервал - {} с'.format(float((60*60/(speed_needed*20)))))
