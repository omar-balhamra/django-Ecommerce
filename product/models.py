from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Product(models.Model):
    PRDName = models.CharField(max_length=100, verbose_name=_("Product Name"))
    # category =
    PRDDesc = models.TextField(verbose_name=_("Description"))
    PRDPrice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Price"))
    PRDCost = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Cost"))
    PRDCreated = models.DateTimeField(verbose_name=_("Created At"))
     
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products") 


    def __str__(self):
        return self.PRDName


class ProductImage(models.Model):
    PRDIProduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
    PRDIImage = models.ImageField(upload_to='product/', verbose_name=_("Image"))


    def __str__(self):
        return str(self.PRDIProduct)


class Category(models.Model):
    CATName = models.CharField(max_length=50, verbose_name=_("Name"))
    CATParent = models.ForeignKey('self', limit_choices_to={'CATParent__isnull' : True}, verbose_name=_("Main Category"), on_delete=models.CASCADE, blank=True, null=True)
    CATDesc = models.TextField(verbose_name=_("Description"))
    CATImg = models.ImageField(upload_to='category/', verbose_name=_("Image"))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


    def __str__(self):
        return (self.CATName)

class Product_Alternative(models.Model):
    PALNProduct = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='main_prodcut' , verbose_name=_("Product"))
    PALNAlternatives = models.ManyToManyField(Product , related_name='alternative_products'  , verbose_name=_("Alternatives"))
    
    class Meta:
        verbose_name = _("Product Alternative")
        verbose_name_plural = _("Product Alternatives")

    def __str__(self):
        return str(self.PALNProduct)


class Product_Accessorie(models.Model):
    PACCProduct = models.ForeignKey(Product, verbose_name=_("Product"), related_name='mainAccessory_prodcut', on_delete=models.CASCADE)
    PACCAlternatives = models.ManyToManyField(Product, verbose_name=_("Accessories"), related_name='accessories_products' )

    class Meta:
        verbose_name = _("Product Accessory")
        verbose_name_plural = _("Product Accessories")

    def __str__(self):
        return str(self.PACCProduct)

   
# category
# images
# alternatives
# accessoires        

    


