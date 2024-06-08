import random, os

def show(grid):
  for r in grid:
    for c in r:
      print(f"{c}", end = "  ")
    print("\n")

def newGrid(r, c, tile):
  grid = [[tile for y in range(c)] for x in range(r)]
  return grid

def placeMines(grid, percentMines):
  n = 0
  while (n < len(grid) * len(grid[0]) * percentMines / 100):
    x = random.randint(0, len(grid) - 1)
    y = random.randint(0, len(grid[0]) - 1)
    if grid[x][y] != "M":
      grid[x][y] = "M"
      n += 1

def plotNums(grid):
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] != "M":
        n = 0
        if c > 0 and grid[r][c - 1] == "M":
          n += 1
        if c < len(grid[0]) - 1 and grid[r][c + 1] == "M":
          n += 1
        if r > 0 and grid[r - 1][c] == "M":
          n += 1
        if r < len(grid) - 1 and grid[r + 1][c] == "M": 
          n += 1
        if r > 0 and c > 0 and grid[r - 1][c - 1] == "M":
          n += 1
        if r > 0 and c < len(grid[0]) - 1 and grid[r - 1][c + 1] == "M": 
          n += 1
        if r < len(grid) - 1 and c > 0 and grid[r + 1][c - 1] == "M":
          n += 1
        if r < len(grid) - 1 and c < len(grid[0]) - 1 and grid[r + 1][c + 1] == "M":
          n += 1
        grid[r][c] = n

def plotStart(grid, rawGrid):
  list = []
  for r in range(len(rawGrid)):
    for c in range(len(rawGrid[0])):
      if rawGrid[r][c] == 0:
        list.append([r, c])
  start = random.choice(list)
  grid[start[0]][start[1]] = "x"
  
def uncoverDFS(grid, rawGrid, innerGrid, x, y):
  grid[x][y] = "#"
  innerGrid[x][y] = "#"
  if x > 0 and grid[x - 1][y] != "#":
    if rawGrid[x - 1][y] == 0:
      uncoverDFS(grid, rawGrid, innerGrid, x - 1, y)
    else:
      grid[x - 1][y] = rawGrid[x - 1][y]
      innerGrid[x - 1][y] = str(rawGrid[x - 1][y])
  if x < len(rawGrid) - 1 and grid[x + 1][y] != "#":
    if rawGrid[x + 1][y] == 0:
      uncoverDFS(grid, rawGrid, innerGrid, x + 1, y)
    else:
      grid[x + 1][y] = rawGrid[x + 1][y]
      innerGrid[x + 1][y] = str(rawGrid[x + 1][y])
  if y > 0 and grid[x][y - 1] != "#":
    if rawGrid[x][y - 1] == 0:
      uncoverDFS(grid, rawGrid, innerGrid, x, y - 1)
    else:
      grid[x][y - 1] = rawGrid[x][y - 1]
      innerGrid[x][y - 1] = str(rawGrid[x][y - 1])
  if y < len(grid[0]) - 1 and grid[x][y + 1] != "#":
    if rawGrid[x][y + 1] == 0:
      uncoverDFS(grid, rawGrid, innerGrid, x, y + 1)
    else:
      grid[x][y + 1] = rawGrid[x][y + 1]
      innerGrid[x][y + 1] = str(rawGrid[x][y + 1])
  if x > 0 and y > 0 and grid[x - 1][y - 1] != "#":
    if rawGrid[x - 1][y - 1] == 0:
      uncoverDFS(grid, rawGrid, innerGrid, x - 1, y - 1)
    else:
      grid[x - 1][y - 1] = rawGrid[x - 1][y - 1]
      innerGrid[x - 1][y - 1] = str(rawGrid[x - 1][y - 1])
  if x > 0 and y < len(grid[0]) - 1 and grid[x - 1][y + 1] != "#":
    if rawGrid[x - 1][y + 1] == 0:
      uncoverDFS(grid, rawGrid, innerGrid, x - 1, y + 1)
    else:
      grid[x - 1][y + 1] = rawGrid[x - 1][y + 1]
      innerGrid[x - 1][y + 1] = str(rawGrid[x - 1][y + 1])
  if x < len(grid) - 1 and y > 0 and grid[x + 1][y - 1] != "#":
    if rawGrid[x + 1][y - 1] == 0:
      uncoverDFS(grid, rawGrid, innerGrid, x + 1, y - 1)
    else:
      grid[x + 1][y - 1] = rawGrid[x + 1][y - 1]
      innerGrid[x + 1][y - 1] = str(rawGrid[x + 1][y - 1])
  if x < len(grid) - 1 and y < len(grid[0]) - 1 and grid[x + 1][y + 1] != "#":
    if rawGrid[x + 1][y + 1] == 0:
      uncoverDFS(grid, rawGrid, innerGrid, x + 1, y + 1)
    else:
      grid[x + 1][y + 1] = rawGrid[x + 1][y + 1]
      innerGrid[x + 1][y + 1] = str(rawGrid[x + 1][y + 1])
  else:
    return True
 
def play():
  while True:
    r = int(input("Rows: "))
    c = int(input("Columns: "))
    percentMines = int(input("Percent mines: "))
    rawGrid = newGrid(r, c, 0)
    placeMines(rawGrid, percentMines)
    plotNums(rawGrid)
    x = int(r / 2)
    y = int(c / 2)
    grid = newGrid(r, c, " ")
    innerGrid = newGrid(r, c, " ")
    grid[x][y] = "+"
    plotStart(grid, rawGrid)
    while True:
      os.system("clear")
      show(grid)
      inp = input("Move: ")
      if inp == " ":
        if rawGrid[x][y] == "M":
          print("You triggered a recursive chain reaction and destroyed the world.")
          break
        elif int(rawGrid[x][y]) > 0:
          innerGrid[x][y] = str(rawGrid[x][y])
        else:
          uncoverDFS(grid, rawGrid, innerGrid, x, y)
      elif inp == "f":
        if innerGrid[x][y] == " ":
          innerGrid[x][y] = "F"
        elif innerGrid[x][y] == "F":
          innerGrid[x][y] = " "
      else:
        grid[x][y] = innerGrid[x][y]
        if x > 0 and inp == "w":
          x -= 1
        elif x < len(grid) - 1 and inp == "s":
          x += 1
        elif y > 0 and inp == "a":
          y -= 1
        elif y < len(grid) - 1 and inp == "d":
          y += 1
      grid[x][y] = "+"
      open = 0
      for r in range(len(grid)):
        for c in range(len(grid[0])):
          if innerGrid[r][c] == " ":
            open += 1
      if open == 0:
        print("You win, woohoo!")
        break

play()
