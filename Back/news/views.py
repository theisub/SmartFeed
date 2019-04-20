from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

#from .models import usertag, User, Tag

@csrf_exempt
def init_user(request):
	if request.method == "OPTIONS":
		resp = JsonResponse(data="", status=200, safe=False)
		resp["Access-Control-Allow-Origin"] = '*'
		resp["Access-Control-Allow-Methods"] = "OPTIONS, POST"
		#resp["Access-Control-Max-Age"] = "1000"
		#resp["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
		return resp

	if request.method == "POST":
		user_and_tags = json.loads(request.body)
		nickname = user_and_tags['nickname']

		'''
		if usertag.objects.filter(user={'nickname': nickname}).exists():
			return JsonResponse("User have already existed", status = 400, safe=False)
		else:
			request_tags = []
			for tag in user_and_tags["tags"]:
				for k in tag:
					tag_name = k
					tag_koeff = tag[k]
					request_tags.append(Tag(tag_name, tag_koeff))

			q = usertag(user=User(nickname), tags=request_tags)
			q.save()

			return JsonResponse("User created", status = 200, safe=False)
		'''
		resp = JsonResponse("User created", status = 200, safe=False)
		resp['Access-Control-Allow-Origin'] = '*'

		return resp


@csrf_exempt
def get_news(request):
	if request.method == "OPTIONS":
		resp = JsonResponse(data="", status=200, safe=False)
		resp["Access-Control-Allow-Origin"] = '*'
		resp["Access-Control-Allow-Methods"] = "OPTIONS, POST"
		#resp["Access-Control-Max-Age"] = "1000"
		#resp["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
		return resp

	if request.method == "POST":
		user_and_tags = json.loads(request.body)
		nickname = user_and_tags['nickname']

		'''
		if usertag.objects.filter(user={'nickname': nickname}).exists():
			...
		else:
			return JsonResponse("User didn't existe", status = 400, safe=False)
		'''

		news_feed = {
		    "size": 10,
		    "articles": [
		        {
		            "img": "https://mobile-review.com/news/wp-content/uploads/dims2.jpg",
		            "url": "https://mobile-review.com/news/huawei-gotova-prodavat-chipy-5g-tolko-apple",
		            "title": "Huawei \u0433\u043e\u0442\u043e\u0432\u0430 \u043f\u0440\u043e\u0434\u0430\u0432\u0430\u0442\u044c \u0447\u0438\u043f\u044b 5G \u0442\u043e\u043b\u044c\u043a\u043e Apple",
		            "description": ""
		        },
		        {
		            "img": "https://s.appleinsider.ru/2019/04/iphonep1-1-1000x526.jpg",
		            "url": "https://appleinsider.ru/iphone/apple-razrabotala-novoe-zashhitnoe-pokrytie-dlya-iphone.html",
		            "title": "Apple \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0430\u043b\u0430 \u043d\u043e\u0432\u043e\u0435 \u0437\u0430\u0449\u0438\u0442\u043d\u043e\u0435 \u043f\u043e\u043a\u0440\u044b\u0442\u0438\u0435 \u0434\u043b\u044f iPhone",
		            "description": "\u0412\u043e\u0442 \u0443\u0436\u0435 \u043c\u043d\u043e\u0433\u043e \u043b\u0435\u0442 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u0438 \u0441\u043c\u0430\u0440\u0442\u0444\u043e\u043d"
		        },
		        {
		            "img": "https://fomag.ru/favicon.png",
		            "url": "https://fomag.ru/news/chto-proiskhodit-na-konkurse-prognozov-po-aktsiyam-apple/",
		            "title": "\u0427\u0442\u043e \u043f\u0440\u043e\u0438\u0441\u0445\u043e\u0434\u0438\u0442 \u043d\u0430 \u043a\u043e\u043d\u043a\u0443\u0440\u0441\u0435 \u043f\u0440\u043e\u0433\u043d\u043e\u0437\u043e\u0432 \u043f\u043e \u0430\u043a\u0446\u0438\u044f\u043c Apple",
		            "description": "\u041e\u0442 \u0431\u0438\u0442\u043a\u043e\u0438\u043d\u0430 \u0434\u043e \u043e\u0431\u043b\u0438\u0433\u0430\u0446\u0438\u0439, \u0441\u0435\u0433\u043e\u0434\u043d\u044f \u0442\u0430\u043a \u043c\u043d"
		        },
		        {
		            "img": "https://s.appleinsider.ru/2019/04/angled-500x263.jpg",
		            "url": "https://appleinsider.ru/eto-interesno/interesnye-fakty-o-titanovoj-versii-apple-card.html",
		            "title": "\u0418\u043d\u0442\u0435\u0440\u0435\u0441\u043d\u044b\u0435 \u0444\u0430\u043a\u0442\u044b \u043e \u0442\u0438\u0442\u0430\u043d\u043e\u0432\u043e\u0439 \u0432\u0435\u0440\u0441\u0438\u0438 Apple Card",
		            "description": "\u0414\u0432\u0435 \u043d\u0435\u0434\u0435\u043b\u0438 \u043d\u0430\u0437\u0430\u0434, 25 \u043c\u0430\u0440\u0442\u0430, \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u044f App"
		        },
		        {
		            "img": "https://s.appleinsider.ru/2019/04/HuaeweiP30Pro-500x263.jpg",
		            "url": "https://appleinsider.ru/iphone/apple-obvinili-v-ekonomii-na-kamerax-novyx-iphone.html",
		            "title": "Apple \u043e\u0431\u0432\u0438\u043d\u0438\u043b\u0438 \u0432 \u044d\u043a\u043e\u043d\u043e\u043c\u0438\u0438 \u043d\u0430 \u043a\u0430\u043c\u0435\u0440\u0430\u0445 \u043d\u043e\u0432\u044b\u0445 iPhone",
		            "description": "\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u0438 \u0444\u043b\u0430\u0433\u043c\u0430\u043d\u0441\u043a\u0438\u0445 "
		        },
		        {
		            "img": "https://img04.rl0.ru/bde2da8094a7a11ff8f2f99ffe7b9bb5/c600x315/news.rambler.ru/img/2019/04/09144639.839354.5567.jpg",
		            "url": "https://news.rambler.ru/tech/42006652-apple-vozrodit-ogromnyy-macbook-pro/",
		            "title": "Apple \u0432\u043e\u0437\u0440\u043e\u0434\u0438\u0442 \u043e\u0433\u0440\u043e\u043c\u043d\u044b\u0439 MacBook Pro",
		            "description": "Apple \u0432\u043e\u0437\u0440\u043e\u0434\u0438\u0442 \u043e\u0433\u0440\u043e\u043c\u043d\u044b\u0439 MacBook Pro\n\n\u0410\u043d\u0430"
		        },
		        {
		            "img": "https://www.mobile-review.com/articles/2019/image/echo-14/pic-scr/11.jpg",
		            "url": "https://www.mobile-review.com/articles/2019/echo-14.shtml",
		            "title": "Mobile-review.com #\u042d\u0445\u043e14: \u043a\u0430\u043a Google, Apple \u0438 Microsoft \u043c\u0435\u043d\u044f\u044e\u0442 \u0431\u0443\u0434\u0443\u0449\u0435\u0435 \u0438\u0433\u0440",
		            "description": "#\u042d\u0445\u043e14: \u043a\u0430\u043a Google, Apple \u0438 Microsoft \u043c\u0435"
		        },
		        {
		            "img": "https://s.appleinsider.ru/2019/04/macbloqueado-1000x526.jpg",
		            "url": "https://appleinsider.ru/tips-tricks/moshenniki-xotyat-ukrast-vash-apple-id-budte-ostorozhny.html",
		            "title": "\u041c\u043e\u0448\u0435\u043d\u043d\u0438\u043a\u0438 \u0445\u043e\u0442\u044f\u0442 \u0443\u043a\u0440\u0430\u0441\u0442\u044c \u0432\u0430\u0448 Apple ID. \u0411\u0443\u0434\u044c\u0442\u0435 \u043e\u0441\u0442\u043e\u0440\u043e\u0436\u043d\u044b",
		            "description": "\u0412\u0440\u0435\u043c\u044f \u043e\u0442 \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u043c\u043e\u0448\u0435\u043d\u043d\u0438\u043a\u0438 \u0430\u043a\u0442\u0438\u0432\u0438\u0437\u0438\u0440\u0443\u044e\u0442\u0441"
		        },
		        {
		            "img": "https://s.appleinsider.ru/2019/04/ntflx-1000x526.jpg",
		            "url": "https://appleinsider.ru/ios/zachem-netflix-vredit-apple-i-ee-polzovatelyam.html",
		            "title": "\u0417\u0430\u0447\u0435\u043c Netflix \u0432\u0440\u0435\u0434\u0438\u0442 Apple \u0438 \u0435\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f\u043c?",
		            "description": "\u041a\u043e\u043d\u043a\u0443\u0440\u0435\u043d\u0446\u0438\u044f \u2013 \u044d\u0442\u043e \u0432\u0441\u0435\u0433\u0434\u0430 \u043d\u0435\u0447\u0435\u0441\u0442\u043d\u043e. \u0415\u0441\u043b\u0438 "
		        },
		        {
		            "img": "https://cdn-st3.rtr-vesti.ru/vh/pictures/bq/194/743/4.jpg",
		            "url": "https://hitech.vesti.ru/article/1201635/",
		            "title": "\u0412 \u0421\u0428\u0410 \u0438\u0437\u043e\u0431\u0440\u0435\u043b\u0438 \"Apple II \u0432 \u043c\u0438\u0440\u0435 \u0440\u043e\u0431\u043e\u0442\u043e\u0432\"",
		            "description": ""
		        }
		    ]
		}
		resp = JsonResponse(news_feed, status = 200)
		resp['Access-Control-Allow-Origin'] = '*'
		
		return resp


