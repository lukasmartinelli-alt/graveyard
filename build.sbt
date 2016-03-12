import com.github.retronym.SbtOneJar._

oneJarSettings

name := "scala-jcloud"

version := "1.0"

scalaVersion := "2.11.8"

organization := "ch.devicetools"

libraryDependencies += "com.softwaremill.reactivekafka" %% "reactive-kafka-core" % "0.10.0"

libraryDependencies += "com.typesafe.akka" %% "akka-actor" % "2.4.1"