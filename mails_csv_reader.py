from csv import reader
def read_data_from_csv():
    to = []
    with open('gmails.csv', mode ='r')as file:
        csvFile = reader(file)
        next(csvFile)
        for lines in csvFile:
                for ele in lines:
                    to.append(ele)
    return to