from django.db import models


# Create your models here. Ao criar um modelo python3 manage.py makemigrations
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("data de publicação")
    
    def __str__(self):
        return self.pub_date
# Comando acima retorna o texto da pergunta na lista de perguntas do django
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)