# factory_detector.py
import ast

def detect_factory(code):
    tree = ast.parse(code)
    
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            has_create_method = False
            creates_different_objects = False
            
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    if item.name.lower().startswith('create') or item.name.lower().startswith('get'):
                        has_create_method = True
                        for sub_node in ast.walk(item):
                            if isinstance(sub_node, ast.Return) and isinstance(sub_node.value, ast.Call):
                                creates_different_objects = True
                                break
                
                if has_create_method and creates_different_objects:
                    return True
    
    return False