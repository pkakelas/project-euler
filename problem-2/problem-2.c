#include <stdio.h>
 
main() {
	int a = 1,b = 2,c = 3,sum = 2,rest;
	while (c < 4000000 ) {
		c = a + b;
		a = b;
		b = c;
		rest = c % 2; 
		if (rest == 0) {
			sum = sum + c;
		}
	}
	printf( "The integer i am looking for is %d", sum ) ;
	
	return 0;
}


