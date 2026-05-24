ticket_queue = []

ticket_queue.append("Alice")
ticket_queue.append("Bob")
ticket_queue.append("Charlie")

print(ticket_queue)

ticket_queue.append("David")

while len(ticket_queue) > 0:
    print(ticket_queue[0] + " bought a ticket")
    ticket_queue.pop(0)