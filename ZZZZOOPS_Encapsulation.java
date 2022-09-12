import java.io.*;
import java.util.*;

// Encapsulation by getter and setter methods
class Encapsulation{

  private String name;
  private int age;

  Encapsulation(String name,int age){
    this.name=name;
    this.age=age;
  }

  public String getname(){
    return name;
  }

  public int getage(){
    return age;
  }

  public void setname(String name){
    this.name = name;
  }
  public void setAge(int age){
    this.age = age;
  }

}
class demo1 {

  // Main driver method
  public static void main(String[] args)
  {

      Scanner read = new Scanner(System.in);
    
      try {
        System.setOut(new PrintStream(
          new FileOutputStream("out.txt")));

        read = new Scanner(new File("in.txt"));
      } catch (Exception e){}

    // Code Here...
  Encapsulation obj = new Encapsulation("Ishan",23);

  System.out.println(obj.getname());

  obj.setname("Harch");

  System.out.println(obj.getname()+" "+obj.getage());


  } //main end

} //class end
