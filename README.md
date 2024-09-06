# PySpring Framework Guide

## Overview

Welcome to **PySpring**, a Python framework inspired by ***Spring Boot***, designed to streamline the development of web applications with `auto Dependency Injection (DI)` and `auto configuration injection`. This guide will walk you through how to define components and properties in **PySpring**, enabling you to build robust applications with minimal configuration.

# Features

### Auto Dependency Injection (DI): 
Automatically inject dependencies between services and components.

### Auto Configuration Injection: 
Map application properties from configuration files directly into your components.

### Installation
To get started with **PySpring**, you need to install the framework:

```bash
pip3 install git+https://github.com/NFUChen/PySpring.git
```

### Defining Components
Components in **PySpring** are classes that inherit from the Component class. These components can have dependencies on other components, which will be automatically injected.

## Example

Defining a Service Component
```python

from loguru import logger
from py_spring.core.entities.component import Component
from py_spring.core.entities.properties.properties import Properties

class ExampleProperties(Properties):
    __key__ = "example"
    value: str

class ExampleService(Component):
    example_properties: ExampleProperties

    def post_construct(self) -> None:
        logger.info(f"Example value: {self.example_properties.value}")

    def pre_destroy(self) -> None:
        logger.info("Pre destroy method called")

class AnotherExampleService(Component):
    example_service: ExampleService

    def post_construct(self) -> None:
        logger.info("AnotherExampleService post construct called")
        logger.info(f"Example value: {self.example_service.example_properties.value}")
```

In this example, `ExampleProperties` is a properties class that inherits from Properties. It represents the configuration properties that can be injected into services.
`ExampleService` is a component that depends on `ExampleProperties`.
`AnotherExampleService` is another component that depends on `ExampleService`.

### Lifecycle Methods
**PySpring** supports lifecycle methods:

- `post_construct`: This method is called after the component is fully constructed and its dependencies are injected.

- `pre_destroy`: This method is called before the component is destroyed, which is mostly used to release resources.

### Configuration
**PySpring** allows you to define application properties in a configuration file, such as `application-properties.json`. These properties are automatically mapped to the corresponding Properties class in your components.

#### Example Application Properties:
```json
{
    "example": {
        "value": "value"
    }
}
```
In this example, the example key in the JSON file is mapped to the `ExampleProperties` class. The value field is automatically injected into the ExampleProperties instance, which is then injected into `ExampleService`.

### Running the Application
Running your **PySpring** application is straightforward. **PySpring** handles all the initialization, dependency injection, and configuration loading automatically.

Simply use the `PySpringApplication` class to start your application:

```python
Copy code
from py_spring import PySpringApplication

if __name__ == "__main__":
    app = PySpringApplication()
    app.run()
```

In this example, creating an instance of `PySpringApplication` and calling the `run` method will automatically:

1. Load the configuration from your application-properties.json file.
2. Initialize all components.
3. Inject the necessary dependencies.
4. Create tables in `models.py` if declared.
5. Run the `FastAPI` web server.

This makes it incredibly easy to get your application up and running with minimal boilerplate code.

# Conclusion

With **PySpring**, setting up and managing your application's components and configuration is straightforward. The framework's automatic DI and configuration injection capabilities help you focus on building your application rather than managing its dependencies.