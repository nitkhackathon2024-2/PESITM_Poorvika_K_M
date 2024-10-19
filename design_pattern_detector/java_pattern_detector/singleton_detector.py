import javalang

def detect_java_singleton(code):
    """
    Detects if a Java class follows the Singleton design pattern.
    """
    try:
        # Parse the Java code using javalang parser
        tree = javalang.parse.parse(code)

        class_declarations = [node for path, node in tree if isinstance(node, javalang.tree.ClassDeclaration)]
        for class_decl in class_declarations:
            # Check if the class has a private constructor and a static instance field
            has_private_constructor = False
            has_static_instance = False
            
            for member in class_decl.body:
                if isinstance(member, javalang.tree.ConstructorDeclaration):
                    if 'private' in member.modifiers:
                        has_private_constructor = True
                
                if isinstance(member, javalang.tree.FieldDeclaration):
                    for declarator in member.declarators:
                        if 'static' in member.modifiers and 'final' in member.modifiers:
                            has_static_instance = True

            # If both conditions are met, it is a Singleton pattern
            if has_private_constructor and has_static_instance:
                return True
        return False
    except javalang.parser.JavaSyntaxError:
        return False
