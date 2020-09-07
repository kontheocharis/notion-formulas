if __name__ == '__main__':
    remove_time = lambda val: f'dateSubtract(dateSubtract({val}, hour({val}), "hours"), minute({val}), "minutes")'

    start_date = f'''if(empty(prop("Do on")), {remove_time('prop("Due")')} , {remove_time('prop("Do on")')})'''

    end_date = f'''if(empty(prop("Do on")), {remove_time('end(prop("Due"))')} , {remove_time('end(prop("Do on"))')})'''

    now = remove_time('now()')

    result = f'if( and( dateBetween({end_date}, {now}, "days") >= 0, dateBetween({start_date}, {now}, "days") <= 0), if( dateBetween({end_date}, {now}, "days") >= 1, "Today+Tomorrow", "Today"), if( and( dateBetween({end_date}, {now}, "days") >= 1, dateBetween({start_date}, {now}, "days") <= 1), "Tomorrow", if( dateBetween({start_date}, {now}, "days") <= -1, "Overdue", "Future")))'

    print(result.replace('\n', '').replace('\t', ''))

