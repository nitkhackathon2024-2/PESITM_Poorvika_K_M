import ast

def detect_observer(code):
    print("Observer detector called")
    tree = ast.parse(code)
    
    subject_class = None
    observer_interface = None
    concrete_observers = set()
    
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            # Detect Subject (look for register, unregister, and notify methods)
            if any(isinstance(item, ast.FunctionDef) and item.name in ['register', 'unregister', 'notify'] for item in node.body):
                subject_class = node.name
                print(f"Found Subject class: {subject_class}")
            
            # Detect Observer interface (look for an 'update' method)
            if any(isinstance(item, ast.FunctionDef) and item.name == 'update' for item in node.body):
                if not node.bases:  # No base class means it’s the Observer interface
                    observer_interface = node.name
                    print(f"Found Observer interface: {observer_interface}")
                elif observer_interface and isinstance(node.bases[0], ast.Name) and node.bases[0].id == observer_interface:
                    concrete_observers.add(node.name)
                    print(f"Found Concrete Observer: {node.name}")
    
    if subject_class and observer_interface and concrete_observers:
        print("Observer pattern detected!")
        return True
    
    print("Observer pattern not detected.")
    return False
