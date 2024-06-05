import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def draw(x_coordinates, y_coordinates):
    fig, ax = plt.subplots()
    ax.grid()

    ax.set_xlim([min(x_coordinates), max(x_coordinates)])
    ax.set_ylim([min(y_coordinates), max(y_coordinates)])

    line, = ax.plot([], [], '-', color='r')

    def update(i):
        line.set_data(x_coordinates[:i], y_coordinates[:i])
        return line

    ani = FuncAnimation(fig=fig, func=update, frames=len(x_coordinates) + 1,interval=5, repeat=False)

    plt.show()

def bressenham(xy_start, xy_end):
    x_list = [xy_start[0]]
    y_list = [xy_start[1]]

    # menghitung nilai dx
    dx = xy_end[0] - xy_start[0]

    # menghitung nilai dy
    dy = xy_end[1] - xy_start[1]

    # jika dx bernilai 0
    if dx == 0:
        x_list = [xy_start[0]] * (abs(dy) + 1)
        y_list = list(range(xy_start[1], xy_end[1] + 1, 1 if dy > 0 else -1))

        return x_list, y_list

    # menghitung nilai 2|dx|
    two_dx = 2 * abs(dx)

    # menghitung nilai 2|dy|
    two_dy = 2 * abs(dy)

    # menghitung nilai 2|dy| - 2|dx|
    two_dy_two_dx = two_dy - two_dx

    # menghitung nilai P
    P = two_dy - abs(dx)

    step_x = 1 if dx > 0 else -1
    step_y = 1 if dy > 0 else -1

    while x_list[-1] != xy_end[0] or y_list[-1] != xy_end[1]:
        P_temp = P
        if P < 0:
            x = x_list[-1] + step_x
            y = y_list[-1]

            P = P_temp + two_dy
        else:
            x = x_list[-1] + step_x
            y = y_list[-1] + step_y

            P = P_temp + two_dy_two_dx

        x_list.append(x)
        y_list.append(y)
    
    return x_list, y_list

xy_start = [100, 100]
xy_end = [0, 0]


x_coordinates, y_coordinates = bressenham(xy_start, xy_end)

# print(x_list)
draw(x_coordinates, y_coordinates)

