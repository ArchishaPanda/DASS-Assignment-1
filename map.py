import matplotlib.pyplot as plt

def move_person(start, commands):
    x, y = start
    positions = [(x, y)]

    for distance, direction in commands:
        if direction == 'N':
            y += distance
        elif direction == 'S':
            y -= distance
        elif direction == 'E':
            x += distance
        elif direction == 'W':
            x -= distance
        elif direction == 'NW':
            x -= distance / 1.414
            y += distance / 1.414
        elif direction == 'NE':
            x += distance / 1.414
            y += distance / 1.414
        elif direction == 'SW':
            x -= distance / 1.414
            y -= distance / 1.414
        elif direction == 'SE':
            x += distance / 1.414
            y -= distance / 1.414

        positions.append((x, y))

    return positions

def print_current_location(x,y):
    if x==0 and y>0:
        print("P is in North wrt S")
    elif x==0 and y<0:
        print("P is in South wrt S")
    elif y==0 and x>0:
        print("P is in East wrt S")
    elif y==0 and x<0:
        print("P is in West wrt S")
    elif x>0 and y>0:
        print("P is in North-East wrt S")
    elif x>0 and y<0:
        print("P is in South-East wrt S")
    elif x<0 and y>0:
        print("P is in North-West wrt S")
    elif x<0 and y<0:
        print("P is in South-West wrt S")
    else:
        print("P is the same position as S")

def calc_dist(point1,point2):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]

    dist = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return dist

def take_input():
    print("What mode of input would you like to give?")
    print("1. Terminal")
    print("2. File input")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Keep entering commands in specified format and write STOP at the end of sequence")
        print("Format: Magnitude Direction")
        print("Example: (3mm,N), (4.5cm,NW), (2mm,SE)")
        while True:
            cmd = input("Enter your command: ")
            if cmd == "STOP":
                break
            else:
                mag_dir = cmd.split(',')
                mag = mag_dir[0]
                dir = mag_dir[1]
                if mag[-2]=='m':
                    new_mag = float(mag[0:len(mag)-2])
                    commands.append((new_mag,dir))
                else:
                    new_mag = float(mag[0:len(mag)-2])*10
                    commands.append((new_mag,dir))                   
                
    elif choice == 2:
        input_file = input("Enter the filename: ")
        with open(input_file,'r') as file:
            lines = file.readlines()
            for line in lines:
                l1 = line.strip().split(',')
                mag = l1[0]
                dir = l1[1]
                if mag[-2]=='m':
                    new_mag = float(mag[0:len(mag)-2])
                    commands.append((new_mag,dir))
                else:
                    new_mag = float(mag[0:len(mag)-2])*10
                    commands.append((new_mag,dir))            

commands = []
take_input()
start_location = (0, 0)
path = move_person(start_location, commands)

x_values, y_values = zip(*path)

plt.plot(x_values[0], y_values[0], marker='o', color='r')
plt.scatter(x_values[1:], y_values[1:], marker='o', color='b')
plt.plot(*start_location, color='r', label='Start Location')
for i, (x, y) in enumerate(path):
    plt.annotate(f'{i+1}', (x, y), textcoords="offset points", xytext=(0,10), ha='center')

for i in range(1, len(path)):
    plt.plot([path[i-1][0], path[i][0]], [path[i-1][1], path[i][1]], color='green', linestyle='-', linewidth=1)

plt.title('Person P Movement in 2D World')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.legend()
plt.grid(False)
plt.show()

x_co = x_values[len(x_values)-1]
y_co = y_values[len(y_values)-1]
print_current_location(x_co,y_co)

print("The distance from initial point is: ",calc_dist(start_location,(x_co,y_co)))