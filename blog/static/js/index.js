/**
 * Created by Administrator on 2017/9/1.
 */
var request, log;
if (window.XMLHttpRequest) {
    request = new window.XMLHttpRequest();
}
else {
    request = new ActiveObject("Microsoft.XMLHTTP");
}
request.open("GET", '/index/log/session/', true);
request.send();
request.onreadystatechange = function () {
    if (request.readyState === 4 && request.status === 200) {
        log = request.responseText;
        if (log !== "default") {
            document.getElementById("user").innerHTML = "用户：" + log;
        }
    }
}
function new_article(id) {
    request.open("GET", '/index/log/session/', true);
    request.send();
    request.onreadystatechange = function () {
        if (request.readyState === 4 && request.status === 200) {
            log = request.responseText;
            if (log === "default") {
                alert("请先登录");
            }
            else {
                window.location.href = ("/index/edt/" + id + "/");
            }
        }
    }
}
function logout() {
    request.open("GET", "/index/log/out/", true)
    request.send();
    request.onreadystatechange = function () {
        if (request.readyState === 4 && request.status === 200) {
            if (request.responseText === "successful") {
                alert("已注销登录");
                window.location.href = ("/index/");
            }
            else {
                alert("还未登录");
            }
        }
    }
}
function article_search() {
    var title = document.getElementById("title").value;
    if(!/\S/.test(title)){
        alert("文章标题不能为空");
        return;
    }
    $.ajax({
        type: "POST",
        url: "search/",
        data: {
            title: title
        },
        success: function (id) {
            if (id!=="") {
                window.location.href = ("article/" + id + "/");
            }
            else {
                alert("该文章不存在");
            }
        },
        error: function () {
            alert("错误");
        }
    })
}