# Authenticate
gcloud auth list
gcloud config list project

# Some useful initial setup
export PROJECT_ID=$(gcloud config get-value project)
export PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format='value(projectNumber)')
export REGION=us-central1
export ZONE=us-central1-a

echo 'Proyecto :  $PROJECT_ID    en la zona $REGION'

# If you're set to the wrong project
gcloud config set project $PROJECT_ID
gcloud auth application-defaul login
gcloud auth application-default set-quota-project $PROJECT_ID
gcloud config set compute/region $REGION

# enable APIs
gcloud services enable container.googleapis.com \
    cloudbuild.googleapis.com

# Create a Google Artifact Registry called my-repository in the specified region
# gcloud artifacts repositories create my-repository \
#   --repository-format=docker \
#   --location=$REGION

# Create a GKE Standard cluster called hello-cluster
# It must be zonal, with 3 nodes
# Min nodes=2, max nodes=6, and cluster autoscaler enabled
# Release channel=Regular, and with cluster version specified
# gcloud container clusters create hello-cluster \
#   --zone $ZONE \
#   --num-nodes=3 --min-nodes=2 --max-nodes=6 --enable-autoscaling \
#   --release-channel=regular \

# We can verify it
# gcloud container clusters list

# we need to obtain the credentials for our cluster
# gcloud container clusters get-credentials hello-cluster --zone $ZONE