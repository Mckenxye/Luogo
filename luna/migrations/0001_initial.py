# Generated by Django 5.1.1 on 2024-09-20 01:20

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo electrónico')),
                ('user_type', models.CharField(choices=[('Administrador', 'Administrador'), ('Cliente', 'Cliente')], default='Cliente', max_length=50)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='customuser_set', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='customuser_set', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id_reserva', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(verbose_name='Fecha de la reserva')),
                ('hora', models.TimeField(verbose_name='Hora de la reserva')),
                ('numero_personas', models.IntegerField(verbose_name='Número de personas')),
                ('correo_cliente', models.EmailField(max_length=254, verbose_name='Correo del cliente')),
                ('telefono_cliente', models.CharField(max_length=15, verbose_name='Teléfono del cliente')),
                ('administrador', models.ForeignKey(limit_choices_to={'user_type': 'Administrador'}, on_delete=django.db.models.deletion.CASCADE, related_name='reservas_administrador', to=settings.AUTH_USER_MODEL, verbose_name='Administrador')),
                ('cliente', models.ForeignKey(limit_choices_to={'user_type': 'Cliente'}, on_delete=django.db.models.deletion.CASCADE, related_name='reservas_cliente', to=settings.AUTH_USER_MODEL, verbose_name='Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='restaurante',
            fields=[
                ('id_restaurante', models.AutoField(primary_key=True, serialize=False)),
                ('logo_restaurante', models.ImageField(null=True, upload_to='imagenes/', verbose_name='logo')),
                ('nombre_restaurante', models.CharField(max_length=50, verbose_name='Nombre del restaurante')),
                ('telefono', models.CharField(max_length=50, verbose_name='Teléfono')),
                ('numero_de_local', models.CharField(max_length=50, verbose_name='Direccion')),
                ('correo_de_local', models.CharField(max_length=50, verbose_name='Correo')),
                ('usuario_administrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurantes', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Administrador')),
            ],
        ),
        migrations.CreateModel(
            name='plato',
            fields=[
                ('Id_plato', models.AutoField(primary_key=True, serialize=False)),
                ('imagen', models.ImageField(upload_to='imagenes/', verbose_name='Imagen')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('descripcion', models.CharField(max_length=1000, verbose_name='descripcion')),
                ('Id_restaurante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luna.restaurante', verbose_name='Id_restaurante')),
            ],
        ),
    ]