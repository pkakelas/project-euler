<?php 		
	$sum = 2;	
	$a = 1;
	$b = 2 ;
	$c = 3;
	while ( $c < 4000000 ) {
		$c = $a + $b;
        $a = $b;
		$b = $c;
		$rest = fmod( $c, 2 );
         if ( $rest == 0 ) {
			$sum += $c;
		}
	}
	echo $sum;
?>
