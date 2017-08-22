/**
 * Created by tacey wong on 17/8/21.
 * 调用parser()函数，传递一个url给他，并获取它返回的数据
 * 根据Android/iOS平台的技术实现交互
 */


function extend(Child, Parent) {
    var mid = function () {
    };
    mid.prototype = Parent.prototype;
    Child.prototype = new mid();
    Child.prototype.constructor = Child;
    Child.father = Parent.prototype;
}


function Downloader() {
    this.xhr = null
}
Downloader.prototype = {
    get_xmlhttp_obj: function () {
        var xmlHttp = null;
        try {
            // Firefox, Opera 8.0+, Safari
            xmlHttp = new XMLHttpRequest();
        } catch (e) {
            // Internet Explorer
            try {
                xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");
            } catch (e) {
                xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
            }
        }
        return xmlHttp;
    },
    js_download: function (url) {
        if (!this.xhr) {
            this.xhr = this.get_xmlhttp_obj();
        }
        if (!this.xhr) {
            alert("您的浏览器内核不支持AJAX！");
            return;
        }
        var responseText = null;
        try {
            xmlHttp.onreadystatechange = function () {
                if (this.xhr.readyState == 4) {
                    responseText = this.xhr.responseText;
                    alert(responseText);
                }
            };
            this.xhr.open("GET", url, false);//同步方式请求
            this.xhr.send(null);
        } catch (e) {
            console.log(e);
        }
        finally {
            this.xhr = null;
        }
        return responseText

    }
};


function BaseParser() {
    this.parser_name = "parser基类";
    this.page_url = "";
    this.init();
}

extend(BaseParser, Downloader);
BaseParser.prototype = {
    init: function () {
    },
    download: function (url) {
        return this.js_download(url);
    },
    text2dom: function (text) {
        try {
            xmlDoc = new ActiveXObject("Microsoft.XMLDOM");
            xmlDoc.async = "false";
            xmlDoc.loadXML(text);
            return (xmlDoc);
        }
        catch (e) {
            try {
                parser = new DOMParser();
                xmlDoc = parser.parseFromString(text, "text/xml");
                return (xmlDoc);
            }
            catch (e) {
                alert(e.message)
            }
        }
        return (null);
    },
    parse: function (url) {


    }

};


function js_download(url) {
    var xmlHttp = GetXmlHttpObject();

    if (xmlHttp == null) {
        alert("您的浏览器不支持AJAX！");
        return;
    }

    var url = url;
    var responseText = null;
    try {
        xmlHttp.onreadystatechange = function () {
            if (xmlHttp.readyState == 4) {
                responseText = xmlHttp.responseText;
                alert(responseText);
            }
        };
        xmlHttp.open("GET", url, false);//同步方式请求
        xmlHttp.send(null);
    } catch (e) {
        console.log(e);
    }
    return responseText

}
function GetXmlHttpObject() {
    var xmlHttp = null;
    try {
        // Firefox, Opera 8.0+, Safari
        xmlHttp = new XMLHttpRequest();
    } catch (e) {
        // Internet Explorer
        try {
            xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");
        } catch (e) {
            xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
        }
    }
    return xmlHttp;
}
function download(url, params, method, cookie_info) {

    //原生代码根据自己平台的技术抽象实现一个可供调用的下载器
    //此处调用Android/iOS原生方法进行下载
    //原生方法返回 content、status、cookie（允许为空）

    resp_text = js_download(url);
    var resp = {
        "content": resp_text,
        "status": 200,
        "cookie": null
    };
    return resp;
}
function text2dom(txt) {
    try {
        xmlDoc = new ActiveXObject("Microsoft.XMLDOM");
        xmlDoc.async = "false";
        xmlDoc.loadXML(txt);
        return (xmlDoc);
    }
    catch (e) {
        try {
            parser = new DOMParser();
            xmlDoc = parser.parseFromString(txt, "text/xml");
            return (xmlDoc);
        }
        catch (e) {
            alert(e.message)
        }
    }
    return (null);
}

function parser(video_page_url) {

    var resp = download(video_page_url);
    //此处根据response提供的信息,使用js代码解析出视频地址
    //先暂用resp["content"]第一个节点的text代替
    var content = resp["content"];
    var obj = text2dom(content);
    var title = obj.querySelector("title").textContent;
    var video_url = title;
    alert(video_url);
    // return video_page_url;
}


