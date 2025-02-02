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