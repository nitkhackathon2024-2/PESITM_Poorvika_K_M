# PESITM_Poorvika_K_M
College Name = PES Institute of Technology and Management
Here's a more detailed and informative version of the `README.md` file, updated with your project structure and some additional context for better clarity.

---

# Design Pattern Detector

This project is a **Design Pattern Detector** developed for identifying common design patterns in JavaScript,,Python,Java code. The project includes a Flask-based web interface that allows users to input JavaScript code and detect design patterns such as Singleton, Factory, Observer, Decorator, Strategy, Command, and Adapter.

## Features

- Detects popular design patterns: 
  - Singleton
  - Factory
  - Observer
  - Decorator
  - Strategy
  - Command
  - Adapter
- Supports code analysis for JavaScript,Python,Java
- Web-based interface for code input and result display
- Easy-to-use and extensible architecture for adding more patterns and languages

---

## Prerequisites

Before running this project, ensure you have the following installed on your system:

- [Python 3.8+](https://www.python.org/downloads/) - for running the backend.
- [Git](https://git-scm.com/downloads) - to clone the repository.
- [Pip (Python package installer)](https://pip.pypa.io/en/stable/installation/) - to install Python dependencies.

### Python Libraries

The project uses several Python packages that need to be installed. The primary libraries are:

- **Flask** - to handle the web framework.
- **re** - to perform regex-based pattern detection.
- **requests** (optional) - in case of any HTTP requests integration.

You can install these dependencies by following the instructions in the setup section below.

---

## Setup Instructions

### 1. Clone the Repository

Start by cloning the repository from GitHub. Open your terminal or command prompt and run:

```bash
git clone https://github.com/yourusername/design-pattern-detector.git
```

After cloning, navigate into the project directory:

```bash
cd design-pattern-detector
```

### 2. Install Required Dependencies

The required Python packages can be installed


If the `requirements.txt` file is not available, you can manually install the necessary dependencies:

```bash
pip install flask
```

### 3. Running the Flask Application

To launch the application, execute the following command in the project directory:

```bash
python app.py
```

The Flask development server should start, and you should see output similar to this:

```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) in your web browser to access the web interface.

### 4. Using the Web Application

- **Input Area**: Paste the JavaScript code you want to analyze in the provided text box.
- **Language Selection**: Select `JavaScript` from the dropdown list.
- **Detection**: Click the "Detect Patterns" button to run the pattern detection algorithms.
- **Result Display**: The detected design patterns will be displayed on the same page.

---

## Project Structure

The project is organized as follows:

```text
design-pattern-detector/
│
├── app.py                              # Main Flask application
├── javascript_pattern_detector/         # Directory for JavaScript pattern detectors
│   ├── __init__.py                      # Init file for module imports
│   ├── singleton_detector.py            # Singleton pattern detection logic
│   ├── factory_detector.py              # Factory pattern detection logic
│   ├── observer_detector.py             # Observer pattern detection logic
│   ├── decorator_detector.py            # Decorator pattern detection logic
│   ├── strategy_detector.py             # Strategy pattern detection logic
│   ├── command_detector.py              # Command pattern detection logic
│   └── adapter_detector.py              # Adapter pattern detection logic
│
├── static/                             # Static files (CSS, JavaScript)
│   ├── style.css                       # Custom CSS styles
│
├── templates/                          # HTML templates for the Flask app
│   └── index.html                      # Main page for code input and result display
│
├── README.md                           # Project documentation (this file)                  
└── .gitignore                          # Files and directories to be ignored by Git
```

### Key Files and Directories:

- `app.py`: This is the core Python file that sets up and runs the Flask web server.
- `javascript_pattern_detector/`: This folder contains the individual modules for detecting various JavaScript design patterns using regex-based logic.
- `static/`: Contains static assets like CSS files for styling the web interface.
- `templates/`: Holds the HTML files that define the structure of the web pages. The main interface is defined in `index.html`.

---

## Running Tests

You can test the functionality of the pattern detectors by using sample JavaScript code snippets for each pattern. Input the code snippets into the web interface and check whether the corresponding design patterns are correctly detected.

Example test for the **Observer Pattern**:

```java
import java.util.ArrayList;
import java.util.List;

interface Observer {
    void update(String message);
}

class ConcreteObserver implements Observer {
    private String name;

    public ConcreteObserver(String name) {
        this.name = name;
    }

    @Override
    public void update(String message) {
        System.out.println(name + " received: " + message);
    }
}

class Subject {
    private List<Observer> observers = new ArrayList<>();

    public void addObserver(Observer observer) {
        observers.add(observer);
    }

    public void notifyObservers(String message) {
        for (Observer observer : observers) {
            observer.update(message);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Subject subject = new Subject();
        Observer observer1 = new ConcreteObserver("Observer 1");
        Observer observer2 = new ConcreteObserver("Observer 2");
        
        subject.addObserver(observer1);
        subject.addObserver(observer2);
        
        subject.notifyObservers("Hello Observers!");  // Output: Observer 1 received: Hello Observers!
                                                       //         Observer 2 received: Hello Observers!
    }
}


```

Expected result: Observer Pattern detected.

---

Example test for the **Singleton Pattern**:

```javascript
const Singleton = (function () {
    let instance;

    function createInstance() {
        return new Object("I am the instance");
    }

    return {
        getInstance: function () {
            if (!instance) {
                instance = createInstance();
            }
            return instance;
        },
    };
})();

// Usage
const instance1 = Singleton.getInstance();
const instance2 = Singleton.getInstance();
console.log(instance1 === instance2); // true

```

Expected result: Singleton Pattern detected.

---

## Extending the Project

You can extend the project to support additional languages or patterns by:

1. Adding new pattern detection logic inside the `javascript_pattern_detector` directory.
2. Modifying the Flask app to handle more languages and patterns.
3. Updating the web interface to allow users to select the new options.

---

## Troubleshooting

### Common Issues

- **Flask app not starting**: Make sure Python 3.8+ is installed and all required libraries are correctly installed.
- **Pattern not detected**: Ensure that the code you are testing conforms to typical structures of the patterns and that your regex is correct.

---

## Contributing

Contributions to this project are welcome! You can open issues or submit pull requests for any bugs or feature improvements. Please follow the standard GitHub workflow for contributing.

---

This should cover the complete setup, usage, project structure, and additional information users may need to work with or contribute to the project. You can modify the content further to suit any specific needs.
