#  приложение на Django REST
1. Приложение habits с различными привычками



## Приложение имеет следующий функционал:

* Пользователь — создатель привычки.
* Место — место, в котором необходимо выполнять привычку.
* Время — время, когда необходимо выполнять привычку.
* Действие — действие, которое представляет собой привычка.
* Признак приятной привычки — привычка, которую можно привязать к выполнению полезной привычки.
* Связанная привычка — привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных.
* Периодичность (по умолчанию ежедневная) — периодичность выполнения привычки для напоминания в днях.
* Вознаграждение — чем пользователь должен себя вознаградить после выполнения.
* Время на выполнение — время, которое предположительно потратит пользователь на выполнение привычки.
* Признак публичности — привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки.



### Установка
+ клонировать репозиторий [Github] https://github.com/SadhuT1000/DRF_Course/pull/1

<h1 align="center">Docker в проекте</h1> 

<h3 align="center">Для быстрого старта:</h3>
<p align="center">Скачайте проект с удаленного репозитория</p>
<p align="center">Настройте зависимости в файле .env</p>
<p align="center">Введите в терминал команду: docker-compose up -d --build</p>






### 1. Requirements  
For a successful deployment you will need:  
  - Remote server with Docker installed.  
  -  Docker Hub account.  
  - Access to the repository on GitHub.

### 2. Setting up a remote server 
1. #### System update
    ```bash
    sudo apt update
    sudo apt upgrade
    ```
2. #### Installing `docker` and `docker-compose`
    ```bash
    sudo apt update && sudo apt install -y docker.io docker-compose
    sudo systemctl enable docker
    sudo usermod -aG docker $USER && newgrp docker
    ```
3. #### Firewall setup
4. ##### **Activate firewall**
    ```bash
    # check the firewall status
    sudo ufw status

    # If the firewall is disabled, enable it
    sudo ufw enable
    ```
5. ##### **Open the necessary ports**
    ```bash
    # http port:
    sudo ufw allow 80/tcp
		
    # https port:
    sudo ufw allow 443/tcp
		
    # ssh port:
    sudo ufw allow 22/tcp
    ```
6. ##### **Cloning a repository:**
    Fill in values. Here's an example: 
    ```bash
    git clone https://github.com/goqwertys/habit-tracker.git /var/www/habit-tracker
    cd /var/www/habit-tracker
    ```
    Fill in values. Here's an example: 
    ```bash
    git clone https://github.com/goqwertys/habit-tracker.git /var/www/habit-tracker
    cd /var/www/habit-tracker
    ```
    Fill in values. Here's an example: 
    ```
    # Django secret key
    SECRET_KEY=django-insecure-12345!abcde67890!@#qwerty
		
    # DB settings
    POSTGRES_DB=habit_tracker_db
    POSTGRES_USER=habit_user
    POSTGRES_PASSWORD=secure_password123
    POSTGRES_HOST=localhost
    POSTGRES_PORT=5432
		
    # Allowed hosts
    ALLOWED_HOSTS=localhost,127.0.0.1,example.com
		
    # CELERY
    CELERY_BROKER_URL=redis://localhost:6379/0
    CELERY_RESULT_BACKEND=redis://localhost:6379/0
		
    # TELEGRAM API
    TG_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz_123456789
    ```
7. ##### **Launch in production:**
    ```bash
    git clone https://github.com/goqwertys/habit-tracker.git /var/www/habit-tracker
    cd /var/www/habit-tracker
    ```
8. ##### **Important:**
9. Nginx will be available on port 80
10. Automatic static and migration build
11. Celery workers/beat запустятся автоматически

## Setting up CI/CD
1. ### **Fork or Clone the Repository**
	-	Fork this repository to your own GitHub account if you plan to contribute or run workflows that require secret keys.
	-	Alternatively, clone the repository directly to your local machine:
		```bash
		git clone https://github.com/username/repository-name.git
		cd repository-name
		```
2. ### **Set Up data into the secrets:**
	1. Go to your forked repository on GitHub.
	2. Navigate to **Settings > Secrets and variables > Actions**.
	3. Add the required secrets, such as
		* `DOTENV` - contents of .`env` (Fill in according to the .env.sample)
		* `DOCKER_HUB_USERNAME` - [Docker Hub](https://hub.docker.com/) login
		* `DOCKER_ACCESS_TOKEN` - Docker Hub token
		* `SSH_KEY` - server private SSH key
		* `SSH_USER` - server user
		* `SERVER_IP` - IP of virtual machine
3. ### Workflow:
	* Automatically launched on push/pull request
	* Steps:
	✅ lint→ ✅ tests → ✅ build → 🚀 deploy
## Local run (development)
1.  #### Make sure you have filled in the data in `.env`
2. #### Build and Run:
	```bash
	docker-compose -f docker-compose.dev.yml up --build
	```
3. #### Creating a superuser
	```bash
	docker-compose -f docker-compose.dev.yml exec web python manage.py createsuperuser
	```
4. #### Ports:
	- Django:  `http://localhost:8000`
	- PostgreSQL: `5432`
	- Redis:  `6379`

## Настройка CI/CD
... (остальная часть раздела с настройкой CI/CD)

## Доступ к развернутому приложению

После успешного завершения процесса развертывания, ваше приложение будет доступно по следующему адресу:

-  Starting development server at http://51.250.114.52:8000/



## Emergency Commands (Server)

```bash
    # Просмотр логов
    docker-compose -f docker-compose.prod.yml logs -f
    
    # Пересборка контейнеров
    docker-compose -f docker-compose.prod.yml up -d --build --force-recreate
    
    # Остановка
    docker-compose -f docker-compose.prod.yml down -v
```
*** 
