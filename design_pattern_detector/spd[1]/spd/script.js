// Array to hold custom patterns
const customPatterns = [];

// Predefined design patterns for JavaScript, Java, and Python
const designPatterns = {
    javascript: [
        { name: 'Singleton', regex: /class\s+\w+\s*{[^}]*if\s*\(!\w+\.instance\)\s*{[^}]*\w+\.instance\s*=\s*this;/, description: 'Ensures a class has only one instance.' },
        { name: 'Factory', regex: /class\s+\w+\s*{[^}]*create\s*\(\)/, description: 'Creates objects without exposing instantiation logic.' },
        { name: 'Observer', regex: /class\s+\w+\s*{[^}]*subscribe\s*\(\)/, description: 'Defines a one-to-many dependency between objects.' },
        { name: 'Decorator', regex: /function\s+\w+\s*\(\s*\w+\s*\)\s*{[^}]*return\s+\w+\(\)/, description: 'Adds behavior to individual objects.' },
        { name: 'Strategy', regex: /class\s+\w+\s*{[^}]*execute\s*\(\)/, description: 'Defines a family of algorithms and encapsulates them.' },
        { name: 'Command', regex: /class\s+\w+\s*{[^}]*execute\s*\(\)/, description: 'Encapsulates a request as an object.' },
        { name: 'Adapter', regex: /class\s+\w+\s*{[^}]*method\s*\(\)/, description: 'Allows incompatible interfaces to work together.' },
        { name: 'Facade', regex: /class\s+\w+\s*{[^}]*method1\s*\(\)[^}]*method2\s*\(\)/, description: 'Provides a simplified interface to a complex subsystem.' },
        { name: 'Proxy', regex: /class\s+\w+\s*{[^}]*getInstance\s*\(\)/, description: 'Provides a surrogate or placeholder for another object.' },
        { name: 'State', regex: /class\s+\w+\s*{[^}]*setState\s*\(\)/, description: 'Allows an object to alter its behavior when its internal state changes.' },
        { name: 'Mediator', regex: /class\s+\w+\s*{[^}]*notify\s*\(\)/, description: 'Defines an object that encapsulates how a set of objects interact.' },
        { name: 'Iterator', regex: /class\s+\w+\s*{[^}]*next\s*\(\)/, description: 'Provides a way to access elements of a collection without exposing its underlying representation.' },
        { name: 'Builder', regex: /class\s+\w+\s*{[^}]*build\s*\(\)/, description: 'Separates the construction of a complex object from its representation.' },
        { name: 'Template Method', regex: /class\s+\w+\s*{[^}]*templateMethod\s*\(\)/, description: 'Defines the skeleton of an algorithm in a method.' },
        { name: 'Chain of Responsibility', regex: /class\s+\w+\s*{[^}]*setNext\s*\(\)/, description: 'Passes a request along the chain of handlers.' },
        { name: 'Visitor', regex: /class\s+\w+\s*{[^}]*visit\s*\(\)/, description: 'Separates an algorithm from the object structure.' }
    ],
    java: [
        { name: 'Singleton', regex: /private\s+static\s+\w+\s+instance\s*=\s*null;[^}]*public\s+static\s+\w+\s+getInstance\s*\(\)\s*{[^}]*if\s*\(instance\s*==\s*null\)\s*instance\s*=\s*new\s+\w+\(\);/, description: 'Ensures a class has only one instance.' },
        { name: 'Factory', regex: /class\s+\w+\s*{[^}]*create\s*\(\)/, description: 'Creates objects without exposing instantiation logic.' },
        { name: 'Observer', regex: /public\s+void\s+subscribe\s*\(\w+\)\s*{/, description: 'Defines a one-to-many dependency between objects.' },
        { name: 'Decorator', regex: /public\s+class\s+\w+\s+extends\s+\w+\s*{[^}]*public\s+\w+\s*\(\)/, description: 'Adds behavior to individual objects.' },
        { name: 'Strategy', regex: /interface\s+\w+\s*{[^}]*execute\s*\(\)/, description: 'Defines a family of algorithms and encapsulates them.' },
        { name: 'Command', regex: /class\s+\w+\s*{[^}]*public\s+void\s+execute\s*\(\)/, description: 'Encapsulates a request as an object.' },
        { name: 'Adapter', regex: /public\s+class\s+\w+\s*implements\s+\w+\s*{/, description: 'Allows incompatible interfaces to work together.' },
        { name: 'Facade', regex: /public\s+class\s+\w+\s*{[^}]*public\s+void\s+method1\s*\(\)[^}]*public\s+void\s+method2\s*\(\)/, description: 'Provides a simplified interface to a complex subsystem.' },
        { name: 'Proxy', regex: /public\s+class\s+\w+\s*{[^}]*private\s+\w+\s+realObject\s*;/, description: 'Provides a surrogate or placeholder for another object.' },
        { name: 'State', regex: /class\s+\w+\s*{[^}]*setState\s*\(\)/, description: 'Allows an object to alter its behavior when its internal state changes.' },
        { name: 'Mediator', regex: /class\s+\w+\s*{[^}]*notify\s*\(\)/, description: 'Defines an object that encapsulates how a set of objects interact.' },
        { name: 'Iterator', regex: /public\s+interface\s+\w+\s*{[^}]*next\s*\(\)/, description: 'Provides a way to access elements of a collection without exposing its underlying representation.' },
        { name: 'Builder', regex: /class\s+\w+\s*{[^}]*build\s*\(\)/, description: 'Separates the construction of a complex object from its representation.' },
        { name: 'Template Method', regex: /abstract\s+class\s+\w+\s*{[^}]*templateMethod\s*\(\)/, description: 'Defines the skeleton of an algorithm in a method.' },
        { name: 'Chain of Responsibility', regex: /class\s+\w+\s*{[^}]*setNext\s*\(\)/, description: 'Passes a request along the chain of handlers.' },
        { name: 'Visitor', regex: /public\s+class\s+\w+\s*{[^}]*visit\s*\(\)/, description: 'Separates an algorithm from the object structure.' }
    ],
    python: [
        { name: 'Singleton', regex: /class\s+\w+\s*:\s*[^}]*_instance\s*=\s*None\s*def\s+__new__\(\s*cls\s*\)[^}]*if\s+cls\._instance\s+is\s+None:/, description: 'Ensures a class has only one instance.' },
        { name: 'Factory', regex: /class\s+\w+\s*:\s*def\s+create\s*\(\)/, description: 'Creates objects without exposing instantiation logic.' },
        { name: 'Observer', regex: /def\s+subscribe\s*\(\w+\)\s*:/, description: 'Defines a one-to-many dependency between objects.' },
        { name: 'Decorator', regex: /def\s+wrapper\s*\(\w+\)/, description: 'Adds behavior to individual objects.' },
        { name: 'Strategy', regex: /class\s+\w+\s*:\s*def\s+execute\s*\(\)/, description: 'Defines a family of algorithms and encapsulates them.' },
        { name: 'Command', regex: /class\s+\w+\s*:\s*def\s+execute\s*\(\)/, description: 'Encapsulates a request as an object.' },
        { name: 'Adapter', regex: /class\s+\w+\s*:\s*def\s+method\s*\(\)/, description: 'Allows incompatible interfaces to work together.' },
        { name: 'Facade', regex: /class\s+\w+\s*:\s*def\s+method1\s*\(\):\s*def\s+method2\s*\(\)/, description: 'Provides a simplified interface to a complex subsystem.' },
        { name: 'Proxy', regex: /class\s+\w+\s*:\s*def\s+get_instance\s*\(\)/, description: 'Provides a surrogate or placeholder for another object.' },
        { name: 'State', regex: /class\s+\w+\s*:\s*def\s+set_state\s*\(\)/, description: 'Allows an object to alter its behavior when its internal state changes.' },
        { name: 'Mediator', regex: /class\s+\w+\s*:\s*def\s+notify\s*\(\)/, description: 'Defines an object that encapsulates how a set of objects interact.' },
        { name: 'Iterator', regex: /class\s+\w+\s*:\s*def\s+next\s*\(\)/, description: 'Provides a way to access elements of a collection without exposing its underlying representation.' },
        { name: 'Builder', regex: /class\s+\w+\s*:\s*def\s+build\s*\(\)/, description: 'Separates the construction of a complex object from its representation.' },
        { name: 'Template Method', regex: /class\s+\w+\s*:\s*def\s+template_method\s*\(\)/, description: 'Defines the skeleton of an algorithm in a method.' },
        { name: 'Chain of Responsibility', regex: /class\s+\w+\s*:\s*def\s+set_next\s*\(\)/, description: 'Passes a request along the chain of handlers.' },
        { name: 'Visitor', regex: /class\s+\w+\s*:\s*def\s+visit\s*\(\)/, description: 'Separates an algorithm from the object structure.' }
    ]
};

