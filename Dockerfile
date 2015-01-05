FROM ubuntu:trusty
MAINTAINER Lukas Martinelli <me@lukasmartinelli.ch>

# install dependencies for building facebook libraries
RUN apt-get update && apt-get install -y \
    g++ \
    gdc \
    automake \
    autoconf \
    autoconf-archive \
    libtool \
    libboost-all-dev \
    libevent-dev \
    libdouble-conversion-dev \
    libgoogle-glog-dev \
    libgflags-dev \
    liblz4-dev \
    liblzma-dev \
    libsnappy-dev \
    make \
    zlib1g-dev \
    binutils-dev \
    libjemalloc-dev \
    libssl-dev \
    libiberty-dev \
    scons \
    git

# build and install folly
RUN git clone https://github.com/facebook/folly
WORKDIR folly/folly
RUN autoreconf -ivf && \
    ./configure && \
    make
RUN apt-get install -y wget unzip
RUN wget https://googletest.googlecode.com/files/gtest-1.6.0.zip && \
    unzip gtest-1.6.0.zip -d test
RUN make check && \
    make install

# build and install double-conversion
RUN git clone https://github.com/floitsch/double-conversion.git
WORKDIR /double-conversion
RUN scons install

# build and install flint
RUN git clone https://github.com/facebook/flint
WORKDIR /flint
RUN curl -0 https://googletest.googlecode.com/files/gtest-1.6.0.zip && \
    unzip gtest-1.6.0.zip -d cxx
ENV LDFLAGS="-L../double-conversion" CPPFLAGS="-I../double-conversion/src"
RUN autoreconf --install && \
    configure ... && \
    make
