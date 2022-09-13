N = 3
q = [0] * N
front = rear = -1

rear = (rear + 1) % N
q[rear] = 20
print(q)
rear = (rear + 1) % N
q[rear] = 30
print(q)
rear = (rear + 1) % N
q[rear] = 40
print(q)    # 20 30 40

front = (front + 1) % N
print(q[front]) # 20

front = (front + 1) % N
print(q[front]) # 30

front = (front + 1) % N
print(q[front]) # 40
# --------------------------------------
rear = (rear + 1) % N
q[rear] = 50    # 50 30 40
print(q)

front = (front + 1) % N
print(q[front]) # 50

