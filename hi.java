
import java.util.Scanner;

public class hi {
	public static void main(String[]args) {
		Scanner sc = new Scanner(System.in);
		int n = Integer.parseInt(sc.nextLine());
		for(int i = 0; i<n; i++) {
			String x = sc.nextLine();
			if(x.length()<=10)
				System.out.println(x);
			else {
				String a = ""+x.charAt(0) + (x.length()-2) + x.charAt(x.length()-1);
				System.out.println(a);
			}
		}
	}
}
