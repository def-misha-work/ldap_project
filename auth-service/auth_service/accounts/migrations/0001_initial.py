# Generated by Django 5.0.2 on 2024-05-03 14:37

import django.contrib.auth.models
import django.core.management.utils
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("companies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Role",
            fields=[],
            options={
                "verbose_name": "role",
                "verbose_name_plural": "roles",
                "db_table": "role",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("auth.group",),
            managers=[
                ("objects", django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "deleted",
                    models.DateTimeField(db_index=True, editable=False, null=True),
                ),
                (
                    "deleted_by_cascade",
                    models.BooleanField(default=False, editable=False),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        db_index=True,
                        max_length=512,
                        unique=True,
                        verbose_name="email address",
                    ),
                ),
                (
                    "secret_key",
                    models.CharField(
                        default=django.core.management.utils.get_random_secret_key,
                        max_length=255,
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=25,
                        null=True,
                        verbose_name="first name",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=25,
                        null=True,
                        verbose_name="last name",
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True, default=None, max_length=128, null=True
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("staff", models.BooleanField(default=False)),
                ("admin", models.BooleanField(default=False)),
                ("last_password_reset", models.DateTimeField(blank=True, null=True)),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="companies.company",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "db_table": "user",
                "permissions": (
                    ("view_user_id", "Can view user id"),
                    ("view_user_is_active", "Can view user status"),
                    ("change_user_data", "Can change user data"),
                    ("change_their_avatar", "Can change their avatar"),
                ),
            },
        ),
        migrations.CreateModel(
            name="RoleUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "role",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="accounts.role",
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "role")},
            },
        ),
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.ManyToManyField(
                related_name="users", through="accounts.RoleUser", to="accounts.role"
            ),
        ),
    ]
