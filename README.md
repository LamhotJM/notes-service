## Comment Micro-services
REST Commentary Services With Django Rest Framework Create the Python Virtual environment and clone the project and follow the below steps.

## Installing 
```
- django-admin startproject {$project-name}
- env\Scripts\activate.bat
- $ pip install -r requirements.txt
- python manage.py makemigrations commentengine (create migration file)
- python manage.py migrate

```
## Run Server
```sh
$ python manage.py runserver
```

## Unit Testing
````
python manage.py migrate
````

## Endpoint
* GetAll : http://localhost:8000/api/comments/?pn={int}&rpp={int}
* Post: http://localhost:8000/api/comments/

```json
 {
    "commentid": 4,
    "userid": "1",
    "loanid": "1",
    "comment": "comment lorem ipsum",
    "file_upload": "file upload",
    "context_id": 1,
    "context_scope": "contex lorem ipsum",
    "status": 1,
    "createdby": "createdby Jhon Doe",
    "createdfrom": "Created From",
    "modifiedby": "modifiedby Jhon Doe",
    "modifiedfrom": "Modifield From"
  }
```

* Get By ID : http://localhost:8000/api/comments/{comment_id}/
* Put : http://localhost:8000/api/comments/{comment_id}/

```json
 {
    "userid": "1",
    "loanid": "1",
    "comment": "comment lorem ipsum",
    "file_upload": "file upload",
    "context_id": 1,
    "context_scope": "contex lorem ipsum",
    "status": 1,
    "createdby": "createdby Jhon Doe",
    "createdfrom": "Created From",
    "modifiedby": "modifiedby Jhon Doe",
    "modifiedfrom": "Modifield From"
  }
```

* Delete: : http://localhost:8000/api/comments/comment_id/

## Responds

```json
{
  "status": "success",
  "cp": 1,
  "total": 3,
  "data": [
    {
      "commentid": 1,
      "userid": "1",
      "loanid": "1",
      "comment": "comment lorem ipsum",
      "file_upload": "file upload",
      "context_id": 1,
      "context_scope": "contex lorem ipsum",
      "status": 1,
      "createdby": "createdby Jhon Doe",
      "createdfrom": "Created From",
      "createddate": "2038-01-19T03:14:07",
      "modifiedby": "modifiedby Jhon Doe",
      "modifiedfrom": "Modifield From",
      "modifieddate": "2038-01-19T03:14:07"
    }
  ]
}
```

## Staging
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'comment_db',
        'USER': 'dev_pg_user',
        'PASSWORD': 'YmhhbG9vY2hvZA==',
        'HOST': 'postgres-dev.cib2hqsoqwhd.ap-southeast-1.rds.amazonaws.com',
        'PORT': 5432,
    }
}
```

## Local 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

```