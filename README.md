# SmartFeed
News aggregator which modifies user's newsfeed based on his interests.  
Currently, this version only supports Russian news (sorry).  
More information about project such as: ER diagram, Use Case diagram and small description is located in docs directory (yep, it's also in Russian, sorry).  
Project was initially developed in private GitLab repository with boards according to Agile manifesto, so most commits refer to an unknown issues.  
**P.S.** You actually can make a little tweak to backend to make it work with other languages. 
Anyway, if you'd like to contribute something or have any questions you can PM me or leave a merge request or add an issue, I'll gladly help.

## To Run Them All

```bash
brew services start mongodb-community@4.0
```

```bash
cd Back; python manage.py runserver
```

```bash
cd App; npm run serve
```

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

## Mongo install on macOS

```bash
brew tap mongodb/brew
brew install mongodb-community@4.0
```

### Run mongo

```bash
brew services start mongodb-community@4.0
```

If this command ended successfully, mongodb will run on localhost and will listen default port. That what back expected for. If you want to check all is fine or not - run "mongo" command.

## Mongo install on other platforms

See [Official installation guide](https://docs.mongodb.com/manual/administration/install-community/). Installations are to different for different platforms. Ass a result you need to run mongo with default settings.

## Back setup

### Installing packeges

```bash
pip install -r requirements.txt
```

### Before applying django migrations and server running

Note that you need to install and run mongo before next steps. See prev chapter for more details.

### Applying django migrations

```bash
cd Back
python manage.py makemigrations news
python manage.py migrate news
```

### Run server

```bash
cd Back; python manage.py runserver
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
