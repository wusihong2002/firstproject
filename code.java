import java.util.Scanner;

public class code {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
String greeting="Hello";
int n=greeting.length();
System.out.print(n);
System.out.print("  ");
int cpCount=greeting.codePointCount(0,greeting.length() );
System.out.print(cpCount);
System.out.print("  ");
char first=greeting.charAt(0);
char last=greeting.charAt(4);
System.out.print(first);
System.out.print("  ");
System.out.print(last);
Scanner in=new Scanner(System.in);
int i=in.nextInt();
int index=greeting.offsetByCodePoints(0, i);
int cp=greeting.codePointAt(index);
System.out.print(i);
	}

}
