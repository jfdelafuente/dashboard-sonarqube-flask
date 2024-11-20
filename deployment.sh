
# Create a Google Artifact Registry called my-repository in the specified region
gcloud artifacts repositories create my-repository \
  --repository-format=docker \
  --location=$REGION

# Create a GKE Standard cluster called hello-cluster
# It must be zonal, with 3 nodes
# Min nodes=2, max nodes=6, and cluster autoscaler enabled
# Release channel=Regular, and with cluster version specified
gcloud container clusters create dashboard-sonar-cluster \
  --zone $ZONE \
  --num-nodes=3 --min-nodes=2 --max-nodes=6 --enable-autoscaling \
  --release-channel=regular \

# We can verify it
gcloud container clusters list

# we need to obtain the credentials for our cluster
gcloud container clusters get-credentials dashboard-sonar-cluster --zone $ZONE


kubectl config current-context


kubectl create deployment dashboard-sonar-app \
    --image=$REGION-docker.pkg.dev/$PROJECT_ID/my-repository/dashboard-sonarqube-flask:579eae0

kubectl expose deployment dashboard-sonar-app \
    --name=dashboar-sonar-app-service --type=LoadBalancer --port 80 --target-port 5005