from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='grocrey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=30)),
                ('gprice', models.IntegerField()),
                ('ginfo', models.TextField()),
                ('gimg', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='vegitables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vname', models.CharField(max_length=30)),
                ('vprice', models.IntegerField()),
                ('vinfo', models.TextField()),
                ('vimg', models.FileField(upload_to='')),
            ],
        ),
    ]
