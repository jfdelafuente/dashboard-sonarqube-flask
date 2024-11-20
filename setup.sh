# Authenticate
gcloud auth list
# gcloud config list project

# Some useful initial setup
export PROJECT_ID=$(gcloud config get-value project)
export PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format='value(projectNumber)')
export REGION=europe-southwest1
export ZONE=europe-southwest1-a

# If you're set to the wrong project
gcloud config set project $PROJECT_ID
# gcloud auth application-defaul login
# gcloud auth application-default set-quota-project $PROJECT_ID
gcloud config set compute/region $REGION

# enable APIs
gcloud services enable container.googleapis.com \
    cloudbuild.googleapis.com

echo "Environment variables configured:"
echo PROJECT_ID="$PROJECT_ID"
echo REGION="$REGION