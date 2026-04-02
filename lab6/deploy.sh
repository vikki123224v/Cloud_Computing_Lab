PORT=8080
echo "Building Docker image..."
docker build -t myapp:latest .
echo "Stopping old containers..."
docker stop myapp || true
docker rm myapp || true
echo "Runnung new container on port $PORT..."
docker run -d --name myapp -p $PORT:8080 myapp:latest
echo "App deployed!"
echo "Use Killercoda Traffic tab port $PORT"

