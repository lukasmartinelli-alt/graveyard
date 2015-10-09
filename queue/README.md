## Event Queue

Implementation of an event queue.
I want to try out [nats.io](http://nats.io/) for this project.

We can run the [official Docker image](https://hub.docker.com/_/nats/).

```
docker run -d --name nats -p 4222:4222 nats
```

Clients can connect with settings.

User: `ruser`
Password: `T0pS3cr3t`
