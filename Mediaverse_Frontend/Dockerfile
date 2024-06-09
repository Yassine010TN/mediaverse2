# Use an official Node.js runtime as a parent image
FROM node:18

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json into the container
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the current directory contents into the container
COPY . .

# Build the app for production
RUN npm run build

# Install serve to run the build
RUN npm install -g serve

# Serve the build
CMD ["serve", "-s", "dist", "-l", "5173"]

# Expose port 5173
EXPOSE 5173
