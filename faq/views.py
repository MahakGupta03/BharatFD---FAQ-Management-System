from rest_framework import viewsets
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    # faq = FAQ(
    # question_en="Where are you from?",
    # answer_en="I am from Dewas."
    # )
    # faq.save()

    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'hi')
        queryset = self.get_queryset()
        data = [
            {
                'id': faq.id,
                'question': faq.get_translation(lang)['question'],
                'answer': faq.get_translation(lang)['answer']
            }
            for faq in queryset
        ]
        return Response(data)