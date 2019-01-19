from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import medicine
from .serializers import MedicineSerializer


# Create your tests here.
class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_medicine(ItemCode="", Descr=""):
        if ItemCode != "" and Descr != "":
            medicine.objects.create(ItemCode=ItemCode, Descr=Descr)

    def setUp(self):
        # add test data
        self.create_medicine("dettol", "soap")
        self.create_medicine("savlon ", "handwash")
        self.create_medicine("crocine", "headache")
        self.create_medicine("paracitamol", "stomach pain")


class GetAllmedicineTest(BaseViewTest):

    def test_get_all_medicine(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the medicine endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("medicine-all", kwargs={"version": "v1"})
        )
        # fetch the data from db