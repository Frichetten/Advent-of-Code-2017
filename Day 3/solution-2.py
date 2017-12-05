def calc_sum(board, x, y):
  val = 0
  try:
    val += board[((x-1),y)]
  except:
    None
  try:
    val += board[((x+1),y)]
  except:
    None
  try:
    val += board[(x,(y+1))]  
  except:
    None
  try:
    val += board[(x,(y-1))]
  except:
    None
  try:
    val += board[((x-1),(y+1))]
  except:
    None
  try:
    val += board[((x+1),(y-1))]
  except:
    None
  try:
    val += board[((x+1),(y+1))]
  except:
    None
  try:
    val += board[((x-1),(y-1))]
  except:
    None
  return val

x = 0
y = 0
i = 1
dist = 2
target = 368078
board = {(0,0):1}
while 1 == 1:
    for j in range(dist-1):
        i += 1
        x += 1
        val = calc_sum(board, x, y)
        board[(x,y)] = val
        print i, x, y, " => ", val
        if val >= target:
            exit()
    for j in range(dist-1):
        i += 1
        y -= 1
        val = calc_sum(board, x, y)
        board[(x,y)] = val
        print i, x, y, " => ", val
        if val >= target:
            exit()
    for j in range(dist):
        i += 1
        x -= 1
        val = calc_sum(board, x, y)
        board[(x,y)] = val
        print i, x, y, " => ", val
        if val >= target:
            exit()
    for j in range(dist):
        i += 1
        y += 1
        val = calc_sum(board, x, y)
        board[(x,y)] = val
        print i, x, y, " => ", val
        if val >= target:
            exit()

    dist += 2
