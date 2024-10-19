import ast

def detect_command(code):
    print("Command detector called")
    tree = ast.parse(code)
    
    command_interface = None
    concrete_commands = set()
    invoker_class = None
    receiver_class = None
    
    # Traverse the AST to find class definitions
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            # Detect Command interface (look for an 'execute' method)
            if any(isinstance(item, ast.FunctionDef) and item.name == 'execute' for item in node.body):
                if not node.bases:  # No base class means it’s the Command interface
                    command_interface = node.name
                    print(f"Found Command interface: {command_interface}")
                elif command_interface and isinstance(node.bases[0], ast.Name) and node.bases[0].id == command_interface:
                    concrete_commands.add(node.name)
                    print(f"Found Concrete Command: {node.name}")
            
            # Detect Invoker (which calls 'execute' on Command objects)
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and any(isinstance(stmt, ast.Call) and isinstance(stmt.func, ast.Attribute) and stmt.func.attr == 'execute' for stmt in ast.walk(item)):
                    invoker_class = node.name
                    print(f"Found Invoker class: {invoker_class}")
                    
            # Detect Receiver class (specific functionality encapsulated by command)
            if any(isinstance(item, ast.FunctionDef) for item in node.body):
                receiver_class = node.name
                print(f"Found Receiver class: {receiver_class}")
    
    if command_interface and concrete_commands and invoker_class and receiver_class:
        print("Command pattern detected!")
        return True
    
    print("Command pattern not detected.")
    return False
