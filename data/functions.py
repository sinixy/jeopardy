import re
def getNumber(line):
    result = re.split(r',', line, maxsplit=1)
    return result[0], result[1]

def getDate(line):
    result = re.split(r',', line, maxsplit=1)
    date = re.search(r'\d{4}-\d{2}-\d{2}', result[0])
    if date:
        return date.group(), result[1]
    else:
        return '', result[1]

def getRound(line):
    result = re.split(r',', line, maxsplit=1)
    return result[0], result[1]

def getCategory(line):
    result = re.split(r',', line, maxsplit=1)
    category = re.search(r'[a-zA-Z\d\-]+', result[0])
    if category:
        return category.group(), result[1]
    else:
        return '', result[1]

def getPrice(line):
    result = re.split(r',', line, maxsplit=1)
    price = re.search(r'\d+', line)
    if price:
        return int(price.group()), result[1]
    else:
        return 0, result[1]

try:
    with open('JEOPARDY_CSV.csv', mode='r', encoding='utf-8') as file:
        header = [i.strip().lower() for i in file.readline().split(',')]
        categ_index = header.index('category')

except IOError as i_error:
    print('No such file', i_error.errno, i_error.strerror)
except ValueError as v_error:
    print('ValueError', v_error)