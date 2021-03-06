# Generated by Django 4.0.2 on 2022-06-03 14:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Died')),
                ('some_information', models.TextField(help_text='Enter here some information about this actor', max_length=1000)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter here a name of film', max_length=200)),
                ('description', models.TextField(help_text='Enter here please some information about film.', max_length=1000)),
                ('actor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pagecatalog.actor')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a film genre(e.g. Science Fiction)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter here film language (e.g. English)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter here to producer of film.', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FilmOrder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular film across whole catalog', primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('was_watched', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('w', 'Was watched'), ('a', 'Available'), ('m', 'Still make'), ('r', 'Reserved'), ('t', 'Maintenance')], default='t', help_text='Film availability', max_length=1)),
                ('film', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='pagecatalog.film')),
            ],
            options={
                'ordering': ['was_watched'],
            },
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ManyToManyField(help_text="Select a genre for this film.<a href='https://en.wikipedia.org/wiki/Film_genre'>Genres</a>", to='pagecatalog.Genre'),
        ),
        migrations.AddField(
            model_name='film',
            name='language',
            field=models.ManyToManyField(help_text='Select a language for this film.', to='pagecatalog.Language'),
        ),
        migrations.AddField(
            model_name='film',
            name='producer',
            field=models.ManyToManyField(help_text='Select a producer for this film.', to='pagecatalog.Producer'),
        ),
    ]
