FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install --legacy-peer-deps
COPY . .
ARG REACT_APP_API_URL=http://localhost:5000/api
ENV REACT_APP_API_URL=${REACT_APP_API_URL}
RUN npm run build

FROM node:20-alpine
RUN npm install -g serve
COPY --from=build /app/build /app/build
EXPOSE 3000
CMD ["serve", "-s", "/app/build", "-l", "3000"]