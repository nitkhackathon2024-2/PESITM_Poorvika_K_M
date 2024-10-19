# decorator_detector.py
import ast

def detect_decorator(code):
    print("Decorator detector called")  # Debug print
    tree = ast.parse(code)
    
    component_interface = None
    concrete_component = None
    base_decorator = None
    concrete_decorator = None
    
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            # Check for Component interface
            if any(isinstance(item, ast.FunctionDef) and item.name == 'operation' for item in node.body):
                if not node.bases:  # If it has no base class, it's the interface
                    component_interface = node.name
                    print(f"Found component interface: {component_interface}")  # Debug print
                elif node.bases[0].id == component_interface:
                    concrete_component = node.name
                    print(f"Found concrete component: {concrete_component}")  # Debug print
            
            # Check for Decorator class
            if component_interface and len(node.bases) > 0 and node.bases[0].id == component_interface:
                if any(isinstance(item, ast.FunctionDef) and item.name == '__init__' for item in node.body):
                    base_decorator = node.name
                    print(f"Found base decorator: {base_decorator}")  # Debug print
            
            # Check for Concrete Decorator
            if base_decorator and len(node.bases) > 0 and node.bases[0].id == base_decorator:
                concrete_decorator = node.name
                print(f"Found concrete decorator: {concrete_decorator}")  # Debug print
    
    result = all([component_interface, concrete_component, base_decorator, concrete_decorator])
    print(f"Decorator detector result: {result}")  # Debug print
    return result