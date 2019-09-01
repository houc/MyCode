<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <title>404</title>
    <script src="https://cdn.staticfile.org/jquery/2.1.1/jquery.min.js"></script>
    <script type="text/javascript" src="http://{{url}}:{{port}}/my_static/jquery.rotate.min.js"></script>
    <script type="text/javascript" src="http://{{local_url}}:{{local_port}}/my_static/jquery.rotate.min.js"></script>
</head>
<script>

    $(function () {
       $('p').css({'font-weight':'bold', 'font-size':'120px', 'margin':'15% 40%','text-align':'center'});
        $('body').css({'background-color':'SandyBrown'});
        //旋转
        var angle = 0;
        setInterval(function(){
        angle += 1;
        $("#field").rotate(angle);
        }, 20);
    });

</script>
<body>
    <h1>页面失效，请检查url是否正确:</h1>
    <p id="field">404</p>
</body>
</html>