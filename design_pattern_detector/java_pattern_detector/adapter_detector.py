def detect_java_adapter(code):
    """
    Detects if the Java code contains the Adapter pattern.
    Looks for Adapter class and method calls to adapt an interface.
    """
    if "Adapter" in code and "adapt" in code:
        return True
    return False
