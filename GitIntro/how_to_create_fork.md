## Як створити fork

Офіційна документація, як створити fork  
https://help.github.com/en/github/getting-started-with-github/fork-a-repo

Ссилка на основний репозиторій в якому буде код з лекцій та практики
https://github.com/Vasilov345/alfred_pennyworth

## Як зв`язати свій fork з основним репозиторієм ?

Перейдіть в директорію свого проекту
```
git remote -v
```
На виході буде ссилка на ваш репозиторій
```
origin https://github.com/{github_nickname}/alfred_pennyworth (fetch)  
origin https://github.com/{github_nickname}/alfred_pennyworth (push)
```

```
git remote add upstream https://github.com/Vasilov345/alfred_pennyworth.git
git remote -v
```

На виході буде дві ссилки на ваш fork(origin), та основний репозиторій (upstream)

```
origin https://github.com/{github_nickname}/alfred_pennyworth.git (fetch)
origin https://github.com/{github_nickname}/alfred_pennyworth.git (push)
upstream https://github.com/Vasilov345/alfred_pennyworth.git (fetch)
upstream https://github.com/Vasilov345/alfred_pennyworth.git (push)
```

## Як стягнути зміни з основного репозиторію у fork репозиторій ?

1. Перевірте ваш поточний стан проекту
```
git status 
```
Результат команди має бути приблизно наступним
```
On branch master
nothing to commit, working tree clean
```

2. Оновляєте зміни зі свого fork
3. Стягуєте зміни з основного репозиторію

```
git pull origin master 
git pull upstream master
```
