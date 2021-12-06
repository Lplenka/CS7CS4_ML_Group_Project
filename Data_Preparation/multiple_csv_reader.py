import glob

myfiles = glob.glob('*.csv')
for file in myfiles:
    lines = open(file).readlines()
    second_line = lines[1]
    if 'SAO PAULO MIRANTE DE SANTANA, BR' in second_line:
        with open('filename.txt', 'a') as f:
            f.write(second_line + ' ; ' +  file +  '\n')
