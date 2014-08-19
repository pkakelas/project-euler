#include <stdio.h>
 
int main() {
 	
	int counter;
    int sum = 0;
	
    for ( counter = 1; counter < 1000; counter++ ) {
         if ( counter % 3 == 0 || counter % 5 == 0 ) {
            sum += counter;
         }
    }

 	printf( "The integer i am looking for is %d\n"  sum );
 
	return 0;
}
