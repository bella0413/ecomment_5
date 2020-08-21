from django import forms
from .models import Post,Category

#cats= [('cosmetic','cosmetic'),('womens','womens'),('children','children'),('organic','organic')]
choices = Category.objects.all().values_list('name','name')
choice_list = []
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=('title','category','text','image',)

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'category' : forms.Select(choices=choice_list,attrs={'class':'form-control','placeholder':'choose a category'},),
            'author' : forms.Select(attrs={'class':'form-control'}),
            'text': forms.TextInput(attrs={'class':'form-control'}),
        }