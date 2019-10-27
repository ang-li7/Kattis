import java.text.DecimalFormat;
import java.util.Scanner;

public class heartrate {
	public static void main(String[]args) {
		Scanner sc = new Scanner(System.in);
		double x = sc.nextDouble();
		DecimalFormat df = new DecimalFormat("#.####");
		System.out.println(df.format(x));
	}

}
