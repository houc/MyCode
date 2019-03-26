
"""发送邮件生成的饼型统计图"""


HTML = '''<!DOCTYPE html>
<html style="height: %s">
   <head>
       <meta charset="utf-8">
   </head>
   <body style="height: %s; margin: 0">
       <div id="container" style="height: %s"></div>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/echarts.min.js"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts-gl/echarts-gl.min.js"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts-stat/ecStat.min.js"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/extension/dataTool.min.js"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/map/js/china.js"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/map/js/world.js"></script>
       <!--<script type="text/javascript" src="https://api.map.baidu.com/api?v=2.0&ak=xfhhaTThl11qYVrqLZii6w8qE5ggnhrY&__ec_v__=20190126"></script>-->
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/extension/bmap.min.js"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/simplex.js"></script>
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
            bottom: 470,
        },
        title: {
        text: '%s',
        subtext: '%s',
        bottom: 850,
        left: 'center',
    },
        tooltip: {
            trigger: 'axis',
            showContent: true,
        },
        dataset: {
            source: [
                ['product', '错误数', '失败数', '跳过数', '成功数'],
                ['错误数', '%s'],
                ['失败数', '%s'],
                ['跳过数', '%s'],
                ['成功数', '%s'],
            ]
        },
        xAxis: [
            {
                type: 'category',
                axisTick: {
                    alignWithLabel: true
                }
            }
        ],
        yAxis: {gridIndex: 0},
        grid: {top: '%s'},
        series: [
            // {type: 'line', smooth: true, seriesLayoutBy: 'column'},
            // {type: 'line', smooth: true, seriesLayoutBy: 'column'},
            // {type: 'line', smooth: true, seriesLayoutBy: 'column'},
            {type: 'line', smooth: true, seriesLayoutBy: 'column'},
            {
                type: 'pie',
                id: 'pie',
                radius: '%s',
                center: ['%s', '%s'],
                label: {
                    formatter: '%s'
                },
                encode: {
                    itemName: 'product',
                    value: '错误数',
                    tooltip: '成功数'
                }
            },
        ]
    };

    myChart.on('updateAxisPointer', function (event) {
        var xAxisInfo = event.axesInfo[0];
        if (xAxisInfo) {
            var dimension = xAxisInfo.value + 1;
            myChart.setOption({
                series: {
                    id: 'pie',
                    label: {
                        formatter: '%s'
                    },
                    encode: {
                        value: dimension,
                        tooltip: dimension
                    }
                }
            });
        }
    });

    myChart.setOption(option);

});
if (option && typeof option === "object") {
    myChart.setOption(option, true);
}
       </script>
   </body>
</html>
 
'''