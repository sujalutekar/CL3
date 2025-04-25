import xmlrpc.client

# Connect to server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

while True:
    user_input = input("Enter a number to calculate factorial (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        print("Client exited.")
        break
    try:
        num = int(user_input)
        result = proxy.calculate_factorial(num)
        print(f"Factorial of {num} is: {result}")
    except ValueError:
        print("Please enter a valid integer.")
