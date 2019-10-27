import java.util.HashMap;
import java.util.Scanner;

public class sumsquareddigits {
	public static void main(String[] args) {
		Scanner kb=new Scanner(System.in);
		int w= Integer.parseInt(kb.nextLine());
		HashMap<Character, Integer> map=new HashMap<Character, Integer>();
		map.put('A', 100);
		map.put('B', 121);
		map.put('C', 144);
		map.put('D', 169);
		map.put('E', 196);
		map.put('F', 225);
		map.put('0', 0);
		map.put('1', 1);
		map.put('2', 4);
		map.put('3', 9);
		map.put('4', 16);
		map.put('5', 25);
		map.put('6', 36);
		map.put('7', 49);
		map.put('8', 64);
		map.put('9', 81);
		for(int i=0; i<w; i++) {
			int aa=kb.nextInt();
			//System.out.println(aa);
			int base=kb.nextInt();
			Integer y=Integer.parseInt(kb.next());
			String hey=y.toString(base);
			System.out.println("Hey "+hey);
			int sum=0;
			for(int j=0; j<hey.length(); j++) {
				int e=map.get(hey.charAt(j));
				sum+=e;
			}
			System.out.println((i+1)+" "+sum);
		}
		
	}

}