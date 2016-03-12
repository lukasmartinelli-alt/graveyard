FROM hseeberger/scala-sbt

# Install and cache dependencies
WORKDIR /usr/src/app/
COPY build.sbt /usr/src/app/
COPY project/plugins.sbt /usr/src/app/project/
RUN sbt compile

# Compile application
COPY src project /usr/src/app/
RUN sbt compile
CMD ["sbt", "one-jar"]
