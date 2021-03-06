# Generated by Django 3.1.3 on 2020-11-18 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='category',
            name='CATDesc',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CATImg',
            field=models.ImageField(upload_to='category/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CATName',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CATParent',
            field=models.ForeignKey(blank=True, limit_choices_to={'CATParent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Main Category'),
        ),
        migrations.CreateModel(
            name='Product_Alternative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PALNAlternatives', models.ManyToManyField(related_name='alternative_products', to='product.Product', verbose_name='Alternatives')),
                ('PALNProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_prodcut', to='product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Product Alternative',
                'verbose_name_plural': 'Product Alternatives',
            },
        ),
    ]
