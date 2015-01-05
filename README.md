# docker-flint

An Ubuntu based image that builds [flint](https://code.facebook.com/posts/729709347050548/under-the-hood-building-and-open-sourcing-flint/) and its dependencies.

- [facebook/folly](https://github.com/facebook/folly)
- [floitsch/double-conversion](https://github.com/floitsch/double-conversion)
- [facebook/flint](https://github.com/facebook/flint)

## Run

Pull the docker image.

```
docker pull lukasmartinelli/docker-flint
```

Run flint on code of yours by mounting it into the `/root` folder of the docker
container.

```
sudo docker run -v /path/to/project/src:/root docker-flint /root
```

## Build

```
sudo docker build -t docker-flint .
```

