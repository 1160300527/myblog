/**
 * Created by Administrator on 2017/8/25.
 */
if(document.getElementById("id").value.toString()!=="0"){
    document.getElementById("Time").style.display= "table";
}
var warning=document.getElementById("warning").value;
if ( warning=== "warning") {
    alert("该题目已存在");
    warning="yes";
    window.location.href=('/index/edt/'+document.getElementById("id").value+'/');
}
else if(warning === "blank"){
    alert("题目及内容不能为空！");
    warning="yes";
    window.location.href=('/index/edt/'+document.getElementById("id").value+'/');
}
else if(warning==="yes"){
    Date.prototype.Format = function (fmt) { //author: meizz
        var o = {
            "M+": this.getMonth() + 1,         //月份
            "d+": this.getDate(),          //日
            "h+": this.getHours(),          //小时
            "m+": this.getMinutes(),         //分
            "s+": this.getSeconds(),         //秒
            "q+": Math.floor((this.getMonth() + 3) / 3), //季度
            "S": this.getMilliseconds()       //毫秒
        };
        if (/(y+)/.test(fmt))
            fmt = fmt.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length));
        for (var k in o)
            if (new RegExp("(" + k + ")").test(fmt))
                fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
        return fmt;
    }
    var date = new Date();
    document.getElementById("Time").value = date.Format('yyyy-MM-dd hh:mm:ss');
    alert("提交时间:"+date.Format('yyyy-MM-dd hh:mm:ss'));
    window.location.href=('/index/');
}