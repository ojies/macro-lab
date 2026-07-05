# macro-lab dashboard — Next.js frontend
FROM node:20-slim

WORKDIR /app

# install deps first (cached layer)
COPY package.json package-lock.json ./
RUN npm ci

COPY . .

# API_URL (→ the backend service) is read by next.config at build + runtime;
# docker-compose overrides it to http://backend:8000
ENV API_URL=http://backend:8000
RUN npm run build

EXPOSE 3000
CMD ["npm", "start"]
