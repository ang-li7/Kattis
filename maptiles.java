
import java.util.Scanner;

public class maptiles {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String s = sc.nextLine();
    int level = s.length();
    int x = 0, y = 0;
    for (int i = s.length()-1; i >= 0; i--) {
      switch (s.charAt(i)) {
        case '1':
          x += Math.pow(2, level-i-1);//level - (i + 1)) * 2 == 0? 1 : (level - (i + 1)) * 2 ;
          break;
        case '2':
          y += Math.pow(2, level-i-1);//level - (i + 1)) * 2 == 0? 1 : (level - (i + 1)) * 2 ;
          break;
        case '3':
          x += Math.pow(2, level-i-1);//level - (i + 1)) * 2 == 0? 1 : (level - (i + 1)) * 2 ;
          y += Math.pow(2, level-i-1);//level - (i + 1)) * 2 == 0? 1 : (level - (i + 1)) * 2 ;
          break;
        default:
          break;
      }
    }
    System.out.printf(level + " " + x + " " +y);
  }
}