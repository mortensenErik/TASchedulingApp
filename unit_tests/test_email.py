from django.test import TestCase
from django.core import mail

class testEmail(TestCase):

    def testSendEmail(self):
        mail.send_mail("Subject", "Test Email", "ejmonka@gmail.com", ["ejmonka@gmail.com"], fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "Subject")
