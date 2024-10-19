def detect_java_observer(code):
    """
    Detects if the Java code contains the Observer pattern.
    Looks for 'Observer' and 'Subject' related methods.
    """
    if "Observer" in code and "Subject" in code:
        return True
    return False
