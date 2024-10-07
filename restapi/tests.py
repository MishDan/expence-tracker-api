from django.test import TestCase
from unicodedata import category

from restapi import models

# Create your tests here.


class TestModels(TestCase):
    def test_expense(self):
        expense = models.Expence.objects.create(
            amount=249.99,
            merchant="amazon",
            description="anc headphones",
            category="music",
        )
        inserted_expense = models.Expence.object.get(pk=expense.id)

        self.assertEqual(249.99, inserted_expense.amount)
        self.assertEqual("amazon", inserted_expense.merchant)
        self.assertEqual("anc headphones", inserted_expense.description)
        self.assertEqual("music", inserted_expense.category)
