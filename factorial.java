import java.util.Scanner;

public class factorial {
	public static void main(String[]args) {
		Scanner sc = new Scanner(System.in);
		int n = Integer.parseInt(sc.nextLine());
		for(int i = 0; i<n; i++) {
			int x = Integer.parseInt(sc.nextLine());
			if(x>4)
				System.out.println(0);
			else {
				if(x == 1)
					System.out.println(1);
				if(x == 2)
					System.out.println(2);
				if(x == 3)
					System.out.println(6);
				if(x == 4)
					System.out.println(4);
			}
		}
	}

}
