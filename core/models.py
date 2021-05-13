from django.db import models
from stdimage.models import StdImageField

# Signals
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    creation_date = models.DateField("creation date", auto_now_add=True)
    modified = models.DateField("update date", auto_now_add=True)
    active = models.BooleanField("active", default=True)

    class Meta:
        abstract = True


class Product(Base):
    image = StdImageField("image", upload_to="products", variations={'thumb': (124, 124)})
    name = models.CharField("name", max_length=100)
    price = models.DecimalField("price", decimal_places=2, max_digits=6)
    description = models.CharField("description", null=True, max_length=300)
    amount = models.IntegerField("amount")
    slug = models.SlugField('slug', max_length=100, blank=True, editable=False)

    def serialize(self):
        return {
            "name": self.name,
            "email": self.price,
            "description": self.description,
            "password": self.amount,
        }


def product_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)


signals.pre_save.connect(product_pre_save, sender=Product)
