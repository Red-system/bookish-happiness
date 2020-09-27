# Getting started

## clone the project

```
git clone https://github.com/Red-system/bookish-happiness.git
```

## create a virtual env

* virtualenv and python are required

```
py -m venv vfrigo
```
* ativate virtualenv in the termial session

```
./frigo/scripts/activate
```

## install dependencies 

```
pip install -r requirements.tkt
```

## run the project

```
./main.py
```

## make migrations

```
alembic revision --autogenerate -m "Added account table"
```

## migrate (apply the change to the database)

```
alembic upgrade head
```

## how to use git

```
# pull the remote changes to local
git pull 
# add all the changes to be committed
git add .
#add changes with reviews of changes 
git add -p 
# commit the changes with a description message
git commit -m "my message" 
# push the commits to master
git push

#se positionner sur la branche desirée
git checkout branche_name
#merge two branches
git merge autre_branche_name


# list branch
git branch -l
# create new branch
git checkout -b branchname
# push a new branch to remote repo (github)
git push -u origin develop
# switch branch on local
git checkout develop
```
