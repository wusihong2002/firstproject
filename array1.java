import java.util.*;
public class array1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
Scanner in=new Scanner(System.in);
System.out.print("��Ҫ�¼�����");
int k=in.nextInt();
System.out.print("�µ�����������");
int n=in.nextInt();
int[] number=new int[n];
for(int i=0;i<number.length;i++)
	number[i]=i+1;
int[] result=new int[k];
for(int i=0;i<result.length;i++) {
	int r=(int)(Math.random()*n);
	result[i]=number[r];
	number[r]=number[n-1];
	n--;
}
Arrays.sort(result);
System.out.println("bet the following combination. it'll make you rich.");
for(int r:result)
	System.out.println(r);
	}

}
