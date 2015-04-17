package lesson4;
//BlueJ Project: lesson4/book1
//Video: Working with the Book Text

import java.util.Scanner;
import java.io.File;

public class Book
{
 private String bookText;

 public Book(String fileName)
 {
     readBook(fileName);
 }

 /**
  * Calculates the number of characters (as in letters and
  * symbols, not people) in the book.
  * @return the number of letters and symbols in the book.
  */
 public int getNumCharacters()
 {
     return bookText.length();
 }

 /**
  * Finds the location of the first occurrence of "Mad hatter".
  */
 public int firstOccurrenceOfMadHatter()
 {
	 return bookText.indexOf("Mad hatter");
 }
 
 /**
  *  
  */
 public String getFirstSentence()
 {
	//The first sentence ends at first point.
	 int endOfSentence = bookText.indexOf(".");
	 //Will return a substring from the beginning of the text (0) to the first point.
	 return bookText.substring(0,endOfSentence+1);
 }
 
 /**
  *  
  */
 public String getSecondSentence()
 {
	 int beginningOfSentence = bookText.indexOf(".")+1;
	 int endOfSentence = bookText.indexOf(".", beginningOfSentence);
	 return bookText.substring(beginningOfSentence,endOfSentence+1);
 }
 
 /**
  *  
  */
 public int occurrencesOfAlice()
 {
	 int length = bookText.length();
	 int lengthWithoutAlice = bookText.replace("Alice", "").length();
	 return (length-lengthWithoutAlice)/5;
 }
 
 /**
  *  Finds the number of occurrences of word.
  */
 public int occurrencesOf(String word)
 {
	 int length = bookText.length();
	 int lengthWithoutAlice = bookText.replace(word, "").length();
	 return (length-lengthWithoutAlice)/word.length();
 }
 /**
  * A method to help read the book out of the file.
  * You don't have to read this unless you want to.
  * the "try" and "catch" are java's way of dealing with
  * runtime errors or "exceptions".
  */
 public void readBook(String fileName)
 {
     bookText = "";
     try
     {
         Scanner file = new Scanner(new File(fileName));
         while (file.hasNextLine())
         {
             String line = file.nextLine();
             bookText += line + "\n";
         }
         file.close();
     }
     catch (Exception e)
     {
         System.out.println(e);
     }
 }
}
