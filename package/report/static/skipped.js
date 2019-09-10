
//全局变量
var pageSize = 5; //默认展示几行
var page = 1;
var skippedPageId = '';

//总行数
function skippedTotalRows() {
    table = document.getElementById(skippedPageId); //获取的状态id
    return parseInt(table.rows.length)
}

// 默认调用方法
function skippedMethod(page_id) {
    skippedPageId = page_id;
    table = document.getElementById(skippedPageId); //获取的状态id
    number = skippedTotalRows();
    for (var i = 1; i < number; i ++ ){
        var s = parseInt(i + pageSize);
        if (number > s){
            table.rows[s].style.display = 'none';
        }
    }

    if (number == 1){
        tbody_fail = document.getElementById('hide-skipped-page');
        tr1 = document.createElement('br');
        tr = document.createElement('tr');
        tr.innerHTML = '<td colspan="8" style="text-align: center; color: grey">~~暂无数据~~</td>';
        tbody_fail.appendChild(tr1);
        tbody_fail.appendChild(tr);
    }
    skippedPre();
    skippedNext_pager();
}


//上一页方法
function skippedPre() {
    const class_page = document.getElementById('skip_pre');//获取按钮div的id
    currentRow = pageSize * page; //获取当前行数  6 / 12 / 18
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
    totalPage = skippedTotalRows(); //table总的总行数 17
    currentRow = pageSize * page; //获取当前行数 16
    nextRow = currentRow + pageSize; //下一页截止行数 32
    if (currentRow >= (totalPage - 1) || pageSize == (totalPage - 1)) { // 下一页截止行数等于行数，禁用下一页点击
        class_page.innerHTML = "<li class='next disabled' id='deposit'><a>下一页</a></li>"
    }
    else {
        class_page.innerHTML = "<li class='next'><a href='JavaScript: skippedNextMethod()'>下一页</a></li>";
    }
}

//上一页方法
function skippedPreMethod() {
    const table = document.getElementById(skippedPageId); //获取的状态id
    maxRow = pageSize * page - pageSize;
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
    page --;
    skippedNext_pager();
    skipped_close(startRow);
    skippedPre()
}

//上一页关闭方法
function skipped_close(page_id) {
    startRow = page_id + pageSize;
    const number = skippedTotalRows(); //table总的总行数
    const table = document.getElementById(skippedPageId); //获取的状态id
    for (var i = startRow; i < number; i ++){
        table.rows[i].style.display = 'none';
    }
}

//下一页方法
function skippedNextMethod() {
    table = document.getElementById(skippedPageId); //获取的状态id
    className = document.getElementById('skip_next'); //获取按钮div的id
    number = skippedTotalRows(); //table总的总行数
    currentRow = pageSize * page; //获取当前行数
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

