FROM hseeberger/scala-sbt

# Install and cache dependencies
WORKDIR /usr/src/app
COPY build.sbt /usr/src/app/
COPY project/plugins.sbt project/build.properties /usr/src/app/project/
RUN sbt compile

# Compile application
COPY src /usr/src/app/src
RUN sbt compile

CMD ["sbt", "run"]
