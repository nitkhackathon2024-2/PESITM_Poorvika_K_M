import re

def detect_factory(code):
    # Regex pattern to identify Factory structure in JavaScript
    factory_pattern = r'function\s+\w+\s*\(\s*\w+\s*,\s*\w+\s*\)\s*{[^}]*return\s+new\s+\w+\s*\(\w+\s*,\s*\w+\s*\);'
    factory_class_pattern = r'function\s+\w+Factory\s*\(\)\s*{[^}]*this\.create\s*=\s*function\s*\(\w+,\s*\w+\)\s*{[^}]*return\s+new\s+\w+\s*\(\w+,\s*\w+\s*\);'

    if re.search(factory_pattern, code) or re.search(factory_class_pattern, code):
        return True  # Factory detected
    return False  # Factory not detected
