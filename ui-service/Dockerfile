# Use an official Node.js image as the base image
FROM node:16 as build

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json /app
RUN npm install

# Copy the rest of the application code
COPY . /app

# Build the React app for production
RUN npm run build

# Use a lightweight web server (nginx) to serve the static files
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html

# Expose the port on which the app runs
EXPOSE 80

# Start the nginx server
CMD ["nginx", "-g", "daemon off;"]

