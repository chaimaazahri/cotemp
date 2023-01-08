from django.db import models
from django.core.mail import send_mail
from django.db import models
import telepot
from django.db.models import FloatField


class Dht(models.Model):
    temp = models.FloatField(null=True)
    hum = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True, null=True)

    def _str_(self):
        return str(self.temp)

    def save(self, *args, **kwargs):
        if self.temp < 2 :
            token = '5830022921:AAFz-iLfWpvRat4yp1Ph8YtZxvpXABYuYAY'
            rece_id = 676259354
            bot = telepot.Bot(token)
            bot.sendMessage(rece_id, 'Attention !!!  Veuillez réparer le problème. La température de votre frigo est critique :' + str(self.temp) )
            print(bot.sendMessage(rece_id, '):' + str(self.temp)))
            send_mail(
                'Temperature',
                'Attention !!!  Veuillez réparer le problème. La température de votre frigo est critique :' + str(self.temp),
                'chaimaa.zahri@ump.ac.ma',
                ['chourakfarah@gmail.com'],
                fail_silently=False,
            )

        elif self.temp > 8 :
            token = '5830022921:AAFz-iLfWpvRat4yp1Ph8YtZxvpXABYuYAY'
            rece_id = 676259354
            bot = telepot.Bot(token)
            bot.sendMessage(rece_id, 'Attention !!!  Veuillez réparer le problème. La température de votre frigo est sévère :' + str(self.temp))
            print(bot.sendMessage(rece_id, 'Attention !!!  Veuillez réparer le problème. La température de votre frigo est sévère :' + str(self.temp)))
            send_mail(
                'Temperature',
                'Attention !!!  Veuillez réparer le problème. La température de votre frigo est sévère :' + str(self.temp),
                'chaimaa.zahri@ump.ac.ma',
                ['chourakfarah@gmail.com'],
                fail_silently=False,
            )
        return super().save(*args, **kwargs)
