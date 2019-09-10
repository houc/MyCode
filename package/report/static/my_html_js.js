
/*饼型图js*/
function pie_img(error, success, skip, fail, unexpected_success, failure) {
    const dom = document.getElementById("container");
    const myChart = echarts.init(dom);
        // var app = {};
        option = null;
        option = {
            title : {
                text: '结果走势', // 饼型图标题
                x: '40%',        // 居中位置偏移
                textStyle: {
                            fontSize: 20 // 标题字体样式
                    }
            },
            tooltip : {
                trigger: 'axis',
                showContent: false // 饼型图是否启用hover
            },
            legend: {
                orient: 'vertical', // 左上方样式
                x: '1%',            // 左上方位置偏移
                textStyle: {
                            fontSize: 12
                    }
            },
            color : ['#EA0000', '#8E8E8E', '#006000', '#B87070', '#00BFFF', '#FFA500'], // 饼型图背景颜色重写
            series : [
                {
                    type: 'pie',  // 图形样式
                    radius : '65%', // 图形大小
                    center: ['45%', '55%'], // 图形位置偏移量【左-右，上-下】
                    label: {
                        formatter: '{b} : {c} ({d}%)', // 计算方式
                        textStyle: {
                            fontSize: 12
                        }
                    },
                    data:[
                        {value: error, name: '错误数'},
                        {value: skip, name: '跳过数'},
                        {value: success, name: '成功数'},
                        {value: fail, name: '失败数'},
                        {value: unexpected_success, name: '意外成功数'},
                        {value: failure, name: '预期失败数'}
                    ] // 数据
                }
            ]
        };
    if (option && typeof option === "object") {
        myChart.setOption(option, true); // 调用函数
    }
}


/*附件新窗口打开*/
function look_img_windows(content) {
    if (content == "" || content == "None") {
        return false
    }
    else {
        const new_win = window.open();
        new_win.document.write("<img src=" + content + " />")
    }
}

