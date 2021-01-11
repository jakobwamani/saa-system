from django import forms
from mis.models import stock

class InStockForm(forms.ModelForm):
    product_name = forms.CharField(max_length=200)
    quantity = forms.IntegerField()
    cost_price = forms.IntegerField()
    category = forms.CharField(max_length=200)
    selling_price = forms.IntegerField()
    pub_date = forms.DateField()

    class Meta:
        model = stock
        fields = ['product_name','quantity','cost_price','category','selling_price','pub_date']
        

      

class SearchForm(forms.Form):
    searched_product = forms.CharField()
    def clean_searched_product(self):
        data = self.cleaned_data['searched_product']
        return data
