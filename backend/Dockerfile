FROM node
RUN mkdir /app
WORKDIR /app
RUN npm install -g nodemon
COPY ./package.json ./
RUN npm install

# During Development
CMD npm run dev

# For production
# CMD npm run start