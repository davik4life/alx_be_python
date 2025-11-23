# def perform_operation(num1, num2, operation):
#     match operation:
#         case "add":
#             return num1 + num2
#         case "subtract":
#             return num1 - num2
#         case "multi[ply":
#             return num1 * num2
#         case "divide":
#             if num2 != 0:
#                 return num1 / num2
#             else:
#                 return "Error: Cannot divide by zero."
#         case _:
#             return "Error: Invalid operation."
        
def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Cannot divide by zero."
    else:
        return "Error: Invalid operation."
        

# Example usage: 
# result = perform_operation(10, 5, "add")
# print(result)  # Output: 15