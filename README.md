# smartfeed

## App

### Project setup

```bash
cd App; npm install
```

#### Compiles and hot-reloads for development

```bash
cd App; npm run serve
```

#### Compiles and minifies for production

```bash
cd App; npm run build
```

#### Run your tests

```bash
cd App; npm run test
```

#### Lints and fixes files

```bash
cd App; npm run lint
```

#### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).

## Back setup

### Installing packeges

```bash
pip install -r requirements.txt
```

### Applying django migrations

```bash
cd Back; python manage.py migrate
```

### Run server

```bash
python manage.py runserver
```

Server will start at <http://127.0.0.1:8000.> API:

#### 1. init_user/

Method: POST
Waiting for JSON with user nickname and list if his tags. Call it, when you need to add new user or change existing user tags

#### 2. get_news/

Method: POST
Waiting for JSON with user nickname. Call it, when you need to get news feed

#### 3. news_click/

Method: POST
Waiting for JSON with user nickname and clicked news url. Call it, when user click on any news

#### 4. get_user_tags/

Waiting for JSON with user nickname. Call it, when you need to render all user tags