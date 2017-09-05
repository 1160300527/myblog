/**
 * Created by Administrator on 2017/8/26.
 */
let checked = "in";
function con() {
    let i, flagW = 0, flagw = 0, flagd = 0;
    /*注:document.getElementById().value得到的均为字符串类型，可用parseInt()解析返回整型*/
    let thisname = new Array(32);
    thisname = document.getElementById("txtname").value;
    let thispass = new Array(32);
    thispass = document.getElementById("txtpass").value;
    if (!thisname.length) {
        alert("用户名不得为空，请重新输入");
        return;
    }
    let fn = thisname[0];
    if (!((fn >= 'a' && fn <= 'z') || (fn >= 'A' && fn <= 'Z') || (fn >= '0' && fn <= '9'))) {
        alert("用户名格式错误，请重新输入");
        return;
    }
    for (i = 1; i < thisname.length; i++) {
        if (thisname[i] === ' ') {
            alert("用户名格式错误，请重新输入");
            return;
        }
    }
    if (!thispass.length) {
        alert("密码不得为空，请重新输入");
        return;
    }
    for (i = 0; i < thispass.length; i++) {
        if (!flagw && thispass[i] >= 'a' && thispass[i] <= 'z') {
            flagw = 1;
        }
        else if (!flagW && thispass[i] >= 'A' && thispass[i] <= 'Z') {
            flagW = 1;
        }
        else if (!flagd && thispass[i] >= '0' && thispass[i] <= '9') {
            flagd = 1;
        }
        else if (thispass[i] === ' ') {
            alert("密码中不得包含空格");
            return;
        }
    }
    if (!(flagw && flagW && flagd)) {
        alert("密码必须同时包含大小写字母及数字");
        return;
    }
    var request;
    if (window.XMLHttpRequest) {
        request = new window.XMLHttpRequest();
    }
    else {
        request = new ActiveObject("Microsoft.XMLHTTP");
    }
    if (checked === "in") {
        $.ajax({
            type:"POST",
            url:"/index/log/login/",
            data:{
                name:thisname,
                password:thispass
            },
            success:function (information) {
                if (information === "successful") {
                    alert("登录成功");
                    window.location.href = ('/index/');
                }
                else if(information ==="name_none"){
                    alert("该用户不存在");
                }
                else if(information === "password_wrong"){
                    alert("密码错误");
                }
            },
            error:function () {
                alert("出现错误");
            }
        });
    }
    if (checked === "up") {
        var thisemail = new Array(64);
        thisemail = document.getElementById("email").value;
        var thisphone = new Array(32);
        thisphone = document.getElementById("phone").value;
        if (thisphone.length !== 13) {
            alert("电话号码位数应有13位");
            return;
        }
        if (thisphone[0] !== '8' || thisphone[1] !== '6') {
            alert("电话号码位数应以86开头");
            return;
        }
        for (i = 2; i < 13; i++) {
            if (thisphone[i] < '0' || thisphone[i] > '9') {
                alert("电话号码位数只能以数字组成");
                return;
            }
        }
        $.ajax({
            type:"POST",
            url:"/index/log/signup/",
            data:{
                name:thisname,
                password:thispass,
                email:thisemail,
                phone:thisphone
            },
            success:function (information) {
                if(information ==="successful"){
                    confirm("注册成功");
                    window.location.href=('/index/');
                }
                else if(information === "name_repeat"){
                    alert("该名称已存在");
                }
                else if (information ==="email_repeat"){
                    alert("邮箱地址已注册");
                }
                else if (information ==="phone_repeat"){
                    alert("该电话号码已注册");
                }
                else {
                    alert("asdf");
                }
            },
            error:function () {
                alert("Wrong");
            }
        })
    }
}
function signin() {
    var form2 = document.getElementsByClassName("dis");
    for (var i = 0; i < form2.length; i++) {
        form2[i].style.display = "none";
    }
    var sign1 = document.getElementById("in");
    var sign2 = document.getElementById("up");
    sign2.style.background = "#3b474f";
    sign1.style.background = "#2C3A46";
    checked = "in";
}
function signup() {
    var form2 = document.getElementsByClassName("dis");
    for (var i = 0; i < form2.length; i++) {
        form2[i].style.display = "table-row";
    }
    var sign1 = document.getElementById("in");
    var sign2 = document.getElementById("up");
    sign1.style.background = "#3b474f";
    sign2.style.background = "#2C3A46";
    checked = "up";
}
