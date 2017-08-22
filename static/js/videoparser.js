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