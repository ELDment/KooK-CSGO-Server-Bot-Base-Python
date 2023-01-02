<? 
    $Host = $_GET['Host'];
    $Port = $_GET['Port'];
    $Steam = "steam://rungameid/730//+connect ".$Host.":".$Port;
    header("location: $Steam"); 
    exit; 
?> 