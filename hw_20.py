def presidents():
    ukrainian_presidents = [
        'Леонід Кравчук',
        'Леонід Кучма',
        'Віктор Ющенко',
        'Віктор Янукович',
        'Олександр Турчинов',
        'Петро Порошенко',
        'Володимир Зеленський',
    ]
    for president in ukrainian_presidents:
        yield president


president_gen = presidents()
print(next(president_gen))
print(next(president_gen))
print(next(president_gen))
print(next(president_gen))
print(next(president_gen))
print(next(president_gen))
print(next(president_gen))
