#include <stdio.h>

int main() {
	
	int a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, number, count=20;
	
	while (number==0) {
		a=count%2;
		b=count%3;
		c=count%4;
		d=count%5;
		e=count%6;
		f=count%7;
		g=count%8;
		h=count%9;
		i=count%10;
		j=count%11;
		k=count%12;
		l=count%13;
		m=count%14;
		n=count%15;
		o=count%16;
		p=count%17;
		q=count%18;
		r=count%19;
		s=count%20;
		if(a==0 && b==0 && c==0 && d==0 && e==0 && f==0 && g==0 && h==0 && i==0 && j==0 && k==0 && l==0 && m==0 && n==0 			&& o==0 && p==0 && q==0 && r==0 && s==0 ){
			number=count;
		}
	count=count+20;
	}
	printf("The number i am looking for is %d",number);
	return 0;
}
