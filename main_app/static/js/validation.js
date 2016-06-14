function checkField(id){
    var this_el = document.getElementById(id);
    if(!checkIfEmpty(id)) {
        if (id == "pwd") {
            checkPwdFormat(id);
        }
        if (id == "pwd" || id == "re-pwd") {
            checkPwdComp(id, "pwd", "re-pwd");
        }
        if (id == "email") {
            checkEmailFormat(id);
        }
    }
}

function checkPwdFormat(id) {
    var val = document.getElementById(id);
    var msg = "Password must contain capital letter, small letter, number and at least 8 letters";
    if(!/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/.test(val.value)){
        document.getElementById(id + "-err").innerHTML = msg;
    } else {
        if(document.getElementById(id + "-err").innerHTML == msg){
            document.getElementById(id + "-err").innerHTML = "";
        }
    }
}

function checkPwdComp(this_id, pwd, re_pwd){
    var pwd_el = document.getElementById(pwd);
    var re_pwd_el = document.getElementById(re_pwd);
    var msg = "Passwords are incompatible";

    if (pwd_el.value != re_pwd_el.value) {
        document.getElementById(this_id+"-err").innerHTML = msg;
    } else if(document.getElementById(this_id+"-err").innerHTML == msg) {
        document.getElementById("pwd-err").innerHTML = "";
        document.getElementById("re-pwd-err").innerHTML = "";
    }
}

function checkIfEmpty(id){
    var msg = "Field must be filled";
    if(document.getElementById(id).value == "") {
        document.getElementById(id + "-err").innerHTML = msg;
        return true;
    } else if(document.getElementById(id + "-err").innerHTML == msg) {
        document.getElementById(id + "-err").innerHTML = "";
        return false;
    }

}

function checkEmailFormat(id){
    var val = document.getElementById(id);
    var msg = "Email format is invalid";
    if(!/\S+@\S+\.\S+/.test(val.value)){
        document.getElementById(id + "-err").innerHTML = msg;
    } else if(document.getElementById(id + "-err").innerHTML == msg) {
        document.getElementById(id + "-err").innerHTML = "";
    }
}