// Wait for DOM to load before adding event listeners
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('addPatternButton').addEventListener('click', addCustomPattern);
    document.getElementById('detectPatternButton').addEventListener('click', detectDesignPattern);
});

// Function to add a custom pattern
function addCustomPattern() {
    const name = document.getElementById('patternName').value.trim();
    const regexInput = document.getElementById('patternRegex').value.trim();
    const description = document.getElementById('patternDescription').value.trim();

    // Validate inputs
    if (!name || !regexInput || !description) {
        alert('Please enter a pattern name, regex, and description.');
        return;
    }
    if (customPatterns.find(pattern => pattern.name === name)) {
        alert('Pattern name already exists. Please choose a different name.');
        return;
    }

    // Validate regex
    let regex;
    try {
        regex = new RegExp(regexInput);
    } catch (error) {
        alert(`Invalid regex pattern: ${error.message}`);
        return;
    }

    // Add pattern to the array
    customPatterns.push({ name, regex, description });
    document.getElementById('customPatternsList').innerHTML += `<p>${name} added successfully!</p>`;
}

// Function to detect design patterns
function detectDesignPattern() {
    const code = document.getElementById('codeInput').value.trim();
    const language = document.getElementById('languageSelect').value;
    const detectedPatterns = [];

    // Check for custom patterns
    customPatterns.forEach(pattern => {
        if (pattern.regex.test(code)) {
            detectedPatterns.push({ name: pattern.name, description: pattern.description });
        }
    });

    // Check for built-in design patterns based on the selected language
    designPatterns[language].forEach(pattern => {
        if (pattern.regex.test(code)) {
            detectedPatterns.push({ name: pattern.name, description: pattern.description });
        }
    });

    // Display the detected patterns
    const detectedPatternsList = document.getElementById('detectedPatterns');
    detectedPatternsList.innerHTML = '';
    if (detectedPatterns.length > 0) {
        detectedPatternsList.innerHTML = detectedPatterns
            .map(pattern => `<p>${pattern.name}: ${pattern.description}</p>`)
            .join('');
    } else {
        detectedPatternsList.innerHTML = '<p>No patterns detected.</p>';
    }
}
