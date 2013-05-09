package miniature

object Currying {
	def addWithoutCurry(x:Int, y:Int) = x + y
		
	def add(x:Int) = (y:Int) => x + y

	def  main(args: Array[String]) {
	  println(addWithoutCurry(1,3))
	  println(add(7)(3))
	}
}