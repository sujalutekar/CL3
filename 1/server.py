from xmlrpc.server import SimpleXMLRPCServer
import threading

def calculate_factorial(n):
    if n < 0:
        return "Invalid input"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return str(result)

# def shutdown_server():
#     print("Shutting down server...")
#     threading.Thread(target=server.shutdown).start()
#     return "Server shutting down..."

# Create server
server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
print("Server is running on port 8000...")

# Register functions
server.register_function(calculate_factorial, "calculate_factorial")
# server.register_function(shutdown_server, "shutdown")

# Run the server
server.serve_forever()





