from django import forms

from my_plant_app.web.models import Profile, Plant


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields='__all__'

# class ProfileDetailsForm(ProfileBaseForm):
#     def save(self, *args, **kwargs):
#         self.full_name = f"{self.first_name} {self.last_name}"
#         super().save(*args, **kwargs)



class CreateProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields='username', 'first_name', 'last_name'

class EditProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields='username', 'first_name', 'last_name', 'profile_picture'

class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields='__all__'
        def __init__(self):
            self.instance = None

        def save(self, commit=True):
            if commit:
                Plant.objects.all().delete()
                self.instance.delete()
            return self.instance

class PlantBaseForm(forms.ModelForm):
    class Meta:
        model=Plant
        fields='__all__'
class PlantCreateForm(PlantBaseForm):
    pass

class PlantEditForm(PlantBaseForm):
    pass

class PlantDeleteForm(PlantBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = ['readonly']