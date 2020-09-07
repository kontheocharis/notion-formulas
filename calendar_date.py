if __name__ == '__main__':
    remove_time = lambda val: f'dateSubtract(dateSubtract({val}, hour({val}), "hours"), minute({val}), "minutes")'
    add_time = lambda a, b: f'dateAdd(dateAdd({a}, hour({b}), "hours"), minute({b}), "minutes")'

    weekly_rule = f'''
dateAdd(prop("Recurring date"), ceil(dateBetween({remove_time('now()')}, {remove_time('prop("Recurring date")')},  "days") / 7 * prop("Recurring every")) * 7 * prop("Recurring every"), "days")'''

    result = f'''
if(or(or(empty(prop("Recurring date")),empty(prop("Recurring"))), empty(prop("Recurring every"))),
if(empty(prop("Do on")), prop("Due"), prop("Do on")),
if(and(prop("Recurring") == "Weekly", timestamp(prop("Recurring date")) <= timestamp(now())), {weekly_rule}, prop("Do on"))
)
'''

    print(result.replace('\n', '').replace('\t', ''))
