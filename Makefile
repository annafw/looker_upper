GCLOUD_PROJECT:=$(shell gcloud config list project --format="value(core.project)")

.PHONY: all
all: deploy

.PHONY: create-cluster
create-cluster:
	gcloud container clusters create looker_upper \
		--scope "https://www.googleapis.com/auth/userinfo.email","cloud-platform"

.PHONY: create-bucket
create-bucket:
	gsutil mb gs://$(GCLOUD_PROJECT)
    gsutil defacl set public-read gs://$(GCLOUD_PROJECT)

.PHONY: build
build:
	docker build -t gcr.io/$(GCLOUD_PROJECT)/looker_upper .

.PHONY: push
push: build
	gcloud docker push gcr.io/$(GCLOUD_PROJECT)/looker_upper

.PHONY: template
template:
	sed -i ".tmpl" "s/\$$GCLOUD_PROJECT/$(GCLOUD_PROJECT)/g" looker_upper.yaml

.PHONY: deploy
deploy: push template
	kubectl create -f looker_upper.yaml

.PHONY: update
update:
	kubectl rolling-update looker_upper --image=gcr.io/${GCLOUD_PROJECT}/looker_upper

.PHONY: delete
delete:
	kubectl delete rc looker_upper
	kubectl delete service looker_upper
