FROM nginx
COPY ["nginx.conf", "/etc/nginx/nginx.conf"]
RUN ["rm", "-rf", "/usr/share/nginx/html/*"]
COPY ["./dist", "/usr/share/nginx/html/"]
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]