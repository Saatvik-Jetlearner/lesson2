ticket_queue = []

name = [ticket_queue(0)]
ticket_queue.append("Alice")
ticket_queue.append("Bob")
ticket_queue.append("Charlie")

print(ticket_queue)

ticket_queue.append("David")

while len(ticket_queue) > 0:
    current_doc = ticket_queue.pop(0)
    print([name] + "bought a ticket.")
