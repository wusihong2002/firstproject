#include<stdio.h>
int main() {
	int x;
	double acr = 0;
	int ace;
	int number[100];
	printf("请输入数字的数量：");
	scanf("%d", &ace);
	if (ace > 0) {
		int number[ace];
		scanf("%d", &x);
		while (x != -1) {
			number[ace] = x;
			acr += x;
			ace++;
			scanf("%d", &x);
		}
	}
}