<?php
    $sum1 = $sum2 = 0;
    for ( $i = 0; $i < 101; $i++ ) {
        $sum1  += $i * $i;
    }
    for ( $i = 0; $i < 101; $i++ ) {
         $sum2 += $i;
    }
    $sum2 = $sum2 * $sum2;
    echo $sum2 - $sum1;
?>
