import matplotlib.pyplot as plt

xy_start = [2, 9]
xy_end = [800, 600]


def draw(x_coordinates, y_coordinates):
    plt.ylabel('sumbu y')
    plt.xlabel('sumbu x')
    plt.grid()

    plt.plot(x_coordinates, y_coordinates, '-')
    # for x, y in zip(x_coordinates, y_coordinates):
    #     plt.scatter(x, y)
    #     plt.pause(0.00001)
    #     print(x)

    plt.show()


def calculate_M_0to1(xy_start, xy_end, P, two_dy, two_dy_two_dx, step_x, step_y):
    x_list = [xy_start[0]]
    y_list = [xy_start[1]]

    K = 0

    while True:
        P_temp = P

        if(x_list[K] == xy_end[0] and y_list[K] == xy_end[1]):
            break

        if P < 0:
            x = x_list[K] + step_x
            y = y_list[K]

            x_list.append(x)
            y_list.append(y)

            P = P_temp + two_dy

            print(f'x = {x}, y = {y}, P = {P}')
        else:
            x = x_list[K] + step_x
            y = y_list[K] + step_y

            x_list.append(x)
            y_list.append(y)

            P = P_temp + two_dy_two_dx
            print(f'x = {x}, y = {y}, P = {P}')

        K += 1

    return x_list, y_list

def calculate_M_min1to0(xy_start, xy_end, P, two_dy, two_dy_two_dx, step_x, step_y):
    x_list = [xy_start[0]]
    y_list = [xy_start[1]]

    K = 0

    while True:
        P_temp = P

        if(x_list[K] == xy_end[0] and y_list[K] == xy_end[1]):
            break

        if P < 0:
            x = x_list[K] + step_x
            y = y_list[K]

            x_list.append(x)
            y_list.append(y)

            P = P_temp + two_dy

            print(f'x = {x}, y = {y}, P = {P}')
        else:
            x = x_list[K] + step_x
            y = y_list[K] - step_y

            x_list.append(x)
            y_list.append(y)

            P = P_temp + two_dy_two_dx
            print(f'x = {x}, y = {y}, P = {P}')

        K += 1

    return x_list, y_list


def calculate(xy_start, xy_end):
    dx = xy_end[0] - xy_start[0]
    dy = xy_end[1] - xy_start[1]

    if dx == 0:
        x_list = [xy_start[0]] * (abs(dy) + 1)
        y_list = list(range(xy_start[1], xy_end[1] + 1, 1 if dy > 0 else -1))
        return x_list, y_list

    M = dy / dx

    # 2 * |dx|
    two_dx = 2 * abs(dx)

    # 2 * |dy|
    two_dy = 2 * abs(dy)

    # 2 * |dy| - 2 * |dx|
    two_dy_two_dx = two_dy - two_dx
    
    # P0 Paramater
    P = two_dy - abs(dx)

    step_x = 1 if dx > 0 else -1
    step_y = 1 if dy > 0 else -1

    if M <= 1:
        result = calculate_M_0to1(xy_start, xy_end, P, two_dy, two_dy_two_dx, step_x, step_y)
    else:
        result = calculate_M_min1to0(xy_start, xy_end, P, two_dy, two_dy_two_dx, step_x, step_y)

    return result

x_coordinates, y_coordinates = calculate(xy_start, xy_end)

draw(x_coordinates, y_coordinates)
