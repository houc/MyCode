<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <title>500</title>
    <script src="https://cdn.staticfile.org/jquery/2.1.1/jquery.min.js"></script>
    <script type="text/javascript" src="http://{{url}}:{{port}}/my_static/jquery.rotate.min.js"></script>
    <script type="text/javascript" src="http://{{local_url}}:{{local_port}}/my_static/jquery.rotate.min.js"></script>
</head>
<script>

    $(function () {
       $('p').css({'font-weight':'bold', 'font-size':'120px', 'margin':'15% 40%','text-align':'center'});
        $('body').css({'background-color': 'Orange'});
        //旋转
        var angle = 0;
        setInterval(function(){
        angle += 1;
        $("#field").rotate(angle);
        }, 20);
    });
</script>
<body>
    <h1>url失效，请检查url是否正确或是否启用了多个bottle:</h1>
    <div><p id="field" style="text-align: center;">500</p></div>
</body>
</html>