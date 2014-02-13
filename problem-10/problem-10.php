<?php
    function isPrime( $num ) {
        for ( $counter = 2; $counter <= sqrt( $num ); $counter++ ) {
            if ( $num % $counter == 0 ) {
                return false;
            }   
        }
        return true;
    }
    
    $sum = 0;

    for ( $i = 2; $i < 2000000; $i++ ) {
        if ( isPrime( $i ) ) {
            $sum += $i;
        }    
    }

    echo $sum;
?>

