import java.io.BufferedReader;
//import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class quadrant {
	public static void main(String[]args) {
		Scanner sc = new Scanner(System.in);
		//BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
		int x = Integer.parseInt(sc.nextLine());
		int y = Integer.parseInt(sc.nextLine());
		//int x = Integer.parseInt(sc.readLine());
		//int y = Integer.parseInt(sc.readLine());
		if(x>0 && y>0) {
			System.out.println("1");
		}
		else if(x<0 && y>0) {
			System.out.println("2");
		}
		else if(x<0 && y<0) {
			System.out.println("3");
		}
		else{
			System.out.println("4");
		}
		
	}

}
