ivan = {                           #объявляем Ивана
    "name": "ivan",
    "age":34,
    "children": [{
        "name":"vasja",
        "age":12,
    },{
        "name":"petja",
        "age":19,
    }],
}

darja = {                           #объявляем Дарью
    "name": "darja",
    "age":41,
    "children": [{
        "name":"kirill",
        "age":21,
    },{
        "name":"pavel",
        "age":15,
    }],
}

emps = [ivan,darja]

def ch(emps):
    for el in emps:           #обходим массив работников
        emp=el['children']
        for i,child in enumerate(emp):     #обходим детей работника
            if child['age']>18:            #если больше 18, то выводим имя работника
                print(el['name'])

ch(emps)