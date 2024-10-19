# javascript_pattern_detector/observer_detector.py

import re

def detect_observer(code):
    # Regex patterns to identify Observer structure in JavaScript
    observer_pattern = r'\w+\s*=\s*class\s+\w+\s*{[^}]*\s*notify\s*\(.*\)\s*{[^}]*for\s*\(const\s+\w+\s+of\s+\w+\s*\)\s*\{[^}]*\}'
    
    if re.search(observer_pattern, code):
        return True  # Observer detected
    return False  # Observer not detected
