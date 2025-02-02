from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question_en = models.TextField()
    answer_en = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        is_new = not self.pk

        if is_new:
            super().save(*args, **kwargs)
            
            translator = Translator()
            for lang in ['hi', 'bn']:
                try:
                    question_trans = translator.translate(self.question_en, dest=lang).text
                    answer_trans = translator.translate(self.answer_en, dest=lang).text
                    
                    setattr(self, f'question_{lang}', question_trans)
                    setattr(self, f'answer_{lang}', answer_trans)
                except Exception as e:
                    setattr(self, f'question_{lang}', self.question_en)
                    setattr(self, f'answer_{lang}', self.answer_en)
            
            kwargs.pop('force_insert', None)
            super().save(force_update=True, *args, **kwargs)
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.question_en[:50]

    def get_translation(self, lang):
        return {
            'question': getattr(self, f'question_{lang}', self.question_en),
            'answer': getattr(self, f'answer_{lang}', self.answer_en)
        }