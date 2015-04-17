import java.util.Scanner;

public class RedderTest
{
   public static void main(String[] args) throws InterruptedException
   {
      Picture pic = new Picture();
      pic.load("queen-mary.png");
      pic.draw();
      Scanner in = new Scanner(System.in);
      System.out.print("How much read do you want to add (0-255)? ");
      int redInc = in.nextInt();
      for (int i = 0; i < pic.pixels(); i++)
      {
         Color c = pic.getColorAt(i);
         c.redden(redInc);
         pic.setColorAt(i, c);
      }
      in.close();
   }
}
