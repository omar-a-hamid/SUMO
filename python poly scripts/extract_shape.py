import csv

data_file = open('edges.csv','r')


reader = csv.reader(data_file, dialect='excel' )
counter = 0
shapes = []
x_cord=[]
y_cord=[]
for row in reader:
    if(not (counter)):
        counter +=1
        continue
        
    # print(row[6])
    list_shapes = row[6].split(' ')
    print(row[6].split(' '))
    for coordinates_pair in list_shapes:

        coordinates_pair_list =coordinates_pair.split(',')
        # print(coordinates_pair_list[0])

        # print ((coordinates_pair))
        # cords = map(float, coordinates_pair)
        # print (cords)
        x_cord.append(float(coordinates_pair_list[0]))
        y_cord.append(float(coordinates_pair_list[1]))
        # cord = map(float,coordinate)
        # print (cord)
        # print(coordinate)
    print(sum(x_cord)/len(x_cord),sum(y_cord)/len(y_cord))
    x_cord.clear()
    y_cord.clear()

    # value = map(int ,row[6].split(' '))
    # print(value)

