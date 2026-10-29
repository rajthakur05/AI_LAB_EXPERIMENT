from collections import deque


def water_jug(capacity1,capacity2,target):
  visited=set()
  queue=deque()

  queue.append((0,0,[]))

  while queue:
    jug1,jug2,path=queue.popleft()
    if (jug1,jug2) in visited:
      continue
    visited.add((jug1,jug2))

    path=path+[(jug1,jug2)]

    if jug1==target or jug2==target:
      return path

    next_states=[
        (capacity1,jug2),
        (jug1,capacity2),
        (0,jug2),
        (jug1,0),
        (jug1-min(jug1,capacity2-jug2),
         jug2+min(jug1,capacity2-jug2)),
        (jug1+min(jug2,capacity1-jug1),
         jug2-min(jug2,capacity1-jug1))
    ]

    for state in next_states:
      if state not in visited:
        queue.append((state[0],state[1],path))
  return None

jug1=int(input("enter capacity of jug1:"))
jug2=int(input("enter capacity of jug2:"))
target=int(input("enter target capacity:"))

solution=water_jug(jug1,jug2,target)

if solution:
  print("solution found:")
  for step in solution:
    print(step)
else:
  print("no solution found")



#output
'''enter capacity of jug1:4
enter capacity of jug2:3
enter target capacity:2
solution found:
(0, 0)
(0, 3)
(3, 0)
(3, 3)
(4, 2)'''