version ?= "development"
login_version ?= "development"
values ?=
image_repo ?= "ccr.ccs.tencentyun.com/bk.io"
chart_repo ?=
namespace ?= "bk-user"
test_release_name ?= "bk-user-test"

generate-release-md:
	rm docs/changelogs/*.md || true
	cd src/saas/ && mkdir -p changelogs/ && poetry run python manage.py generate_release_md
	mv src/saas/changelogs docs/
	mv src/saas/release.md docs/

link:
	ln -s ${PWD}/src/bkuser_global src/api || true
	ln -s ${PWD}/src/bkuser_global src/saas || true
	ln -s ${PWD}/src/bkuser_global src/login || true
	ln -s ${PWD}/src/sdk/bkuser_sdk src/saas || true

generate-sdk:
	cd src/ && swagger-codegen generate -i http://localhost:8004/redoc/\?format\=openapi -l python -o sdk/ -c config.json

build-api:
	docker build -f src/api/Dockerfile . -t ${image_repo}/bk-user-api:${version}

build-saas:
	docker build -f src/saas/Dockerfile . -t ${image_repo}/bk-user-saas:${version}

build-login:
	docker build -f src/login/Dockerfile . -t ${image_repo}/bk-login:${login_version}

build-all: build-api build-saas build-login

push:
	docker push ${image_repo}/bk-user-api:${version}
	docker push ${image_repo}/bk-user-saas:${version}
	docker push ${image_repo}/bk-login:${login_version}

helm-sync:
	mkdir -p deploy/helm/api/templates/
	mkdir -p deploy/helm/saas/templates/
	mkdir -p deploy/helm/login/templates/
	ln -s ${PWD}/deploy/helm/chartty/* deploy/helm/api/templates/ || true
	ln -s ${PWD}/deploy/helm/chartty/* deploy/helm/saas/templates/ || true
	ln -s ${PWD}/deploy/helm/chartty/* deploy/helm/login/templates/ || true

	ln -s ${PWD}/deploy/helm/chartty/c_*.tpl deploy/helm/bk-user-stack/templates/ || true

helm-refresh: helm-sync
	cd deploy/helm && helm dependency update bk-user-stack --skip-refresh

helm-debug: helm-refresh
	cd deploy/helm && helm install ${test_release_name} bk-user-stack --debug --dry-run -f local_values.yaml

helm-install: helm-refresh
	cd deploy/helm && helm upgrade --install ${test_release_name} bk-user-stack -n ${namespace} -f local_values.yaml

helm-uninstall:
	helm uninstall ${test_release_name} -n ${namespace} || true
	kubectl delete deploy,sts,cronjob,pod,svc,ingress,secret,cm,sa,pvc -n ${namespace} -l app.kubernetes.io/instance=${test_release_name}

helm-package: helm-refresh
	cd deploy/helm && helm package bk-user-stack -d dist/

helm-publish: deploy/helm/dist/*.tgz
	for f in $^; do \
		curl -kL -X POST -F chart=@$${f} -u ${credentials} ${chart_repo}; \
	done