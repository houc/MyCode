
//全局变量
var pageSize = 15; //默认展示几行
var page = 1;
var skippedPageId = '';

//总行数
function skippedTotalRows() {
    const table = document.getElementById(skippedPageId); //获取的状态id
    return parseInt(table.rows.length)
}

// 默认调用方法
function skippedMethod(page_id) {
    skippedPageId = page_id;
    const table = document.getElementById(skippedPageId); //获取的状态id
    const number = skippedTotalRows();
    for (var i = 1; i < number; i ++ ){
        var s = parseInt(i + pageSize);
        if (number > s){
            table.rows[s].style.display = 'none';
        }
    }
    skippedPre();
    skippedNext_pager();
}


//上一页方法
function skippedPre() {
    const class_page = document.getElementById('skip_pre');//获取按钮div的id
    var currentRow = pageSize * page; //获取当前行数  6 / 12 / 18
    if (currentRow == pageSize){
        class_page.innerHTML = "<li class='previous disabled'><a>上一页</a></li>"
    }
    else {
        class_page.innerHTML = "<li class='previous'><a href='JavaScript: skippedPreMethod()'>上一页</a></li>";
    }
}

//下一页方法
function skippedNext_pager() {
    const class_page = document.getElementById('skip_next');//获取按钮div的id
    var number = skippedTotalRows(); //table总的总行数
    var currentRow = pageSize * page; //获取当前行数
    var nextRow = currentRow + (pageSize + 1); //下一页截止行数
    if (nextRow == number || number <= pageSize) { // 下一页截止行数等于行数，禁用下一页点击
        class_page.innerHTML = "<li class='next disabled' id='deposit'><a>下一页</a></li>"
    }
    else {
        class_page.innerHTML = "<li class='next'><a href='JavaScript: skippedNextMethod()'>下一页</a></li>";
    }
}

//上一页方法
function skippedPreMethod() {
    const table = document.getElementById(skippedPageId); //获取的状态id
    var maxRow = pageSize * page - pageSize;
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
    page --;
    skippedNext_pager();
    skipped_close(startRow);
    skippedPre()
}

//上一页关闭方法
function skipped_close(page_id) {
    var startRow = page_id + pageSize;
    const number = skippedTotalRows(); //table总的总行数
    const table = document.getElementById(skippedPageId); //获取的状态id
    for (var i = startRow; i < number; i ++){
        table.rows[i].style.display = 'none';
    }
}

//下一页方法
function skippedNextMethod() {
    var table = document.getElementById(skippedPageId); //获取的状态id
    var className = document.getElementById('skip_next'); //获取按钮div的id
    var number = skippedTotalRows(); //table总的总行数
    var currentRow = pageSize * page; //获取当前行数
    var nextRow = currentRow + (pageSize + 1); //下一页截止行数
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
    page ++;
    skippedClose();
    skippedPre();
}

//下一页关闭方法
function skippedClose() {
    const table = document.getElementById(skippedPageId); //获取的状态id
    for (var i = 1; i < currentPage + 1; i ++){
        table.rows[i].style.display = 'none';
    }
}

