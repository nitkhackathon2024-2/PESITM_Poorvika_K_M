import ast

def detect_strategy(code):
    print("Strategy detector called")  # Debug print
    tree = ast.parse(code)
    
    strategy_interface = None
    concrete_strategies = set()
    context_class = None
    context_uses_strategy = False
    
    # Traverse the AST to find class definitions
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            # Detect the Strategy interface by checking for the 'execute' method
            if any(isinstance(item, ast.FunctionDef) and item.name == 'execute' for item in node.body):
                if not node.bases:  # No base class = Strategy interface
                    strategy_interface = node.name
                    print(f"Found strategy interface: {strategy_interface}")
                elif strategy_interface and isinstance(node.bases[0], ast.Name) and node.bases[0].id == strategy_interface:
                    concrete_strategies.add(node.name)
                    print(f"Found concrete strategy: {node.name}")
            
            # Detect the Context class
            for item in node.body:
                # Check for an __init__ method that receives the strategy
                if isinstance(item, ast.FunctionDef) and item.name == '__init__':
                    if any(isinstance(arg, ast.arg) and arg.arg == 'strategy' for arg in item.args.args):
                        context_class = node.name
                        print(f"Found context class: {context_class}")
                
                # Check if the 'perform_operation' method calls the strategy's execute method
                if isinstance(item, ast.FunctionDef) and item.name == 'perform_operation':
                    for stmt in ast.walk(item):
                        if isinstance(stmt, ast.Call) and isinstance(stmt.func, ast.Attribute) and stmt.func.attr == 'execute':
                            context_uses_strategy = True
                            print(f"Context class {context_class} calls execute method of strategy")
                            break
    
    # If both strategy interface and concrete strategies are found and context uses strategy
    if strategy_interface and concrete_strategies and context_class and context_uses_strategy:
        print("Strategy pattern detected!")
        return True
    
    print("Strategy pattern not detected.")
    return False
