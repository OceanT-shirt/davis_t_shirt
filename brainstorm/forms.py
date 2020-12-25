from django import forms
from .models import Brainstorms


class BSForm(forms.ModelForm):
    """
   新規データ登録画面用のフォーム定義
   """

    class Meta:
        model = Brainstorms
        fields = ['date', 'title', 'answer1', 'answer2', 'answer3', 'answer4', 'answer5', 'answer6', 'answer7',
                  'answer8', 'answer9', 'answer10', 'answer11', 'answer12', 'answer13']
