# javascript_pattern_detector/strategy_detector.py

import re

def detect_strategy(code):
    # Regex patterns to identify Strategy structure in JavaScript
    strategy_pattern = r'function\s+\w+\s*\(.*\)\s*{\s*let\s+\w+\s*=\s*\(\)\s*=>\s*{[^}]*}\s*return\s+\w+;\s*}'
    
    if re.search(strategy_pattern, code):
        return True  # Strategy detected
    return False  # Strategy not detected
