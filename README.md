#DEV_DJANGO
1. I make the django project with tutorial: 'https://www.youtube.com/playlist?list=PL3U271IN44UpfqNWsKQDGzhTimShPaXXy'.
2. I make the app yt_ideas and did migration with it.
3. Some commends:
    django-admin startproject {name_project}
    python manage.py runserver
    python manage.py startapp {name_app}
4. To add application to project we needed to add line in
    settings.py in line "INSTALLED_APPS = [...'name.apps.NameConfig'...]"
5. And naxt step is to do migration with commands:
    python manage.py makemigrations {name_app},
    See the migration in terminal for app.
6. After makemigrations have to use commands:
    python manage.py migrate
    - Run python manage.py makemigrations to create migrations for those changes
    - Run python manage.py migrate to apply those changes to the database.

#DEV_DOCKER
1. Listing avaible container 'docker ps'.
2. To enter conteiner 'docker exec -it {id} bash'.
3. To rebild container 'docer-compose build {name_container}'.
4. Start project containers 'docker-compose up'.

#DEV_POSTGRESQP
1. To change the database from sqllite3 to postgresql we have to
    change it in settings.py file and change in postgrasql lines
    for our db, user and password.

#DEV_GIT
1. Add application to github
2. Create new repository on github
3. Use commends:
    git init 
    git status
    git add .
    git status
    git commit "name_commit"
    git branch -M main
    git remote add origin {https://gtihub...}
    git push
    git push -u origin main
4. Remote pycache and add new commit:
    git rm -r .\ideas\__pycache__
    git rm -r .\youtube_ideas\__pycache__
    git status
    git commit -m "remove __pycache__"