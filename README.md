# Lab Report Generator

A Python-based tool that automatically generates well-structured lab reports using Google's Gemini AI API. The tool creates professional-looking lab reports in DOCX format with proper formatting and structure.

## Features

- Automated lab report generation using Gemini AI
- Well-structured output with proper sections (Objective, Theory, Implementation, Output, Conclusion)
- Professional document formatting with proper margins and font styles
- Support for code snippets with proper formatting
- Customizable output filename
- Command-line interface for easy usage

## Prerequisites

- Python 3.x
- Google Gemini API key (Get it from https://ai.google.dev/)


## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/lab-gen-pyscript.git
cd lab-gen-pyscript
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

You can run the script in two ways:

### 1. Interactive Mode
```bash
python labgen.py
```
The script will prompt you for:
- Your Gemini API key
- The lab report prompt
- Output filename (optional)

### 2. Command-line Arguments
```bash
python labgen.py --api YOUR_API_KEY --prompt "Your lab report prompt" --file output.docx
```

Arguments:
- `--api`: Your Gemini API key
- `--prompt`: The prompt for generating the lab report
- `--file`: Output filename (optional, defaults to lab_report.docx)

## Project Structure

```
lab-gen-pyscript/
│
├── labgen.py           # Main script file
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## Code Structure

The project consists of a main `LabReportGenerator` class with the following key methods:

- `__init__(api_key, filename)`: Initializes the generator with API key and output filename
- `get_genai_response(prompt)`: Fetches AI-generated content using the Gemini API
- `generate_document(data)`: Creates the formatted DOCX document

## Generated Report Structure

The generated lab report includes the following sections:

1. **TOPIC**: The main subject of the lab report
2. **OBJECTIVE**: Bullet points listing the goals of the lab
3. **THEORY**: Theoretical background and explanation
4. **IMPLEMENTATION**: Code implementation with proper formatting
5. **OUTPUT**: Space for screenshots or results
6. **CONCLUSION**: Summary of findings and results

## Sample Output

![alt text](<Screenshot 2025-09-10 102910.png>)

## Dependencies

- `google-genai`: Google Gemini AI API client
- `python-docx`: For creating and formatting Word documents
- Other dependencies listed in `requirements.txt`

## License



## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
Made with 💖 by Nischhal. 🌟 Star this project. thankss
