Claro, aqui está um exemplo de um README em inglês para o seu projeto:

```markdown
# LoGate: Logic-Based Graphical Proposition Classifier

LoGate is a Python project that allows you to classify and analyze logical propositions using a graphical representation. It is designed to help you categorize and organize logical statements in a clear and structured manner.

## Getting Started

These instructions will help you get started with using LoGate for classifying logical propositions.

### Prerequisites

To run LoGate, you need to have Python 3.x installed on your system. You can download Python from the official website: [Python Official Website](https://www.python.org/downloads/)

You'll also need to install the required Python packages using pip:

```bash
pip install spacy
pip install en_core_web_sm
```

### Installing

1. Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/LoGate.git
```

2. Navigate to the project directory:

```bash
cd LoGate
```

3. Run the project:

```bash
python main.py
```

## Usage

LoGate allows you to manually classify logical propositions by specifying the type of each proposition. You can also use the spaCy-based automatic classification for more advanced analysis. Here's how to use LoGate:

### Manual Classification

1. Open `main.py`.

2. Manually classify logical propositions by providing the proposition and its type using the `frases_classificadas` list.

3. Run the script:

```bash
python main.py
```

The script will classify the propositions and display the results.

### Automatic Classification

1. Open `main.py`.

2. Use the `classify_proposition` function to automatically classify a logical proposition. For example:

```python
result = classify_proposition(Phrase("This is a logical proposition", 8, "main"))
```

3. Run the script:

```bash
python main.py
```

The script will use spaCy to automatically classify the proposition and display the results.

## Contributing

We welcome contributions to LoGate. If you have any ideas or improvements, feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thank you to the spaCy project for providing a powerful natural language processing library.
- Special thanks to the contributors and maintainers of this project.


*Happy classifying!*
