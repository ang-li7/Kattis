import java.util.Scanner;

public class radiocommercials{
	public static void main(String[]args) {
		Scanner sc = new Scanner(System.in);
		String[] np = sc.nextLine().split(" ");
		int n = Integer.parseInt(np[0]);
		int p = Integer.parseInt(np[1]);
		String[] xx = sc.nextLine().split(" ");
		int[] x = new int[n];
		for(int i = 0; i<n; i++) {
			x[i] = Integer.parseInt(xx[i]) - p;
		}
		int[] dp = new int[n+1];
		for(int i = 0; i<n+1; i++) {
			dp[i] = 0;
		}
		for(int i = 1; i<n+1; i++) {
			int temp = dp[i-1] + x[i-1];
			if(temp>0) {
				dp[i] = temp;
			}
			else {
				dp[i] = 0;
			}
		}
		//System.out.println();
		int max = 0;
		for(int i = 0; i<n+1; i++) {
			if (dp[i]>max){
				max = dp[i];
			}
		}
		System.out.println(max);
	}

}
