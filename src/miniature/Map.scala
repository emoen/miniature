package miniature

object Map {

  def  main(args: Array[String]) {
    println(List("How","long","are","we?") map (s => s.length))
    println(List("How","capitalized","are","we?") map (s => s.toUpperCase))
    println(List("How","backwards","are","we?") map (s => s.reverse))
  }
}