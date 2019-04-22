import unittest
import requests


class TestStringMethods(unittest.TestCase):

  serv_url = "http://127.0.0.1:8000/"

  def test_init_user(self):
      j = {"nickname": "user1",
            "tags": [{"Apple": 0.5},
                     {"Samsung": 0.6},
                     {"HTC": 0.7}
            ]
      }

      r = requests.post(self.serv_url + "init_user/", json=j)

      self.assertEqual(r.status_code, 200)

  def test_get_news(self):
      j = {"nickname": "user1"}
      r = requests.post(self.serv_url + "get_news/", json=j)

      self.assertEqual(r.status_code, 200)

  def test_news_click(self):
      j = {"nickname": "user1",
           "url": "http://yandex.ru"}
      r = requests.post(self.serv_url + "news_click/", json=j)

      self.assertEqual(r.status_code, 200)

  def test_get_user_tags(self):
      j = {"nickname": "user1"}
      r = requests.post(self.serv_url + "get_user_tags/", json=j)

      self.assertEqual(r.status_code, 200)



if __name__ == '__main__':
    unittest.main()