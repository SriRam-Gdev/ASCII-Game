import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_grid(grid, player_pos):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if (x, y) == player_pos:
                print("P", end=" ")
            else:
                print(grid[y][x], end=" ")
        print()
    print()

def move_player(player_pos, direction, grid):
    x, y = player_pos
    if direction == 'w' and y > 0 and grid[y - 1][x] != '#':
        y -= 1
    elif direction == 's' and y < len(grid) - 1 and grid[y + 1][x] != '#':
        y += 1
    elif direction == 'a' and x > 0 and grid[y][x - 1] != '#':
        x -= 1
    elif direction == 'd' and x < len(grid[0]) - 1 and grid[y][x + 1] != '#':
        x += 1
    return (x, y)

def main():
    grid = [
        ["#", "#", "#", "#", "#", "#", "#"],
        ["#", " ", " ", " ", " ", " ", "#"],
        ["#", " ", "#", "#", "#", " ", "#"],
        ["#", " ", " ", " ", "#", " ", "#"],
        ["#", "#", "#", " ", "#", " ", "#"],
        ["#", " ", " ", " ", " ", "T", "#"],
        ["#", "#", "#", "#", "#", "#", "#"]
    ]

    player_pos = (1, 1)
    treasure_pos = (5, 5)

    while player_pos != treasure_pos:
        clear_screen()
        print_grid(grid, player_pos)
        move = input("Move (w/a/s/d): ").strip().lower()
        player_pos = move_player(player_pos, move, grid)

    clear_screen()
    print_grid(grid, player_pos)
    print("Congratulations! You've found the treasure!")

if __name__ == "__main__":
    main()
