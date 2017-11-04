from django import forms
from apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):

	class Meta:
		model=Mascota

		fields=[
			'nombre', 
			'sexo',
			'edad_aprox',
			'fecha_res',
			'persona',
			'vacuna',
		]


		labels={
			'nombre': 'Nombre', 
			'sexo': 'Sexo',
			'edad_aprox': 'Edad aproximada',
			'fecha_res': 'Fecha de rescate',
			'persona': 'Adoptante',
			'vacuna': 'Vacunas',
		}

		widgets={
			'nombre': forms.TextInput(attrs={'class':'form-control'}), 
			'sexo': forms.TextInput(attrs={'class':'form-control'}),
			'edad_aprox': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_res': forms.TextInput(attrs={'class':'form-control'}),
			'persona': forms.Select(attrs={'class':'form-control'}),
			'vacuna': forms.CheckboxSelectMultiple(),
		}



