RANGE = 5

board = [[0 for x in range(RANGE)] for x in range(RANGE)]

board[1][1] = 1

class Underpopulated:
  def shouldRun(self, total_live_friends):
    print "Underpopulated: %s" % total_live_friends
    return total_live_friends < 2

  def result(self):
    return 0


class JustRight:
  def shouldRun(self, total_live_friends):
    print "JustRight: %s" % total_live_friends
    return total_live_friends in [2, 3]

  def result(self):
    return 1


class Overpopulated:
  def shouldRun(self, total_live_friends):
    print "Overpopulated: %s" % total_live_friends
    return total_live_friends > 3

  def result(self):
    return 0


def GetValue(board, x, y, x_offset, y_offset):
  try:
    return board[x + x_offset][y + y_offset]
  except:
    return 0

handlers = [Underpopulated(), JustRight(), Overpopulated()]


# while True:
  # for each cell
  # check neighbour
    # if < 2 then 0
    # if 2/3 then 1
    # if > 3 then 0

# for x in range(RANGE):
for i in range(RANGE):
  for j in range(RANGE):

    live_friends = [
      GetValue(board, i, j, -1, -1),
      GetValue(board, i, j, 0, -1),
      GetValue(board, i, j, 1, -1),
      GetValue(board, i, j, 1, 0),
      GetValue(board, i, j, 1, 1),
      GetValue(board, i, j, 0, 1),
      GetValue(board, i, j, -1, 1),
      GetValue(board, i, j, -1, 0)
    ]

    total_live_friends = sum(live_friends)

    filtered = filter(lambda handler: handler.shouldRun(total_live_friends) == True, handlers)

print board