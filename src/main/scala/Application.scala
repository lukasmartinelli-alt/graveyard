package ch.devicetools

import akka.actor.ActorSystem
import akka.stream.ActorMaterializer
import akka.stream.scaladsl.{Sink, Source}
import com.softwaremill.react.kafka.KafkaMessages._
import com.softwaremill.react.kafka.{ConsumerProperties, ProducerMessage, ProducerProperties, ReactiveKafka}
import org.apache.kafka.common.serialization.{StringDeserializer, StringSerializer}
import org.reactivestreams.{Publisher, Subscriber}

object Main extends App {
    implicit val actorSystem = ActorSystem("ReactiveKafka")
    implicit val materializer = ActorMaterializer()

    System.out.println("Running app")
    val kafka = new ReactiveKafka()
    val publisher: Publisher[StringConsumerRecord] = kafka.consume(ConsumerProperties(
      bootstrapServers = sys.env("KAFKA_HOST"),
      topic = "lowercaseStrings",
      groupId = "groupName",
      valueDeserializer = new StringDeserializer()
    ))

    val subscriber: Subscriber[StringProducerMessage] = kafka.publish(ProducerProperties(
      bootstrapServers = sys.env("KAFKA_HOST"),
      topic = "uppercaseStrings",
      valueSerializer = new StringSerializer()
    ))

    Source.fromPublisher(publisher).map(m => {
      System.out.print(m.value())
      ProducerMessage(m.value().toUpperCase)
    })
      .to(Sink.fromSubscriber(subscriber)).run()
}

