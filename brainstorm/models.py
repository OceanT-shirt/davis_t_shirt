from django.db import models
from datetime import datetime


class Brainstorms(models.Model):
    class Meta:
        db_table = "brainstorms"
        verbose_name = "アイデア"
        verbose_name_plural = "アイデア"

    date = models.DateField(verbose_name="日付", default=datetime.now)
    title = models.CharField(verbose_name="タイトル", max_length=50)
    answer1 = models.TextField(verbose_name="そのサービスはどのような課題を解決するの？", null=True, blank=True)
    answer2 = models.TextField(verbose_name="もし新聞に取り上げられたらどんな記事になる？", null=True, blank=True)
    answer3 = models.TextField(verbose_name="ほかの商品・サービスに例えると？", null=True, blank=True)
    answer4 = models.TextField(verbose_name="一言でそのサービスを紹介すると？", null=True, blank=True)
    answer5 = models.TextField(verbose_name="友人に勧めるならどう勧める？", null=True, blank=True)
    answer6 = models.TextField(verbose_name="競合するサービスに対する優位性は？", null=True, blank=True)
    answer7 = models.TextField(verbose_name="回答", null=True, blank=True)
    answer8 = models.TextField(verbose_name="回答", null=True, blank=True)
    answer9 = models.TextField(verbose_name="回答", null=True, blank=True)
    answer10 = models.TextField(verbose_name="回答", null=True, blank=True)
    answer11 = models.TextField(verbose_name="回答", null=True, blank=True)
    answer12 = models.TextField(verbose_name="回答", null=True, blank=True)
    answer13 = models.TextField(verbose_name="回答", null=True, blank=True)

    def __str__(self):
        return self.title
