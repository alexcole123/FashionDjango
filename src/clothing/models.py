from django.db.models import Model, CharField, DecimalField, ForeignKey, RESTRICT
from django.forms import ModelForm, TextInput, NumberInput, Select
from django.core.validators import MinLengthValidator, MaxLengthValidator, MaxValueValidator, MinValueValidator



# Type model:
class TypeModel(Model):

    # First column - id - will be created automatically.

    # Second column: 
    name = CharField(max_length = 50)

    #__str__ magic method:
    def __str__(self):
        return self.name

    # Metadata:
    class Meta:
        db_table = "type"


# --------------------------------------------------------------------


# Product model:
class ClothingModel(Model):

    # First column - id - will be created automatically.

    # Second column: 
    manufacturer = CharField(max_length = 50, validators=[MinLengthValidator(2), MaxLengthValidator(100)])

    # Third column:
    price = DecimalField(max_digits = 5, decimal_places = 2, validators=[MinValueValidator(0, "Price can't be negative."), MaxValueValidator(1000)])

    # Four column (relation):
    type = ForeignKey(TypeModel, on_delete = RESTRICT)

    # Metadata:
    class Meta:
        db_table = "clothing"


# --------------------------------------------------------------------

class ClothingForm(ModelForm):

    class Meta:
        model = ClothingModel
        exclude = ["id"]

        widgets = {
            "manufacturer": TextInput(attrs = {"class": "form-control", "minlength": 2, "maxlength": 100}), #attrs = HTML attributes
            "price": NumberInput(attrs = {"class": "form-control", "min": 0, "max": 1000}), 
            "type": Select(attrs = {"class": "form-control"}), 
        }