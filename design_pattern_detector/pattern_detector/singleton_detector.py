# singleton_detector.py
import ast

def detect_singleton(code):
    tree = ast.parse(code)
    
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            has_private_constructor = False
            has_instance_variable = False
            has_get_instance_method = False
            
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    if item.name == '__init__' and item.args.args[0].arg == 'self':
                        has_private_constructor = True
                    elif item.name.lower().startswith('get_instance'):
                        has_get_instance_method = True
                elif isinstance(item, ast.Assign):
                    if isinstance(item.targets[0], ast.Name) and item.targets[0].id.startswith('_instance'):
                        has_instance_variable = True
            
            if has_private_constructor and has_instance_variable and has_get_instance_method:
                return True
    
    return False