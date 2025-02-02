# Generated by Django 3.0.1 on 2019-12-20 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchaseitem',
            old_name='value',
            new_name='count',
        ),
        migrations.AlterField(
            model_name='purchaseitem',
            name='purchase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='Cart.Purchase'),
        ),
    ]
