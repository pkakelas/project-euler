<?php
    $sum=0;
    for ( $counter = 1; $counter < 1000; $counter++ ) {
         if ( $counter % 3 == 0 || $counter % 5 == 0 ) {
            $sum += $counter;
         }
    }
    echo $sum;
?>
