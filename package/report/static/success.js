
//全局变量
var successPage = 1;
var successPageId = '';

//总行数
function successTotalRows() {
    table = document.getElementById(successPageId); //获取的状态id
    return parseInt(table.rows.length)
}

// 默认调用方法
function successMethod(page_id) {
    successPageId = page_id;
    const table = document.getElementById(successPageId); //获取的状态id
    const number = successTotalRows();
    for (var i = 1; i < number; i ++ ){
        var s = parseInt(i + pageSize);
        if (number > s){
            table.rows[s].style.display = 'none';
        }
    }

    if (number == 1){
        tbody_fail = document.getElementById('hide-success-page');
        tr1 = document.createElement('br');
        tr = document.createElement('tr');
        tr.innerHTML = '<td colspan="8" style="text-align: center; color: grey">~~暂无数据~~</td>';
        tbody_fail.appendChild(tr1);
        tbody_fail.appendChild(tr);
    }
    successPre();
    successNext_pager();
}


//上一页方法
function successPre() {
    const class_page = document.getElementById('success_pre');//获取按钮div的id
    currentRow = pageSize * successPage; //获取当前行数  6 / 12 / 18
    if (currentRow == pageSize){
        class_page.innerHTML = "<li class='previous disabled'><a>上一页</a></li>"
    }
    else {
        class_page.innerHTML = "<li class='previous'><a href='JavaScript: successPreMethod()'>上一页</a></li>";
    }
}

//下一页方法
function successNext_pager() {
    class_page = document.getElementById('success_next');//获取按钮div的id
    totalPages = successTotalRows(); //table总的总行数 96
    currentRow = pageSize * successPage; //获取当前行数 94
    nextRow = currentRow + pageSize; //下一页截止行数 188
    if (currentRow >= (totalPages - 1) || pageSize == (totalPages - 1)) { // 下一页截止行数等于行数，禁用下一页点击
        class_page.innerHTML = "<li class='next disabled' id='deposit'><a>下一页</a></li>"
    }
    else {
        class_page.innerHTML = "<li class='next'><a href='JavaScript: successNextMethod()'>下一页</a></li>";
    }
}

//上一页方法
function successPreMethod() {
    const table = document.getElementById(successPageId); //获取的状态id
    maxRow = pageSize * successPage - pageSize;
    startRow = maxRow - pageSize;
    if (startRow == 0){
        startRow = 1;
    }
    else {
        startRow = startRow + 1;
    }
    for (var i = startRow; i < maxRow + 1; i++){
        table.rows[i].style.display = '';
    }
    successPage --;
    successNext_pager();
    success_close(startRow);
    successPre()
}

//上一页关闭方法
function success_close(page_id) {
    startRow = page_id + pageSize;
    const number = successTotalRows(); //table总的总行数
    const table = document.getElementById(successPageId); //获取的状态id
    for (var i = startRow; i < number; i ++){
        table.rows[i].style.display = 'none';
    }
}

//下一页方法
function successNextMethod() {
    table = document.getElementById(successPageId); //获取的状态id
    className = document.getElementById('success_next'); //获取按钮div的id
    number = successTotalRows(); //table总的总行数
    currentRow = pageSize * successPage; //获取当前行数
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
    successPage ++;
    successClose();
    successPre();
}

//下一页关闭方法
function successClose() {
    const table = document.getElementById(successPageId); //获取的状态id
    for (var i = 1; i < currentPage + 1; i ++){
        table.rows[i].style.display = 'none';
    }
}
