
//全局变量
var errorsPage = 1;
var errorsPageId = '';

//总行数
function errorsTotalRows() {
    const table = document.getElementById(errorsPageId); //获取的状态id
    return parseInt(table.rows.length)
}

// 默认调用方法
function errorsMethod(page_id) {
    errorsPageId = page_id;
    const table = document.getElementById(errorsPageId); //获取的状态id
    const number = errorsTotalRows();
    for (var i = 1; i < number; i ++ ){
        var s = parseInt(i + pageSize);
        if (number > s){
            table.rows[s].style.display = 'none';
        }
    }
    if (number == 1){
        tbody = document.getElementById('hide-errors-page');
        tr = document.createElement('tr');
        tr.innerHTML = '<td colspan="8" style="text-align: center; color: grey;">执行太棒了，没有错误的数据哦</td>';
        tbody.appendChild(tr);
    }
    errorsPre();
    errorsNext_pager();
}


//上一页方法
function errorsPre() {
    const class_page = document.getElementById('errors_pre');//获取按钮div的id
    var currentRow = pageSize * errorsPage; //获取当前行数  6 / 12 / 18
    if (currentRow == pageSize){
        class_page.innerHTML = "<li class='previous disabled'><a>上一页</a></li>"
    }
    else {
        class_page.innerHTML = "<li class='previous'><a href='JavaScript: errorsPreMethod()'>上一页</a></li>";
    }
}

//下一页方法
function errorsNext_pager() {
    const class_page = document.getElementById('errors_next');//获取按钮div的id
    total = errorsTotalRows(); //table总的总行数 3
    currentRow = pageSize * errorsPage; //获取当前行数 2
    nextRow = currentRow + pageSize; //下一页截止行数 4
    if (currentRow >= (total - 1) || pageSize == (total - 1)) { // 下一页截止行数等于行数，禁用下一页点击
        class_page.innerHTML = "<li class='next disabled' id='deposit'><a>下一页</a></li>"
    }
    else {
        class_page.innerHTML = "<li class='next'><a href='JavaScript: errorsNextMethod()'>下一页</a></li>";
    }
}

//上一页方法
function errorsPreMethod() {
    const table = document.getElementById(errorsPageId); //获取的状态id
    var maxRow = pageSize * errorsPage - pageSize;
    var startRow = maxRow - pageSize;
    if (startRow == 0){
        startRow = 1;
    }
    else {
        startRow = startRow + 1;
    }
    for (var i = startRow; i < maxRow + 1; i++){
        table.rows[i].style.display = '';
    }
    errorsPage --;
    errorsNext_pager();
    errors_close(startRow);
    errorsPre()
}

//上一页关闭方法
function errors_close(page_id) {
    startRow = page_id + pageSize;
    number = errorsTotalRows(); //table总的总行数
    table = document.getElementById(errorsPageId); //获取的状态id
    for (var i = startRow; i < number; i ++){
        table.rows[i].style.display = 'none';
    }
}

//下一页方法
function errorsNextMethod() {
    table = document.getElementById(errorsPageId); //获取的状态id
    className = document.getElementById('errors_next'); //获取按钮div的id
    number = errorsTotalRows(); //table总的总行数
    currentRow = pageSize * errorsPage; //获取当前行数
    nextRow = currentRow + (pageSize + 1); //下一页截止行数
    if (nextRow > number){ // 当下一页截止行数大于总行数，则下一页截止行数取总行数
        nextRow = number
    }
    for (var i = currentRow; i < nextRow; i ++) { // 从当前行数开始循环到下一页截止行数
        table.rows[i].style.display = '';
    }
    if (nextRow == number){ // 下一页截止行数等于行数，禁用下一页点击
        className.innerHTML = "<li class='next disabled' id='deposit'><a>下一页</a></li>"
    }
    currentPage = currentRow;
    errorsPage ++;
    errorsClose();
    errorsPre();
}

//下一页关闭方法
function errorsClose() {
    const table = document.getElementById(errorsPageId); //获取的状态id
    for (var i = 1; i < currentPage + 1; i ++){
        table.rows[i].style.display = 'none';
    }
}

