from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketAdmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grocrey',
            name='gamm',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='vegitables',
            name='vamm',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='grocrey',
            name='gimg',
            field=models.ImageField(upload_to='static/imagesg/'),
        ),
        migrations.AlterField(
            model_name='vegitables',
            name='vimg',
            field=models.ImageField(upload_to='static/imagesv/'),
        ),
    ]
