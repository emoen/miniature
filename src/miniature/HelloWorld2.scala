package miniature

object HelloWorld2 {
  def main(args:Array[String]):Unit = {
    println(args(0))
    var greeting = ""
    val range = 0.until(args.length) //val -> var with final
    for (i <- range) {
    //for (i <- 0 until args.length) {
      greeting += (args(i) + " ")
    }
    var greeting1:String = ""
    args.foreach { arg =>
    	greeting1 += (arg + " ")
    }
    if (args.length > 0) greeting = greeting.substring(0, greeting.length - 1)
 
    println(greeting)
    println(greeting1)
  }
}