FROM node:12.16.3
ENV NODE_ENV=production
WORKDIR /app
COPY ["package.json", "package-lock.json*","webpack.config.json", "./"]
COPY ["./frontend", .]