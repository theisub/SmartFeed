from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
#from working_with_news import

from .models import usertag, User, Tag, news

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

		request_tags = []
		for tag in user_and_tags["tags"]:
			for k in tag:
				tag_name = k
				tag_koeff = tag[k]
				request_tags.append(Tag(tag_name, tag_koeff))

		if usertag.objects.filter(user={'nickname': nickname}).exists():
			q = usertag.objects.get(user={'nickname': nickname})

			for tag in request_tags:
				tmp_tag_name = tag.tag_name
				will_append = True
				for existe_tags in q.tags:
					if existe_tags.tag_name == tmp_tag_name:
						will_append = False
						break
				if will_append:
					q.tags.append(tag)
		else:
			q = usertag(user=User(nickname), tags=request_tags,\
			 watched_news=[], clicked_news=[])
			
		q.save()
		
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
		user_and_get_param = json.loads(request.body)
		nickname = user_and_get_param['nickname']
		param = user_and_get_param['param']

		if usertag.objects.filter(user={'nickname': nickname}).exists():
			q = usertag.objects.get(user={'nickname': nickname})

			# prepare tags for news API
			tags_for_feed = {}
			for tag in q.tags:
				tags_for_feed[tag.tag_name] = tag.tag_koef

			'''
			if param == "refresh":
				news_feed = get_news_feed(tags_for_feed, q.clicked_news)
			else:
				blocked_news = q.watched_news
				for url in q.clicked_news:   # url arrays merge
					blocked_news.append(url)
				news_feed = get_news_feed(tags_for_feed, blocked_news)
			'''

			news_feed = {
			    "size": 10,
			    "articles": [
			        {
			            "img": "https://mobile-review.com/news/wp-content/uploads/dims2.jpg",
			            "url": "https://mobile-review.com/news/huawei-gotova-prodavat-chipy-5g-tolko-apple",
			            "title": "Huawei \u0433\u043e\u0442\u043e\u0432\u0430 \u043f\u0440\u043e\u0434\u0430\u0432\u0430\u0442\u044c \u0447\u0438\u043f\u044b 5G \u0442\u043e\u043b\u044c\u043a\u043e Apple",
			            "description": ""
			        }
			    ]
			}

			# store watched news
			for article in news_feed["articles"]:
				q.watched_news.append(news(article["url"]))
			q.save()

			resp = JsonResponse(news_feed, status = 200)
			resp['Access-Control-Allow-Origin'] = '*'
			
			return resp

		else:
			resp = JsonResponse("User didn't exist", status = 400, safe=False)
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
		
		q = usertag.objects.get(user={'nickname': nickname})
		q.clicked_news.append(news(url))

		#new_tags = update_tags(url, q.tags?)
		new_tags = {
					"Apple": 0.6,
			        "Samsung": 0.55,
			        "HTC": 0.5
    	}

    	#koef updating...
		for tag in new_tags:
			new_one = True
			for i in range(len(q.tags)):
				if tag == q.tags[i].tag_name:
					q.tags[i] = Tag(tag, new_tags[tag])
					new_one = False
					break
			if new_one:
				q.tags.append(Tag(tag, new_tags[tag]))

		q.save()
		
		resp = JsonResponse("Koeff updated", status = 200, safe=False)
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

		q = usertag.objects.get(user={'nickname': nickname})
		result = {"nickname": nickname, "tags": []}
		
		for tag in q.tags:
			result["tags"].append({tag.tag_name: tag.tag_koef})
		

		resp = JsonResponse(result, status = 200)
		resp['Access-Control-Allow-Origin'] = '*'
		
		return resp