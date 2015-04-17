package lesson4;

import java.util.Scanner;

public class LookUpAnyWord {
	public static void main(String args[])
	{
		Book aliceInWonderland = new Book("aliceInWonderland.txt");
		Scanner in = new Scanner(System.in);
		System.out.print("Type a word and press enter and I´ll tell you how many times"
				+ "it appears in \n"
				+ "Alice in Wonderland: ");
		String word = in.nextLine();
		int occurrences = aliceInWonderland.occurrencesOf(word);
		System.out.println(word + " occurrs " + occurrences + " times.");
		in.close();
	}

}
