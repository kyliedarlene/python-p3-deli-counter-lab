def line(current_line):
    if current_line == []:
        print("The line is currently empty.")
    else:
        message = ["The line is currently:"]
        for index, member in enumerate(current_line):
            message.append(f"{index + 1}. {member}")
        print(" ".join(message))
    
def take_a_number(current_line, customer):
    current_line.append(customer)
    print(f"Welcome, {customer}. You are number {len(current_line)} in line.")

def now_serving(current_line):
    if current_line == []:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {current_line[0]}.")
        current_line.pop(0)