from django import forms
from .models import TransportSchedule

class TransportScheduleForm(forms.ModelForm):
    class Meta:
        model = TransportSchedule
        fields = ['direction', 'time']
        widgets = {
            'travel_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        help_texts = {
            'direction': 'Enter "To Campus" or "From Campus".',
        }


from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['feedback_text', 'rating']
