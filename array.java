import java.util.*;
public class array {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
int[] a= {2,2,4,5,6,71,5,6,74,3,};
for(int element:a)
	System.out.println(element);//��ӡa�����ÿһ��Ԫ�أ�һ��Ԫ��ռһ��
//int[] copiednum=Arrays.copyOf(a, 9);�������飬��һ�����飬�ڶ��������鳤��
int[] copiednum=Arrays.copyOf(a, 2*9);//�ڶ���������������ĳ���
for(int ele:copiednum)
	System.out.println(ele);
}
}