from datetime import datetime
def get_str_date(date):
    x=str(date).split(' ')
    c=x[0].split('-')
    string_data=datetime(year=int(c[0]),month=int(c[1]),day=int(c[2]))
    return string_data.strftime('%A')

def get_birthdays_per_week(users):
    days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    b=[{"Monday":[]},
    {"Tuesday":[]},
    {"Wednesday":[]},
    {"Thursday":[]},
    {"Friday":[]},
    ]
    lst_days=[]

    for i in users:
        for k,v in i.items():
            day=get_str_date(v)
            yes=False
            for t in b:
                    for n,l in t.items():
                            if n==day:
                                l.append(k)
                                yes=True
                            elif day=='Sunday' or day=='Saturday':
                                l.append(k)
                                yes=True
                    if yes:
                         break
    for j in b:
        for keys, value in j.items():
            if len(value)==0:
                continue
            else:
                a=', '.join(value)
                lst_days.append(f'{keys}: {a}')

    return  '\n'.join(lst_days)
if __name__ == "__main__" :
    print(get_birthdays_per_week([{'Illy':datetime(year=2023, month=1, day=21)},{'Mia':datetime(year=2023, month=1, day=19)},{'Nina':datetime(year=2028, month=10, day=9)}]))
                                