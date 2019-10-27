import java.util.Scanner;

public class encodedmessage {
	public static void main(String[]args) {
		Scanner sc = new Scanner(System.in);
		int n = Integer.parseInt(sc.nextLine());
		for(int i = 0; i<n; i++) {
			String[] x = sc.nextLine().split("");
			//System.out.println(x.length);
			int sq = (int)Math.sqrt((double)x.length);
			//System.out.println(sq);
			String z = "";
			for(int j = sq-1; j>=0; j--) {
				for(int k = 0; k<sq; k++) {
					z = z + x[j + k*sq];
				}
			}
			System.out.println(z);
		}
	}

}
