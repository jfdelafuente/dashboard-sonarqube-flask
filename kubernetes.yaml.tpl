apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-cloudbuild
  labels:
    app: hello-cloudbuild
spec:
  replicas: 1
  selector:
    matchLabels:
      app: hello-cloudbuild
  template:
    metadata:
      labels:
        app: hello-cloudbuild
    spec:
      containers:
      - name: dashboard-sonarqube-flask
        image: REGION-docker.pkg.dev/GOOGLE_CLOUD_PROJECT/my-repository/dashboard-sonarqube-flask:COMMIT_SHA
        ports:
        - containerPort: 5005
---
kind: Service
apiVersion: v1
metadata:
  name: hello-cloudbuild
spec:
  selector:
    app: hello-cloudbuild
  ports:
  - protocol: TCP
    port: 80
    targetPort: 5005
  type: LoadBalancer