def detect_java_command(code):
    """
    Detects if the Java code contains the Command pattern.
    Looks for 'Command' interface and concrete command classes.
    """
    if "Command" in code and "execute" in code:
        return True
    return False
