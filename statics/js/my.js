//清空表单数据
function clearForm(id) {
      $("#"+id).find("input[name!='type']").val('');
      alert('waiting for perfect')
    }
    //获取表单数据
 function getFormdata(id) {
      var postData = {};
        var t = $('#'+id).serializeArray();
        $.each(t, function () {
            postData[this.name] = this.value;
        });
        return postData
 }

 //easy ui转成中文
    function formate_Chinee(id) {
        $("#"+id).datagrid('getPager').pagination({
            displayMsg: '当前显示从第{from}条到{to}条 共{total}条记录',
            beforePageText: '页数',
            afterPageText: '共{pages}页'
        })
    }