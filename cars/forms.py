from django import forms 
from cars.models import Car
import re


class CarlModelform(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value <20000:
            self.add_error('value', 'Valor minímo do carro deve ser de  R$ 20.000.')
            return value
        
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year <1975:
            self.add_error('factory_year','Não é possível cadastrar carros fabricados antes de 1975.')

    
    def clean_plate(self):
        plate = self.cleaned_data.get('plate')
        standard = re.compile (r'[A-Z][A-Z][A-Z][0-9][A-Z][0-9][0-9]')
        check = standard.match (plate)

        if check ==  None:
            self.add_error('plate','Incorreto o formato da placa deve ser como: ABC1D23')
            return plate
        