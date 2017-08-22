/**
 * Created by apple on 17/8/21.
 */
/**
 * Created by Tacey Wong on 17/8/18.
 */



function miaopai_parser(doc, url) {
    console.log(url)
    return '{"data":url}';
}

function select_parser(url) {
    url = url;
    return miaopai_parser;
}

function after_parse(data) {
    return data;

}

function parse_video(url) {
    $.get(url, function (data, status) {
        var parser_selected = select_parser(url);
        var result = parser_selected(data, url);
        result = after_parse(result);
        return result
    }).error(function () {

        return "error";
    })

}

//Test
// 格式化解析结果
function fornat_json_to_web(json_data, show_dom) {
    var format = function () {
        var options = {
            dom: show_dom,
            quoteKeys: true,
            tabSize: 2,
        };
        window.jf = new JsonFormater(options);
        jf.doFormat(json_data);
    };
    format();

}

$("#parse_it").click(function () {
    var url = $('#page_url').val();
        console.log(url);
    var json_data = parse_video(url);
    console.log(json_data);
    fornat_json_to_web(json_data, '#parse_result');
});

