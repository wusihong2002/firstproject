import java.util.*;
public class array {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
int[] a= {2,2,4,5,6,71,5,6,74,3,};
for(int element:a)
	System.out.println(element);//打印a数组的每一个元素，一个元素占一行
//int[] copiednum=Arrays.copyOf(a, 9);拷贝数组，第一是数组，第二个是数组长度
int[] copiednum=Arrays.copyOf(a, 2*9);//第二个参数是新数组的长度
for(int ele:copiednum)
	System.out.println(ele);
}
}