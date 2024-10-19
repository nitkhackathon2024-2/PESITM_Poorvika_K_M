from flask import Flask, render_template, request
# Python detectors
from pattern_detector.singleton_detector import detect_singleton
from pattern_detector.factory_detector import detect_factory
from pattern_detector.observer_detector import detect_observer
from pattern_detector.decorator_detector import detect_decorator
from pattern_detector.strategy_detector import detect_strategy
from pattern_detector.command_detector import detect_command
from pattern_detector.adapter_detector import detect_adapter
# Java detectors
from java_pattern_detector.singleton_detector import detect_java_singleton
from java_pattern_detector.factory_detector import detect_java_factory
from java_pattern_detector.observer_detector import detect_java_observer
from java_pattern_detector.decorator_detector import detect_java_decorator
from java_pattern_detector.strategy_detector import detect_java_strategy
from java_pattern_detector.command_detector import detect_java_command
from java_pattern_detector.adapter_detector import detect_java_adapter
# JavaScript detectors
from javascript_pattern_detector.singleton_detector import detect_singleton
from javascript_pattern_detector.factory_detector import detect_factory
from javascript_pattern_detector.observer_detector import detect_observer
from javascript_pattern_detector.decorator_detector import detect_decorator
from javascript_pattern_detector.strategy_detector import detect_strategy
from javascript_pattern_detector.command_detector import detect_command
from javascript_pattern_detector.adapter_detector import detect_adapter

from pattern_detector.pattern_explanations import get_pattern_explanation

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    code = ""
    detected_patterns = []
    language = "python"  # Default to Python unless specified otherwise

    if request.method == 'POST':
        code = request.form['code']
        language = request.form.get('language', 'python')  # Get the selected language
        print("Received code:")
        print(code)
        print(f"Language selected: {language}")

        detectors = []
        # Python detectors
        if language == 'python':
            detectors = [
                ('Singleton', detect_singleton),
                ('Factory', detect_factory),
                ('Observer', detect_observer),
                ('Decorator', detect_decorator),
                ('Strategy', detect_strategy),
                ('Command', detect_command),
                ('Adapter', detect_adapter)
            ]
        # Java detectors
        elif language == 'java':
            detectors = [
                ('Singleton', detect_java_singleton),
                ('Factory', detect_java_factory),
                ('Observer', detect_java_observer),
                ('Decorator', detect_java_decorator),
                ('Strategy', detect_java_strategy),
                ('Command', detect_java_command),
                ('Adapter', detect_java_adapter)
            ]
        # JavaScript detectors
        elif language == 'javascript':
            detectors = [
                ('Singleton', detect_singleton),
                ('Factory', detect_factory),
                ('Observer', detect_observer),
                ('Decorator', detect_decorator),
                ('Strategy', detect_strategy),
                ('Command', detect_command),
                ('Adapter', detect_adapter)
            ]

        # Run the appropriate detectors based on the selected language
        for pattern, detector in detectors:
            print(f"Running {pattern} detector for {language}...")
            if detector(code):
                detected_patterns.append((pattern, get_pattern_explanation(pattern)))
                print(f"{pattern} pattern detected!")
            else:
                print(f"{pattern} pattern not detected.")

    return render_template('index.html', code=code, detected_patterns=detected_patterns, language=language)

if __name__ == '__main__':
    app.run(debug=True)
