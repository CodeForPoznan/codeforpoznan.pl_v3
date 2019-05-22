.DEFAULT_GOAL:=help

help:   ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

start:  ## Start the environment in the background
	docker-compose up -d

logs:   ## Display logs from containers
	docker-compose logs

stop:   ## Stop the environment
	docker-compose stop

bash:   ## Go to the backend container
	docker exec -ti codeforpoznanpl_v3_backend_1 bash
	
psql:   ## Go to the db and make SQL queries
        docker exec -ti codeforpoznanpl_v3_db_1 psql -U cfp_v3
