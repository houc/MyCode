
//全局变量
var errorsPage = 1;
var errorPageSize = 10;
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
        var s = parseInt(i + errorPageSize);
        if (number > s){
            table.rows[s].style.display = 'none';
        }
    }
    errorsPre();
    errorsNext_pager();
}


//上一页方法
function errorsPre() {
    const class_page = document.getElementById('errors_pre');//获取按钮div的id
    var currentRow = errorPageSize * errorsPage; //获取当前行数  6 / 12 / 18
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
    var total = errorsTotalRows(); //table总的总行数 21
    var currentRow = errorPageSize * errorsPage; //获取当前行数 10
    var nextRow = currentRow + errorPageSize; //下一页截止行数 20
    if (nextRow == total || total <= errorPageSize) { // 下一页截止行数等于行数，禁用下一页点击
        class_page.innerHTML = "<li class='next disabled' id='deposit'><a>下一页</a></li>"
    }
    else {
        class_page.innerHTML = "<li class='next'><a href='JavaScript: errorsNextMethod()'>下一页</a></li>";
    }
}

//上一页方法
function errorsPreMethod() {
    const table = document.getElementById(errorsPageId); //获取的状态id
    var maxRow = errorPageSize * errorsPage - errorPageSize;
    var startRow = maxRow - errorPageSize;
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
    var startRow = page_id + errorPageSize;
    const number = errorsTotalRows(); //table总的总行数
    const table = document.getElementById(errorsPageId); //获取的状态id
    for (var i = startRow; i < number; i ++){
        table.rows[i].style.display = 'none';
    }
}

//下一页方法
function errorsNextMethod() {
    var table = document.getElementById(errorsPageId); //获取的状态id
    var className = document.getElementById('errors_next'); //获取按钮div的id
    var number = errorsTotalRows(); //table总的总行数
    var currentRow = errorPageSize * errorsPage; //获取当前行数
    var nextRow = currentRow + (errorPageSize + 1); //下一页截止行数
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

