<?php
   session_start();
   unset($_SESSION["username"]);
   unset($_SESSION["pass"]);
   $_COOKIE['username']='';
   $_COOKIE['pass']='';
   header('Refresh: 2; URL = login.php');
   header('Location: login.php');
   
?>