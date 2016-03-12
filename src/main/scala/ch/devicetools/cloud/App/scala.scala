package ch.devicetools.cloud.App

object App {

  def main(args : Array[String]) {
    println( "Hello World!" )

    val myList = List(1,2,3)
    println("Length of " + myList + " is: " + listLength(myList))
  }

  def listLength[A](list: List[A]) : Int = {
    list match {
      case Nil => 0
      case head :: tail => 1 + listLength(tail)
    }
  }
}
