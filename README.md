# FAQ Management System

This is a Django-based FAQ Management System that allows users to manage frequently asked questions and their translations.

## Project Structure

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/MahakGupta03/BharatFD---FAQ-Management-System.git
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv env
    ```

3. **Activate the virtual environment:**
    - On Windows:
        ```sh
        .\env\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source env/bin/activate
        ```

4. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

5. **Run migrations:**
    ```sh
    python manage.py migrate
    ```

6. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

## Usage

- Access the application at `http://127.0.0.1:8000/`.
- Use the Django admin interface to manage FAQs.

## Models

The FAQ model includes fields for questions and answers in English, Hindi, and Bengali. When a new FAQ is created, the English question and answer are automatically translated into Hindi and Bengali using the Google Translate API.

## Running Tests

1. **Install [pytest](http://_vscodecontentref_/7) and [pytest-django](http://_vscodecontentref_/8):**
    ```sh
    pip install pytest pytest-django
    ```

2. **Create a [pytest.ini](http://_vscodecontentref_/9) file in the root directory with the following content:**
    ```ini
    [pytest]
    DJANGO_SETTINGS_MODULE = config.settings
    python_files = tests.py
    ```

3. **Run the tests:**
    ```sh
    pytest
    ```

### Example Test

The [tests.py](http://_vscodecontentref_/10) file contains a test for the FAQ model:

```python
import pytest
from faq.models import FAQ

@pytest.mark.django_db
def test_faq_creation():
    faq = FAQ.objects.create(
        question_en="Where are you from?",
        answer_en="I am from Dewas."
    )
    assert faq.question_hi is not None
    assert faq.answer_hi is not None
    assert faq.question_bn is not None
    assert faq.answer_bn is not None
