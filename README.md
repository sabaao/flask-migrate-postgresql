# flask-postgresql

# Run Postgresql docker in local
```
docker run --name mypostgres -e POSTGRES_PASSWORD=postgres -d postgres
```

Set password is postgres


# How to add new model
Add new model or modfiy modify model in `models` folder.
And use command to generate migrate script.
```
flask db migrate -m "your comment"
```
# deploy database
```
flask db upgrade
```
And it will create table in postgres.

# How to insert data
```
flask db revision
```
Use this command generate a new revision file in migrations/versions.
Then you can write insert/update python in this file.
You can see migrations/version/29c9ec063e2c_add_data.py.
# Reference
https://blog.miguelgrinberg.com/post/flask-migrate-alembic-database-migration-wrapper-for-flask