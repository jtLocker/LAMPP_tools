<?php

$url = "https://api.coinbase.com/v2/prices/BTC-USD/spot";
$file = file_get_contents($url);

$json = json_decode($file, TRUE);

?>

<?php echo $json["data"]["amount"];?>
