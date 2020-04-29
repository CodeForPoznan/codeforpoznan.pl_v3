.DEFAULT_GOAL:=help

help: ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

start: ## Start the environment in the background
	docker-compose up -d

logs: ## Display logs from containers
	docker-compose logs --tail 100 -f

stop: ## Stop the environment
	docker-compose stop

bash: ## Go to the backend container
	docker-compose exec backend bash

psql: ## Go to the db and make SQL queries
	docker-compose exec db psql -U cfp_v3

populate_database: ## Populate database with fake data
	docker-compose exec backend flask populate-database

rebuild: ## Rebuild docker images
	docker-compose rm --force
	docker-compose build --no-cache

test: ## Run unittests
	docker-compose exec backend pytest

black: ## Run black
	docker-compose exec backend black .

black-check: ## Check black
	docker-compose exec backend black --check .

prettier: ## Run prettier
	docker-compose exec frontend yarn lint:fix

prettier-check: ## Check prettier
	docker-compose exec frontend yarn lint

lint: black prettier

lint-check: black-check prettier-check

code-cov: ## Run pytest with code coverage
	docker-compose exec backend pytest --cov=backend

cov-report: ## Generate coverage raport in HTML
	docker-compose exec backend pytest --cov=backend --cov-report=html

remove-tokens: ## Remove expired tokens from db
	docker-compose exec backend flask remove-expired-tokens
