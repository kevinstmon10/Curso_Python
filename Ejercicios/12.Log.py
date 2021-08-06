from datetime import datetime

print(datetime.now())

with open('log.txt', 'a') as file:
    file.write('el archivo corrio a las: {0}\n'.format(datetime.now()))
    file.close()
