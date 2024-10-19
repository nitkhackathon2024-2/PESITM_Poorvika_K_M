def detect_java_strategy(code):
    """
    Detects if the Java code contains the Strategy pattern.
    Looks for Strategy interface and concrete strategy implementations.
    """
    if "Strategy" in code and "implements" in code:
        return True
    return False
