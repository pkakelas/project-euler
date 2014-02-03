<?
    $sum1 = $sum2 = 0;
    for ( $i = 0; $i < 101; $i++ ) {
        $res = $i * $i;
        $sum1 = $sum1 + $res;
    }
    for ( $i = 0; $i < 101; $i++ ) {
         $sum2 = $sum2 + $i;
    }
    $sum2 = $sum2 * $sum2;
    echo $sum2 - $sum1;
?>
