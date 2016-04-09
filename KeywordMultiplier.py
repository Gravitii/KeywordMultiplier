

cityTuples = [
    ('Charlotte', 'NC'),
    ('Raleigh', 'NC'),
    ('Greensboro', 'NC'),
    ('Durham', 'NC'),
    ('Winston-Salem', 'NC'),
    ('Fayetteville', 'NC'),
    ('Cary', 'NC'),
    ('Wilmington', 'NC'),
    ('High Point', 'NC'),
    ('Greenville', 'NC'),
    ('Asheville', 'NC')
]

nicheList = [
    'seo',
    'internet marketing',
    'digital marketing',
]

titleList = [
    'consultant',
    'agency',
    'expert',
    'firm',
    'company'
]

modifierList = [
    'near',
    'in',
]
kwList = list()

#city + niche
#niche + city
for city in cityTuples:
    string = ""
    for niche in nicheList:
        for title in titleList:
            kwList.append(city[0] + ' ' + niche)
            kwList.append(niche + ' ' + city[0])

#city + niche + title
for city in cityTuples:
    string = ""
    for niche in nicheList:
        for title in titleList:
            kwList.append(city[0] + ' ' + niche + ' ' + title)

#niche + title + city
for city in cityTuples:
    string = ""
    for niche in nicheList:
        for title in titleList:
            kwList.append(niche + ' ' + title + ' ' + city[0])

#niche + title + mod + city
for city in cityTuples:
    string = ""
    for niche in nicheList:
        for title in titleList:
            for mod in modifierList:
                kwList.append(niche + ' ' + title + ' ' + mod + ' ' + city[0])

#niche + title + city + state
for city in cityTuples:
    string = ""
    for niche in nicheList:
        for title in titleList:
            kwList.append(niche + ' ' + title + ' ' + city[0]  + ' ' + city[1])

#niche + title + mod + city + state
for city in cityTuples:
    string = ""
    for niche in nicheList:
        for title in titleList:
            for mod in modifierList:
                kwList.append(niche + ' ' + title + ' ' + mod + ' ' + city[0]  + ' ' + city[1])

f = open('C:\\Users\\Brendan\\Documents\\kwList.txt', 'w')
for kw in kwList:
    f.write(kw + '\n')
f.close()

print('Finished! \n# of keywords: ' + str(len(kwList)))