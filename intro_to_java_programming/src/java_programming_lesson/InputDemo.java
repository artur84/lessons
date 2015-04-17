package java_programming_lesson;

import java.util.Scanner;

public class InputDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		System.out.print("How old are you? ");
		int age = in.nextInt();
		
		System.out.print("Next year you will be ");
		System.out.println(age + 1);
		
		in.close();

	}

}
