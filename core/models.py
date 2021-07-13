import uuid
from django.db import models
from stdimage.models import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return filename


class Base(models.Model):
    creation_date = models.DateField("creation date", auto_now_add=True)
    modified = models.DateField("update date", auto_now_add=True)
    active = models.BooleanField("active", default=True)

    class Meta:
        abstract = True


class Info(Base):
    ICON_CHOICES = {
        ("icon-instagram", "Instagram"),
        ("icon-email", "Email"),
        ("icon-phone", "Phone"),
    }

    service = models.CharField("service", max_length=100)
    description = models.CharField("description", max_length=200)
    icon = models.CharField("icon", max_length=14, choices=ICON_CHOICES)

    class Meta:
        verbose_name = "Contact information"

    def serialize(self):
        return self.service


class Product(Base):
    image = StdImageField("image", upload_to=get_file_path, variations={'thumb': (124, 124)})
    name = models.CharField("name", max_length=100)
    price = models.DecimalField("price", decimal_places=2, max_digits=6)
    description = models.CharField("description", null=True, max_length=300)
    size = models.CharField('size', max_length=5)
    amount = models.IntegerField("amount")
    slug = models.SlugField('slug', max_length=100, blank=True, editable=False)

    def serialize(self):
        return {
            "name": self.name,
            "amount": self.amount,
            "price": self.price,
            "description": self.description
        }


def product_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)


signals.pre_save.connect(product_pre_save, sender=Product)
