<!DOCTYPE html>
<html style="height: 100%" lang="zh-CN">
   <head>
       <meta charset="utf-8">
       <title>邮件报告</title>
   </head>
   <body style="height: 100%; margin: 0">
   <div id="container" style="height: 100%"></div>
   <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js"></script>
   <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/echarts-gl/dist/echarts-gl.min.js"></script>
   <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/echarts-stat/dist/ecStat.min.js"></script>
   <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/echarts/dist/extension/dataTool.min.js"></script>
   <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/echarts/map/js/china.js"></script>
   <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/echarts/map/js/world.js"></script>
   <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/echarts/dist/extension/bmap.min.js"></script>
   <script type="text/javascript">
var dom = document.getElementById("container");
var myChart = echarts.init(dom);
// var app = {};
option = null;

setTimeout(function () {
    option = {
        legend: {
            //orient: 'vertical',
            center: '30px',
            bottom: 520,
        },
        title: {
        text: '{{project_name}}统计简报',
        subtext: '{{scene}}',
        bottom: 910,
        left: 'center',
    },
        tooltip: {
            trigger: 'axis',
            showContent: true,
        },
        color : ['#EA0000', '#B87070', '#8E8E8E', '#006000', '#FFA500', '#00BFFF'], // 饼型图背景颜色重写
        dataset: {
            source: [
                ['product', '错误数', '失败数', '跳过数', '成功数', '预期失败', '意外成功'],
                ['错误数', {{error_count}}],
                ['失败数', {{fail_count}}],
                ['跳过数', {{skip_count}}],
                ['成功数', {{success_count}}],
                ['预期失败', {{guess_count}}],
                ['意外成功', {{accident_count}}],
            ]
        },
        xAxis: [
            {
                type: 'category',
                axisTick: {
                    alignWithLabel: true
                },
                data: ['错误数', '失败数', '跳过数', '成功数', '预期失败', '意外成功']
            }
        ],
        yAxis: [
            {gridIndex: 0},
        ],
        grid: {top: '55%'},
        series: [
            {
                data: [{{error_count}}, {{fail_count}}, {{skip_count}}, {{success_count}}, {{guess_count}}, {{accident_count}}],
                type: 'line',
                smooth: true
            },
            {
                type: 'pie',
                id: 'pie',
                radius: '25%',
                center: ['50%', '25%'],
                label: {
                    formatter: '{b}: {@错误数} ({d}%)'
                },
                encode: {
                    itemName: 'product',
                    value: '错误数',
                    tooltip: '成功数'
                }
            },
        ]
    };

    myChart.setOption(option);

});
if (option && typeof option === "object") {
    myChart.setOption(option, true);
}
       </script>
   </body>
</html>

