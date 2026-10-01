from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Perfume",
            fields=[
                ("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),
                ("nombre",models.CharField(max_length=180)),
                ("marca",models.CharField(max_length=100)),
                ("categoria",models.CharField(max_length=80)),
                ("descripcion",models.TextField()),
                ("precio",models.DecimalField(decimal_places=2,max_digits=8)),
                ("imagen",models.ImageField(blank=True,null=True,upload_to="perfumes/")),
                ("fecha",models.DateTimeField(auto_now_add=True)),
                ("disponible",models.BooleanField(default=True)),
            ],
            options={"ordering":["-fecha"]},
        ),
        migrations.CreateModel(
            name="ArchivoSubido",
            fields=[
                ("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),
                ("nombre",models.CharField(max_length=180)),
                ("archivo",models.FileField(upload_to="archivos/")),
                ("fecha",models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
