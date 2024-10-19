# javascript_pattern_detector/singleton_detector.py

import re

def detect_singleton(code):
    # Regex patterns to identify Singleton structure in JavaScript
    singleton_pattern = r'const\s+\w+\s*=\s*\(function\s*\(\)\s*\{[^}]*let\s+instance\s*;'
    get_instance_pattern = r'getInstance\s*:\s*function\s*\(\)\s*\{[^}]*if\s*\(\s*!instance\s*\)'

    if re.search(singleton_pattern, code) and re.search(get_instance_pattern, code):
        return True  # Singleton detected
    return False  # Singleton not detected
