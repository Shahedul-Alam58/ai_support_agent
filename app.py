from controller import route_request

user_input = input("Welcome to SRBN store. How can I help you today?\n")

response = route_request(user_input)

print(response)