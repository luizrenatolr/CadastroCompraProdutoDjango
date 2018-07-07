# Generated by Django 2.0.6 on 2018-06-23 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('preco_de_compra', models.FloatField()),
                ('preco_medio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('nome', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.Produto'),
        ),
    ]
