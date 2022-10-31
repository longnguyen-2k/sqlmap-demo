<?php

class Auth
{
    public $db = null;

    public function __construct(DBController $db)
    {
        if (!isset($db->con)) return null;
        $this->db = $db;
    }

    public  function login($username,$password){
        $sql = "SELECT * FROM users WHERE user_name='$username' AND password='$password'";
        error_log($sql);
        $result = mysqli_query($this->db->con, $sql);  
        if(mysqli_num_rows($result) === 1) {
            $row = mysqli_fetch_assoc($result);
            error_log(json_encode($row));
            $_SESSION['valid'] = true;
            $_SESSION['timeout'] = time();
            $_SESSION['username'] = $row['user_name'];
            return true;    
        }
        return false;
    }
}