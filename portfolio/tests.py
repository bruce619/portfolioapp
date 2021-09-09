from django.test import TestCase, SimpleTestCase
from django.shortcuts import reverse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



class HomePageTest(SimpleTestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_title(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.assertEquals(self.driver.title, "My App")

    
    def test_increase(self):
        self.driver.get('http://127.0.0.1:8000/')
        increase = self.driver.find_element_by_id("increase")
        for i in range(3):
            increase.click()
        self.assertEqual(self.driver.find_element_by_tag_name('h1').text, "3")

    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_home_url_name(self):
        response = self.client.get(reverse("home"))
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(reverse("home"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "portfolio/home.html")

    def tearDown(self):
        self.driver.close()







