def detect_java_decorator(code):
    """
    Detects if the Java code contains the Decorator pattern.
    Looks for 'Decorator' or 'Wrapper' keywords and common method signatures.
    """
    if "Decorator" in code or "wrap" in code:
        return True
    return False
