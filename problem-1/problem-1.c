#include <stdio.h>
 
int main() {
 	
	int a,b,c,sum=0;
	
	while (a<1000) {
	b=a % 3  ;
	c=a % 5  ;
	if (b==0 || c==0) {
	sum=sum+a ;
	}
	a = a+1 ;	
}
 	printf("The integer i am looking for is %d\n", sum);
 
	return 0;
}