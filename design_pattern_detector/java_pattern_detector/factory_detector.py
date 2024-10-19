def detect_java_factory(code):
    """
    Detects if the Java code contains the Factory pattern.
    Basic detection looks for 'factory' class names or related keywords.
    """
    if "Factory" in code and "create" in code:
        return True
    return False
