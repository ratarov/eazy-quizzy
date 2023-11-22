from django import forms
from .models import QuestionResponse, Answer, Question


class QuestionResponseForm(forms.ModelForm):
    class Meta:
        model = QuestionResponse
        fields = ["answers"]

    def __init__(self, q, *args, **kwargs):
        super(QuestionResponseForm, self).__init__(*args, **kwargs)
        if q.input_type == Question.InputType.SINGLE:
            self.fields["answers"] = forms.ModelChoiceField(
                queryset=Answer.objects.filter(question=q),
                widget=forms.RadioSelect(),
            )
        else:
            self.fields["answers"] = forms.ModelMultipleChoiceField(
                queryset=Answer.objects.filter(question=q),
                widget=forms.CheckboxSelectMultiple(),
            )
