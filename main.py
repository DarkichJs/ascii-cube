import os
import math
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_rotated_cube(angle_x, angle_y, angle_z, cube_size):

    vertices = [
        [-cube_size, -cube_size, -cube_size],
        [cube_size, -cube_size, -cube_size],
        [cube_size, cube_size, -cube_size],
        [-cube_size, cube_size, -cube_size],
        [-cube_size, -cube_size, cube_size],
        [cube_size, -cube_size, cube_size],
        [cube_size, cube_size, cube_size],
        [-cube_size, cube_size, cube_size]
    ]

    rotate_x = [[1, 0, 0],
                [0, math.cos(angle_x), -math.sin(angle_x)],
                [0, math.sin(angle_x), math.cos(angle_x)]]

    rotate_y = [[math.cos(angle_y), 0, math.sin(angle_y)],
                [0, 1, 0],
                [-math.sin(angle_y), 0, math.cos(angle_y)]]

    rotate_z = [[math.cos(angle_z), -math.sin(angle_z), 0],
                [math.sin(angle_z), math.cos(angle_z), 0],
                [0, 0, 1]]

    rotated_vertices = []
    for vertex in vertices:
        rotated_vertex = vertex
        rotated_vertex = [sum(rotate_x[j][i] * rotated_vertex[i] for i in range(3)) for j in range(3)]
        rotated_vertex = [sum(rotate_y[j][i] * rotated_vertex[i] for i in range(3)) for j in range(3)]
        rotated_vertex = [sum(rotate_z[j][i] * rotated_vertex[i] for i in range(3)) for j in range(3)]
        rotated_vertices.append(rotated_vertex)

    return rotated_vertices

def draw_cube(rotated_vertices, screen_width, screen_height):
    edges = [
        [0, 1], [1, 2], [2, 3], [3, 0],
        [4, 5], [5, 6], [6, 7], [7, 4],
        [0, 4], [1, 5], [2, 6], [3, 7]
    ]

    projected_vertices = []
    for vertex in rotated_vertices:
        x, y = vertex[0], vertex[1]
        projected_vertices.append([screen_width // 2 + int(x), screen_height // 2 - int(y)])
    screen = [[' ' for _ in range(screen_width)] for _ in range(screen_height)]
    for edge in edges:
        x0, y0 = projected_vertices[edge[0]]
        x1, y1 = projected_vertices[edge[1]]
        dx, dy = x1 - x0, y1 - y0
        distance = max(abs(dx), abs(dy))
        for i in range(distance):
            x, y = x0 + dx * i // distance, y0 + dy * i // distance
            if 0 <= x < screen_width and 0 <= y < screen_height:
                screen[y][x] = '$'  

    for row in screen:
        print(''.join(row))

def main():
    cube_size = 10
    screen_width, screen_height = 80, 40
    angle_x, angle_y, angle_z = 0, 0, 0
    while True:
        clear_screen()
        rotated_vertices = get_rotated_cube(angle_x, angle_y, angle_z, cube_size)
        draw_cube(rotated_vertices, screen_width, screen_height)
        angle_x += 0.05
        angle_y += 0.05
        angle_z += 0.05
        time.sleep(0.1)

main()  

