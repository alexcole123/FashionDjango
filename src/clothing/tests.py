from django.test import Client, TestCase, SimpleTestCase
from django.urls import resolve, reverse
from http import HTTPStatus
from django.contrib.auth.models import User
from .models import TypeModel, ClothingModel
from .views import fashion, list, details, insert, delete

class TestUrls(SimpleTestCase):

    def test_urls(self):
        url = reverse("fashion") #"fashion" = the name
        view_function = resolve(url).func
        self.assertEqual(view_function, fashion)

        url = reverse("clothing") 
        view_function = resolve(url).func
        self.assertEqual(view_function, list)

        url = reverse("details", args = [1]) 
        view_function = resolve(url).func
        self.assertEqual(view_function, details)

        url = reverse("insert") 
        view_function = resolve(url).func
        self.assertEqual(view_function, insert)

        url = reverse("delete", args = [1]) 
        view_function = resolve(url).func
        self.assertEqual(view_function, delete)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        accessories = TypeModel.objects.create(name = "Accessories")
        ClothingModel.objects.create(manufacturer = "Ray Ban", price = 250, type = accessories)
        ClothingModel.objects.create(manufacturer = "Teus", price = 8, type = accessories)
        ClothingModel.objects.create(manufacturer = "Rolex", price = 9, type = accessories)
        test_username= "tester@gmail.com"
        test_password = "testing1234"
        User.objects.create_superuser(username=test_username, password=test_password)
        self.client.login(username=test_username, password=test_password)


    def test_fashion(self):
        url = reverse("fashion")
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "fashion.html")
    
    def test_list(self):
        url = reverse("clothing")
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "clothing.html")
        self.assertContains(response, "Ray Ban")
        self.assertContains(response, "Teus")
        self.assertContains(response, "Rolex")

    def test_details(self):
        url = reverse("details", args= [1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "details.html")
        self.assertContains(response, "Ray Ban")

    def test_insert_get(self):
        url = reverse("insert")
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "insert.html")
        self.assertContains(response, "<form")
        self.assertContains(response, "</form>")

    def test_insert_post(self):
        url = reverse("insert") 
        form_data = {"manufacturer": "Castro", "price": 50, "type": 4}
        response = self.client.post(url, data= form_data, follow= True) #follow = True --> tells the client to follow all redirection until final result
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "clothing.html")
        existInDB = ClothingModel.objects.filter(manufacturer = "Castro").exists()
        self.assertTrue(existInDB)
        self.assertContains(response, "Castro")
        
    def test_edit_get(self):
        url = reverse("edit", args= [1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "edit.html")
        self.assertContains(response, "<form")
        self.assertContains(response, "</form>")

    def test_edit_post(self):
        url = reverse("edit", args= [1]) 
        form_data = {"manufacturer": "Versace", "price": 150, "type": 1}
        response = self.client.post(url, data= form_data, follow= True) #follow = True --> tells the client to follow all redirection until final result
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "clothing.html")
        existInDB = ClothingModel.objects.filter(manufacturer = "Versace").exists()
        self.assertTrue(existInDB)
        self.assertContains(response, "Versace")

    def test_delete(self):
        url = reverse("delete", args= [1])
        response = self.client.get(url, follow= True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        existInDB = ClothingModel.objects.filter(manufacturer = "Castro").exists()
        self.assertFalse(existInDB)

