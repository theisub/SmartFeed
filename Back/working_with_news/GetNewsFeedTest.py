import unittest
from GetFeed import SortNewsByInterest,FormUserFeed
from NewsFetch import GetResponses,GetTxt
class TestNewsFeedMethods(unittest.TestCase):

    def test_normal_res(self):
        original_news =  [
        {
            "img": "https://mobile-review.com/news/wp-content/uploads/dims2.jpg",
            "url": "https://mobile-review.com/news/huawei-gotova-prodavat-chipy-5g-tolko-apple",
            "title": "Huawei \u0433\u043e\u0442\u043e\u0432\u0430 \u043f\u0440\u043e\u0434\u0430\u0432\u0430\u0442\u044c \u0447\u0438\u043f\u044b 5G \u0442\u043e\u043b\u044c\u043a\u043e Apple",
            "description": "",
            "coef":0.5
        },
        {
            "img": "https://s.appleinsider.ru/2019/04/iphonep1-1-1000x526.jpg",
            "url": "https://appleinsider.ru/iphone/apple-razrabotala-novoe-zashhitnoe-pokrytie-dlya-iphone.html",
            "title": "Apple \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0430\u043b\u0430 \u043d\u043e\u0432\u043e\u0435 \u0437\u0430\u0449\u0438\u0442\u043d\u043e\u0435 \u043f\u043e\u043a\u0440\u044b\u0442\u0438\u0435 \u0434\u043b\u044f iPhone",
            "description": "\u0412\u043e\u0442 \u0443\u0436\u0435 \u043c\u043d\u043e\u0433\u043e \u043b\u0435\u0442 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u0438 \u0441\u043c\u0430\u0440\u0442\u0444\u043e\u043d",
            "coef":0.3
        },
        {
            "img": "https://fomag.ru/favicon.png",
            "url": "https://fomag.ru/news/chto-proiskhodit-na-konkurse-prognozov-po-aktsiyam-apple/",
            "title": "\u0427\u0442\u043e \u043f\u0440\u043e\u0438\u0441\u0445\u043e\u0434\u0438\u0442 \u043d\u0430 \u043a\u043e\u043d\u043a\u0443\u0440\u0441\u0435 \u043f\u0440\u043e\u0433\u043d\u043e\u0437\u043e\u0432 \u043f\u043e \u0430\u043a\u0446\u0438\u044f\u043c Apple",
            "description": "\u041e\u0442 \u0431\u0438\u0442\u043a\u043e\u0438\u043d\u0430 \u0434\u043e \u043e\u0431\u043b\u0438\u0433\u0430\u0446\u0438\u0439, \u0441\u0435\u0433\u043e\u0434\u043d\u044f \u0442\u0430\u043a \u043c\u043d",
            "coef":0.6
        }]
        expected_news = [
        {
            "img": "https://fomag.ru/favicon.png",
            "url": "https://fomag.ru/news/chto-proiskhodit-na-konkurse-prognozov-po-aktsiyam-apple/",
            "title": "\u0427\u0442\u043e \u043f\u0440\u043e\u0438\u0441\u0445\u043e\u0434\u0438\u0442 \u043d\u0430 \u043a\u043e\u043d\u043a\u0443\u0440\u0441\u0435 \u043f\u0440\u043e\u0433\u043d\u043e\u0437\u043e\u0432 \u043f\u043e \u0430\u043a\u0446\u0438\u044f\u043c Apple",
            "description": "\u041e\u0442 \u0431\u0438\u0442\u043a\u043e\u0438\u043d\u0430 \u0434\u043e \u043e\u0431\u043b\u0438\u0433\u0430\u0446\u0438\u0439, \u0441\u0435\u0433\u043e\u0434\u043d\u044f \u0442\u0430\u043a \u043c\u043d",
            "coef":0.6
        },
        {
            "img": "https://mobile-review.com/news/wp-content/uploads/dims2.jpg",
            "url": "https://mobile-review.com/news/huawei-gotova-prodavat-chipy-5g-tolko-apple",
            "title": "Huawei \u0433\u043e\u0442\u043e\u0432\u0430 \u043f\u0440\u043e\u0434\u0430\u0432\u0430\u0442\u044c \u0447\u0438\u043f\u044b 5G \u0442\u043e\u043b\u044c\u043a\u043e Apple",
            "description": "",
            "coef":0.5
        },
        {
            "img": "https://s.appleinsider.ru/2019/04/iphonep1-1-1000x526.jpg",
            "url": "https://appleinsider.ru/iphone/apple-razrabotala-novoe-zashhitnoe-pokrytie-dlya-iphone.html",
            "title": "Apple \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0430\u043b\u0430 \u043d\u043e\u0432\u043e\u0435 \u0437\u0430\u0449\u0438\u0442\u043d\u043e\u0435 \u043f\u043e\u043a\u0440\u044b\u0442\u0438\u0435 \u0434\u043b\u044f iPhone",
            "description": "\u0412\u043e\u0442 \u0443\u0436\u0435 \u043c\u043d\u043e\u0433\u043e \u043b\u0435\u0442 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u0438 \u0441\u043c\u0430\u0440\u0442\u0444\u043e\u043d",
            "coef":0.3
        }  
        ]
        res = SortNewsByInterest(original_news)
        self.assertEqual(res,expected_news)
    
    def test_form_feed(self):

        original_news =  [
        {
            "img": "https://mobile-review.com/news/wp-content/uploads/dims2.jpg",
            "url": "https://mobile-review.com/news/huawei-gotova-prodavat-chipy-5g-tolko-apple",
            "title": "Huawei \u0433\u043e\u0442\u043e\u0432\u0430 \u043f\u0440\u043e\u0434\u0430\u0432\u0430\u0442\u044c \u0447\u0438\u043f\u044b 5G \u0442\u043e\u043b\u044c\u043a\u043e Apple",
            "description": "",
            "coef":0.5
        }]
        expected_news =  {
        
            'size':1,
            'articles':[{
            "img": "https://mobile-review.com/news/wp-content/uploads/dims2.jpg",
            "url": "https://mobile-review.com/news/huawei-gotova-prodavat-chipy-5g-tolko-apple",
            "title": "Huawei \u0433\u043e\u0442\u043e\u0432\u0430 \u043f\u0440\u043e\u0434\u0430\u0432\u0430\u0442\u044c \u0447\u0438\u043f\u044b 5G \u0442\u043e\u043b\u044c\u043a\u043e Apple",
            "description": ""
            }]
        }
        res = FormUserFeed(original_news)
        self.assertEqual(res,expected_news)
        
    def test_empty_sort(self):
        res = SortNewsByInterest('')
        self.assertEqual(res,'')

   # def test_get_txt(self):
   #     url = dict()
   #     url['url'] = "https://github.com/theisub/Unknown/blob/master/README.md"
   #     url['tag'] = 'git'
   #     url['coef'] = 0.5
   #     res = GetTxt(url)
   #     print(res)
   #     self.assertEqual(res,'')

    def test_get_empty(self):
        url = dict()
        url['url'] = ""
        res = GetTxt(url)
        self.assertEqual(res,'')


    

if __name__ == '__main__':
    unittest.main()