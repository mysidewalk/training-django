## Make Migrations
# Every time we create/update/delete a model within the Django framework we will need create a 
# new database migration that helps inform the database how to make the changes. We can do this
# quite simply by making our desired additions, changes, or deletions to any model in any our our
# Django apps. Following those changes we can create a new migration by using the following command
# while ssh'ed into your vagrant machine:

cd /vagrant/mm2 && python manage.py makemigrations

# We can optionally specify a Django app for this command to only make migrations for that app:

cd /vagrant/mm2 && python manage.py makemigrations library

# The result of this command is the creation of a new directory in our library app called
# "migrations". The "migrations" directory will hold each one of our migrations, as well as Django,
# storing each one of these in a specific table.

# Every time you create a new migration, the app generates the needed dependencies and places them
# at the top of the migrations file. A general rule of thumb for us at MindMixer is that until you 
# are ready to merge your branch that you created migrations on to commit your migrations, all other
# commits can and should be made without committing that migrations file to prevent multiple
# migrations from needing to be made, this allows us to make some updates to a model/migration
# during development without having 5 migrations to support 1 added model.



## Running Migrations
# After generating a migration you can run it by using one of the following syntaxes:

# The following command will run all migrations that have not been run but are generated
cd /vagrant/mm2 && python manage.py migrate

# The following command will run only migrations for the library app
cd /vagrant/mm2 && python manage.py migrate library

# After you have run the migrate command without errors you should be able to open pgAdmin and see
# your new tables as well as create and populate content via the interactive shell.



## Running a specific migration
# You can choose to run a specific migration when using the "migrate" command by simply including 
# the numeric prefix to the migration. For example if you updated the library checkout model to 
# include a returned at date time field you could target the second migration as 0002 or just 2. 
# Each migration after that will be incremented similarly with the first one be title 0001_initial.
