ENV_FILE = .env

ifeq ($(shell test -e $(ENV_FILE) && echo true), true)
    include $(ENV_FILE)
		export
endif

APP_NAME = ${PROJECT}-${ENV}-${STAGE}

build:
	sam build --region ${REGION} --profile ${PROFILE} --parameter-overrides Project=${PROJECT} Env=${ENV} Stage=${STAGE}

deploy:
	sam deploy \
		--stack-name ${APP_NAME} \
		--s3-bucket "${APP_NAME}-bucket" \
		--region ${REGION} \
		--profile ${PROFILE} \
		--parameter-overrides Project=${PROJECT} Env=${ENV} Stage=${STAGE} \
		--capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND
