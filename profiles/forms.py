from django import forms

from . models import Profile

#Form to update user profile
class ProfileForm(forms.Form):
    name = forms.CharField(max_length=30, label='Name')
    location = forms.CharField(max_length=80, label='Location')
    image = forms.ImageField(required=False)

    def clean(self):
        #IF an image is uploaded use it as profile pic IF NOT use default image from media files
        self.cleaned_data = super().clean()
        image = self.cleaned_data.get('image')
        if not image:   self.cleaned_data['image'] = 'uploads/profile_pics/default.png'

    
    def signup(self, request, user):
        user.save()
        profile = Profile()
        profile.user = user
        profile.name = self.cleaned_data['name']
        profile.location = self.cleaned_data['location']
        profile.image = self.cleaned_data['image']
        profile.save()
