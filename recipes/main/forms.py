from django import forms

class CreateNewRecipe(forms.Form):
    name = forms.CharField(label='Recipe Name', max_length=200)
    author = forms.CharField(label='Author', max_length=50)
    # ingredients = forms.ModelMultipleChoiceField(queryset=Ingredient.objects.all())
    instructions = forms.CharField(widget=forms.Textarea)
    serving_size = forms.IntegerField(label='Serving Size')
