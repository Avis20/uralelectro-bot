BASE_DOCKER_COMPOSE = -f docker/dev.docker-compose.yml
TEST_DOCKER_COMPOSE = -f docker/docker-compose.override.test.yml -f docker/docker-compose.test.yml
ENV_FILE =  ./.docker.env
LOCAL_ENV_FILE =  ./.env

.PHONY: create_env
create_env: ## Just touching env files
	touch $(ENV_FILE)
	touch $(LOCAL_ENV_FILE)

.PHONY: up
up: create_env ## up services
# make up service=uralelectro-bot-backend
	@docker compose --env-file $(ENV_FILE) $(BASE_DOCKER_COMPOSE) up $(service) -d

.PHONY: logs
logs: ## tail logs services
# make logs service=uralelectro-bot-backend
	@docker compose --env-file $(ENV_FILE) $(BASE_DOCKER_COMPOSE) logs $(service) -f

.PHONY: down
down: ## down services
	@docker compose --env-file $(ENV_FILE) $(BASE_DOCKER_COMPOSE) down

.PHONY: build
build: create_env ## build services
# make build service=uralelectro-bot-backend
	@docker compose --env-file $(ENV_FILE) $(BASE_DOCKER_COMPOSE) build $(service)

.PHONY: restart
restart: down up ## restart services

.PHONY: uninstall
uninstall: create_env ## uninstall all services
	@docker compose --env-file $(ENV_FILE) $(BASE_DOCKER_COMPOSE) down --remove-orphans --volumes

###############
### tests start
###############

.PHONY: run_test
run_test: ## run once all tests
# make up service=uralelectro-bot-backend
	@docker compose --env-file $(ENV_FILE) $(TEST_DOCKER_COMPOSE) run --rm test-uralelectro-bot-migrate-db
	@docker compose --env-file $(ENV_FILE) $(TEST_DOCKER_COMPOSE) down

.PHONY: up_test
up_test: ## up test services
	@docker compose $(TEST_DOCKER_COMPOSE) up -d

.PHONY: build_test
build_test: ## build test services
	@docker compose --env-file $(ENV_FILE) $(TEST_DOCKER_COMPOSE) build

.PHONY: log_test
log_test: ## log test services
	@docker compose $(TEST_DOCKER_COMPOSE) logs $(service) -f

.PHONY: lint
lint: ## run linters
	poetry run pre-commit run --all-files

#############
### tests end
#############

.PHONY: help
help: ## Help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
