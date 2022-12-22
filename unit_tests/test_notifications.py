from django.test import TestCase
from django.core import mail


class testNotifications(TestCase):

    def testSendEmail(self):
        mail.send_mail("Urgent Message to all TAs", "Details", "tascheduler@uwm.edu", ["ejmonka@uwm.edu"],
                       fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "Urgent Message to all TAs")
