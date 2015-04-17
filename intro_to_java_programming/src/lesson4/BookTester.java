package lesson4;
public class BookTester
{
    public static void main(String[] args)
    {
        Book alice = new Book("aliceInWonderland.txt");

        System.out.println(alice.getNumCharacters());
        System.out.println("Expected: 144331");
        //How many times does the MadHatter Appears in book
        System.out.println(alice.firstOccurrenceOfMadHatter());
        

        Book mary = new Book("mary.txt");
        System.out.println(mary.getNumCharacters());
        System.out.println("Expected: 475");
        System.out.println(mary.firstOccurrenceOfMadHatter());
        
        System.out.println(alice.getSecondSentence());
        
        System.out.println(alice.occurrencesOf("daisies"));
    }
}
