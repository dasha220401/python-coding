def parse(rules):
    res = []
    value = 0
    for rule in rules:
        if rule == 'i':
            value +=1
        elif rule == 's':
            value *= value
        elif rule == 'd':
            value -= 1
        elif rule == 'o':
            res.append(value)
    return res


print(parse("iiisdoso"))