# Sanskrit Sandhi Calculator

## Project Title
Sanskrit Sandhi Calculator

## Project Contributors
* **Name**:Sasidhara Kashyap Chaturvedula
* **Registration No**:24241D5809
* **Guide**:Dr. G Ramesh (Associate Professor)
* **Institution**: Gokaraju Rangaraju Institute of Engineering and Technology, Department of Computer Science and Engineering

## Academic Information
* **Academic Year**:2024-2025
* **Program**:M. Tech I Year / II semester
* **Branch**:CSE
* **Course Code**:GR24D5048 – MINI PROJECT

## Overview

This project implements a web-based Sanskrit Sandhi calculator. It allows users to input Sanskrit words and get the result of applying Sandhi rules to combine them.

## Objective

The primary objective of this project is to provide a user-friendly tool for demonstrating and calculating Sanskrit Sandhi. This can be helpful for students and enthusiasts of Sanskrit to understand how words combine according to grammatical rules.

## Abstract

The Sanskrit Sandhi Calculator is a web application built using the Flask framework. It takes two Sanskrit words as input from the user through a simple web interface. The backend processes these inputs, applies relevant Sanskrit Sandhi rules, and returns the combined word or phrase, which is then displayed to the user.

## Key Features

*   Web-based interface for easy access.
*   Calculates Sandhi for two input Sanskrit words.
*   Provides a clear output of the combined form.
*   Built with Flask for a lightweight and flexible web application.

## Project Requirements

To run this project, you will need:

*   Python 3.13
*   Flask
*   HTML
*   CSS
*   JavaScript
*   Poetry (for dependency management)
*   A Web Browser

The project dependencies are managed using Poetry and are listed in the `pyproject.toml` file. These dependencies will be automatically installed when you set up the environment using Poetry.

## Usage and Execution

This project is a web application built with Flask that provides a Sanskrit Sandhi calculator. To use and execute this code, follow the steps below:

### Setting up the Environment

1.  **Clone the repository:** If you haven't already, clone the project repository from its source.
2.  **Install Poetry:** This project uses Poetry for dependency management. If you don't have Poetry installed, follow the instructions on the official Poetry website: [https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation)
3.  **Install Dependencies:** Navigate to the project's root directory in your terminal and install the project dependencies using Poetry:
```
bash
    poetry install
    
```
This will create a virtual environment and install all the required libraries.

### Running the Application

1.  **Activate the virtual environment:** With Poetry, you can activate the project's virtual environment by running:
```
bash
    poetry shell
    
```
2.  **Run the Flask development server:** Once the virtual environment is active, you can start the Flask development server by executing the main application file:
```
bash
    python src/main.py
    
```
The server will typically start on `http://127.0.0.1:5000/`. You will see output in your terminal indicating that the server is running.

### Interacting with the Sanskrit Sandhi Calculator

1.  **Open your web browser:** Open your preferred web browser and navigate to the address where the Flask application is running (usually `http://127.0.0.1:5000/`).
2.  **Use the interface:** You will see a web page with input fields. Enter the Sanskrit words you want to combine using Sandhi into the provided input boxes.
3.  **Get the result:** The application will process your input and display the result of the Sandhi combination on the same page.















## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
