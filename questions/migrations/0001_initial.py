# Generated by Django 2.2 on 2020-12-12 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=150)),
                ('answer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='correct_answer', to='questions.Answer')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='questions.Category')),
                ('choices', models.ManyToManyField(related_name='choices', to='questions.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_name', models.CharField(max_length=150)),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='questions.Category')),
                ('question', models.ManyToManyField(blank=True, to='questions.Question')),
            ],
            options={
                'verbose_name_plural': 'Quizes',
            },
        ),
    ]
