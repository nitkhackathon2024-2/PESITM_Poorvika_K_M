import ast

def detect_adapter(code):
    print("Adapter detector called")
    tree = ast.parse(code)
    
    target_interface = None
    adaptee_class = None
    adapter_class = None
    
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            # Look for Target interface (methods expected by the client)
            if any(isinstance(item, ast.FunctionDef) for item in node.body):
                if not node.bases:
                    target_interface = node.name
                    print(f"Found Target interface: {target_interface}")
                
            # Look for Adaptee class (the incompatible interface)
            if any(isinstance(item, ast.FunctionDef) for item in node.body):
                adaptee_class = node.name
                print(f"Found Adaptee class: {adaptee_class}")
            
            # Look for Adapter class (implements target interface, calls adaptee methods)
            if target_interface and adaptee_class and any(isinstance(item, ast.FunctionDef) for item in node.body):
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        if any(isinstance(stmt, ast.Call) and isinstance(stmt.func, ast.Attribute) for stmt in ast.walk(item)):
                            adapter_class = node.name
                            print(f"Found Adapter class: {adapter_class}")
    
    if target_interface and adaptee_class and adapter_class:
        print("Adapter pattern detected!")
        return True
    
    print("Adapter pattern not detected.")
    return False