@csrf_exempt
def news_click(request):
	if request.method == "OPTIONS":
		resp = JsonResponse(data="", status=200, safe=False)
		resp["Access-Control-Allow-Origin"] = '*'
		resp["Access-Control-Allow-Methods"] = "OPTIONS, POST"
		#resp["Access-Control-Max-Age"] = "1000"
		#resp["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
		return resp

	if request.method == "POST":
		user_and_url = json.loads(request.body)
		nickname = user_and_url["nickname"]
		url = user_and_url["url"]
		#print(nickname, url)
		#print("aaaaaaa")

		#koef updating...
		resp = JsonResponse("Koeff update", status = 200, safe=False)
		resp['Access-Control-Allow-Origin'] = '*'
		
		return resp


@csrf_exempt
def get_user_tags(request):
	if request.method == "OPTIONS":
		resp = JsonResponse(data="", status=200, safe=False)
		resp["Access-Control-Allow-Origin"] = '*'
		resp["Access-Control-Allow-Methods"] = "OPTIONS, POST"
		#resp["Access-Control-Max-Age"] = "1000"
		#resp["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
		return resp
	    
	if request.method == "POST":
		user = json.loads(request.body)
		nickname = user["nickname"]

		#tags = get_tags_from_db(nickname)
		tags = {"tags": [ 
		        {"Apple": 0.6},
		        {"Samsung": 0.55},
		        {"HTC": 0.5} 
    		]
    	}

		resp = JsonResponse(tags, status = 200)
		resp['Access-Control-Allow-Origin'] = '*'
		
		return resp