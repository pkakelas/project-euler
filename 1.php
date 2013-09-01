<?php
$sum=0 ;
$a=1 ;
while ($a<1000) {
	$b=fmod($a, 3) ;
	$c=fmod($a, 5) ;
	if ($b==0 or $c==0) {
	$sum=$sum+$a ;
	}
	$a = $a+1 ;	
}
echo $sum ;
?>