# Cloud Gateway Lab

## 1) Containerize a Simple Flask App
```bash
cd flask-app
docker build -t flask-cloud:latest .
```

## 2) Run the Docker Container Locally
```bash
docker run --rm -d --name flask-cloud -p 5000:5000 flask-cloud:latest
# verify
curl -i http://localhost:5000/hello
docker ps --filter name=flask-cloud
```

## 3) Simulate API Gateway with NGINX
**Option A: docker compose (easy)**
```bash
cd ..
docker compose up -d --build
curl -i http://localhost:8080/api/hello
```

**Option B: manual**
```bash
docker network create labnet
docker run --rm -d --name flask-cloud --network labnet -p 5000:5000 flask-cloud:latest
cd gateway
docker build -t nginx-gw:latest .
docker run --rm -d --name api-gw --network labnet -p 8080:80 nginx-gw:latest
curl -i http://localhost:8080/api/hello
```

## 4) Deploy a Serverless Function
**Local simulation**
```bash
cd ../lambda
python invoke_local.py
# or
python -c "import json;import handler;print(handler.handler({'queryStringParameters':{'name':'Cloud'}}, None))"
```

**(Optional) Real AWS Lambda quick path (zip & create)**
```bash
cd lambda
zip function.zip handler.py
# Create a role with AWSLambdaBasicExecutionRole first (outside scope here)
aws lambda create-function --function-name hello-cloud-lambda   --runtime python3.11 --handler handler.handler   --role arn:aws:iam::<ACCOUNT_ID>:role/<ROLE_NAME> --zip-file fileb://function.zip
aws lambda invoke --function-name hello-cloud-lambda out.json
cat out.json
```

## 5) Optional: Kubernetes (Minikube)
```bash
# Build the image inside Minikube's Docker
eval $(minikube docker-env)
cd ../flask-app && docker build -t flask-cloud:latest .

# Apply manifests
cd ../k8s
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# Get external URL
minikube service flask-cloud --url
```

## Screenshots to capture
- `docker ps` showing `flask-cloud` running.
- `curl -i http://localhost:8080/api/hello` showing a 200 with JSON payload.
- Local lambda execution output from `python lambda/invoke_local.py`.
- (Optional) `kubectl get pods,svc` showing the pod and service running.
