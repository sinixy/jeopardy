from data.functions import getCategory, getDate, getNumber, getPrice, getRound
def getDataset(path):
    dataset = dict()
    try:
        with open(path, mode='r', encoding='utf-8') as file:
            header = [i.strip().lower() for i in file.readline().split(',')]
            for line in file:
                if not line:
                    continue
                number, new = getNumber(line)
                date, new = getDate(new)
                rnd, new = getRound(new)
                categ, new = getCategory(new)
                price, new = getPrice(new)
                if categ in dataset:
                    dataset[categ].extend([{'Show Number': number,
                                            'Air Date': date,
                                            'Round': rnd,
                                            'Value': price
                                            }])

                else:
                    dataset[categ] = [{'Show Number': number,
                                           'Air Date': date,
                                           'Round': rnd,
                                           'Value': price,
                                       }]
        return dataset
    except IOError as i_error:
        print('No such file', i_error.errno, i_error.strerror)
    except ValueError as v_error:
        print('ValueError', v_error)