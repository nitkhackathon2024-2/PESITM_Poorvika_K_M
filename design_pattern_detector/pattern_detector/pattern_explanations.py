# pattern_explanations.py

pattern_explanations = {
    'Singleton': "The Singleton pattern ensures a class has only one instance and provides a global point of access to it. It's useful when exactly one object is needed to coordinate actions across the system.",
    'Factory': "The Factory pattern provides an interface for creating objects in a superclass, allowing subclasses to decide which class to instantiate. It's useful when a class can't anticipate the type of objects it needs to create.",
    'Observer': "The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. It's useful for implementing distributed event handling systems.",
    'Decorator': "The Decorator pattern allows behavior to be added to individual objects, either statically or dynamically, without affecting the behavior of other objects from the same class. It's useful for extending functionality without subclassing.",
    'Strategy': "The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. It lets the algorithm vary independently from clients that use it. It's useful when you have multiple algorithms for a specific task and want to switch between them dynamically.",
    'Command': "The Command pattern encapsulates a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations. It's useful for implementing undo/redo functionality or delayed execution of operations.",
    'Adapter': "The Adapter pattern allows objects with incompatible interfaces to collaborate. It acts as a wrapper between two objects, converting the interface of one object so that it can be used by the other. It's useful when you want to use an existing class, but its interface isn't compatible with the rest of your code."
}

def get_pattern_explanation(pattern):
    return pattern_explanations.get(pattern, "No explanation available for this pattern.")