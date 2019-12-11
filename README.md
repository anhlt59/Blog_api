# recipe-app-api
Recipe app api source code

# note
if docker-compose.yml or Dockerfile is changed,
	retyping "docker-compose build"
	and "docker-compose up -d" to run in deamon

docker-compose run app sh -c "command here"
docker-compose --rm > for services run once, avoid to linger on a system after it's ran

#######
from django.contrib.auth import get_user_model
> get_user_model get model is definded in settings.AUTH_USER_MODEL
