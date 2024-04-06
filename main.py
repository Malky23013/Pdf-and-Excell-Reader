from PyPDF2 import PdfReader
import pandas as pd
from openai import OpenAI
# הגדרת מפתח ה-API
api_key = "secret"

# יצירת client עם ה-API key
client = OpenAI(api_key=api_key)


def extract_text_from_pdf(file_path):
    # קריאת קובץ PDF
    with open(file_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        num_pages = len(pdf_reader.pages)  # מספר העמודים במסמך

        # קריאת כל העמודים ואיחודם לטקסט אחד
        text = ''
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

        return text
def extract_text_from_excel(file_path):
    try:
        # קריאת קובץ Excel
        excel_data = pd.read_excel(file_path)

        # המרת הנתונים לטקסט
        text = ''
        for column in excel_data.columns:
            for row in excel_data[column]:
                text += str(row) + ' '

        return text
    except Exception as e:
        print(f"Error reading Excel: {e}")
        return None

# פונקציה זו מקבלת את הטקסט ושולחת אותו לניתוח באמצעות OpenAI
def analyze_text(text):
    section_name = "Business Plan"  # הגדרת שם חלק התוכנית
    user_input = "Your project idea here"  # הגדרת הרעיון לתוכנית העסקית שלך

    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': text}
        ],
        temperature=1,
        max_tokens=500,
    )
    return response

# נתיב לקובץ PDF
file_path = 'C:/Users/User/Downloads/Receipt-2428-1456.pdf'

# קריאת המלל מהקובץ
extracted_text = extract_text_from_pdf(file_path)
excel_file_path = 'C:/Users/User/Downloads/מעברים.xlsx'

# קריאת המלל מהקובץ
extracted_text = extract_text_from_excel(excel_file_path)
#print(extracted_text)
# שליחת הטקסט לניתוח באמצעות OpenAI
analysis_result = analyze_text(extracted_text)

# הדפסת תוצאת הניתוח מ-OpenAI
print(analysis_result.choices[0].message)

