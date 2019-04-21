from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from working_with_news.GetNews import get_news_feed

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

			# prepare block_news for news API
			blocked_news = []
			for clicked_news_url in q.clicked_news:
				blocked_news.append(clicked_news_url.url)

			if param == "refresh":
				news_feed = get_news_feed(tags_for_feed, blocked_news)
			else:
				for watched_news_url in q.watched_news:   # url arrays merge
					blocked_news.append(watched_news_url.url)
				print(blocked_news)
				news_feed = get_news_feed(tags_for_feed, blocked_news)

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

		'''
		# prepare tags for news API
		tags_for_feed = {}
		for tag in q.tags:
			tags_for_feed[tag.tag_name] = tag.tag_koef

		new_tags = update_tags(url, tags_for_feed)
		'''
		
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