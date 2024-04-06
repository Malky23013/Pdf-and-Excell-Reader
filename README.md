# PDF and Excel Reader

This repository contains a Python application for reading and extracting data from PDF and Excel files.

## Features

- **PDF Reader**: Utilizes [PyPDF2](https://github.com/mstamy2/PyPDF2) library to extract text content from PDF files.
- **Excel Reader**: Employs [openpyxl](https://openpyxl.readthedocs.io/en/stable/) library to parse Excel files and extract data.

## Installation

1. Clone this repository to your local machine using:
    ```
    git clone https://github.com/your_username/pdf-excel-reader.git
    ```

2. Install the required Python libraries using pip:
    ```
    pip install -r requirements.txt
    ```

## Usage

1. **PDF Reader**:
    ```python
    from pdf_reader import PDFReader
    
    pdf_path = "path/to/pdf_file.pdf"
    pdf_reader = PDFReader(pdf_path)
    text_content = pdf_reader.extract_text()
    print(text_content)
    ```

2. **Excel Reader**:
    ```python
    from excel_reader import ExcelReader
    
    excel_path = "path/to/excel_file.xlsx"
    excel_reader = ExcelReader(excel_path)
    data = excel_reader.read_excel()
    print(data)
    ```

## Contributing

Contributions are welcome! Please feel free to submit any bug fixes or enhancements.

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -am 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Submit a pull request.

## Acknowledgments

- [PyPDF2](https://github.com/mstamy2/PyPDF2)
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/)
