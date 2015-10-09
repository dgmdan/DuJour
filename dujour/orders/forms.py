from django import forms

class AddItemForm(forms.Form):
    menu_item_id = forms.IntegerField()
    quantity = forms.IntegerField()
    comments = forms.CharField()

    def add_item(self):
        pass
