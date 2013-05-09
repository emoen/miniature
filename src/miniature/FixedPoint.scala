package miniature

object FixedPoint {
  def fact(n:Int):Int = {
    if (n == 0) 
      1 
    else 
      fact( n - 1) * n
  }
  
  def  main(args: Array[String]) {
    println(fact(10))
  }
}