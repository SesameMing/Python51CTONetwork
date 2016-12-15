/**
 * Created by Sesame on 2016/12/14.
 */
SELECTDATA=[
        {'id':1, 'value':"上线"},
        {'id':2, 'value':"下线"}
    ]

$(function () {
        $('td.tb').delegate('input','click',function(i){
            if($('table').attr('edit')=='true'){
                // 进入编辑
                if(!$(this).parent().parent().prop('edit')){
                    $(this).parent().parent().prop('edit',true);

                    // 获取 主机列 对象
                    var t1 =  $(this).parent().next().text();
                    $(this).parent().next().html('<input type="text" value="' + t1 +'">');

                    // 获取端口列对象
                    var t2 =  $(this).parent().next().next().text();
                    $(this).parent().next().next().html('<input type="text" value="' + t2 +'">');

                    // 获取在线列对象
                    var t3_id = $(this).parent().next().next().next().attr('selectid');
                    $(this).parent().next().next().next().html('<select></select>');
                        for (var i=0; i<SELECTDATA.length; i++){
                            $(this).parent().next().next().next().children().append('<option value="'+ SELECTDATA[i].id +'">'+SELECTDATA[i].value+'</option>')
                        }
                    $(this).parent().next().next().next().children().prop('value',t3_id);

                }else {
                // 退出编辑
                    $(this).parent().parent().prop('edit',false);
                    var t1 =  $(this).parent().next().children().val();
                    $(this).parent().next().html(t1);
                    var t2 =  $(this).parent().next().next().children().val();
                    $(this).parent().next().next().html(t2);

                    var t3_id = $(this).parent().next().next().next().children().val();
                    var t3_text = $(this).parent().next().next().next().children().find("option:selected").text();
                    console.log(t3_id);
                    $(this).parent().next().next().next().attr('selectid',t3_id);
                    $(this).parent().next().next().next().html(t3_text);

                }

            }
        })
    });

    //  全选
    function CheckAll() {
        $(':checkbox').prop('checked',true);
        if($('table').attr('edit')=='true'){
            $('input[type="checkbox"]').each(function (i) {
                if($(this).prop('checked')){
                    // 进入编辑

                    if(!$(this).parent().parent().prop('edit')){
                        $(this).parent().parent().prop('edit',true);

                        var t1 =  $(this).parent().next().text();
                        $(this).parent().next().html('<input type="text" value="' + t1 +'">');
                        var t2 =  $(this).parent().next().next().text();
                        $(this).parent().next().next().html('<input type="text" value="' + t2 +'">');

                        var t3_id = $(this).parent().next().next().next().attr('selectid');
                        $(this).parent().next().next().next().html('<select></select>');
                        for (var i=0; i<SELECTDATA.length; i++){
                            $(this).parent().next().next().next().children().append('<option value="'+ SELECTDATA[i].id +'">'+SELECTDATA[i].value+'</option>')
                        }

                       $(this).parent().next().next().next().children().prop('value',t3_id);
                    }

                }
            })
        }
    }

    // 取消
    function CancleAll() {
        $(':checkbox').prop('checked',false);
        if($('table').attr('edit')=='true'){
            // 退出编辑
            $('input[type="checkbox"]').each(function (i) {
                if(!$(this).prop('checked')){
                    if($(this).parent().parent().prop('edit')){
                        $(this).parent().parent().prop('edit',false);
                        var t1 =  $(this).parent().next().children().val();
                        $(this).parent().next().html(t1);
                        var t2 =  $(this).parent().next().next().children().val();
                        $(this).parent().next().next().html(t2);

                        var t3_id = $(this).parent().next().next().next().children().val();
                        var t3_text = $(this).parent().next().next().next().children().find("option:selected").text();
                        console.log(t3_id);
                        $(this).parent().next().next().next().attr('selectid',t3_id);
                        $(this).parent().next().next().next().html(t3_text);

                    }

                }
            })
        }
    }
    //反选
    function ReverseAll() {
        $(':checkbox').each(function () {
            if($(this).prop('checked')){
                // T退出编辑
                if($('table').attr('edit')=='true'){
                        $(this).parent().parent().prop('edit',false);
                        var t1 =  $(this).parent().next().children().val();
                        $(this).parent().next().html(t1);
                        var t2 =  $(this).parent().next().next().children().val();
                        $(this).parent().next().next().html(t2);

                        var t3_id = $(this).parent().next().next().next().children().val();
                        var t3_text = $(this).parent().next().next().next().children().find("option:selected").text();
                        console.log(t3_id);
                        $(this).parent().next().next().next().attr('selectid',t3_id);
                        $(this).parent().next().next().next().html(t3_text);

                    }

                $(this).prop('checked',false);
            }else {
                if($('table').attr('edit')=='true'){
                        $(this).parent().parent().prop('edit',true);
                        var t1 =  $(this).parent().next().text();
                        $(this).parent().next().html('<input type="text" value="' + t1 +'">');
                        var t2 =  $(this).parent().next().next().text();
                        $(this).parent().next().next().html('<input type="text" value="' + t2 +'">');


                        var t3_id = $(this).parent().next().next().next().attr('selectid');

                        $(this).parent().next().next().next().html('<select></select>');
                        for (var i=0; i<SELECTDATA.length; i++){
                            $(this).parent().next().next().next().children().append('<option value="'+ SELECTDATA[i].id +'">'+SELECTDATA[i].value+'</option>')
                        }

                       $(this).parent().next().next().next().children().prop('value',t3_id);
                    }
                $(this).prop('checked',true);
            }

        });
    }

    // 编辑模式与非编辑模式的切换
    function editModel(ths) {
        if($('table').attr('edit') == 'true'){
            $('table').attr('edit', false);
            $(ths).val('进入编辑模式');

            $('input[type="checkbox"]').each(function (i) {
                if($(this).prop('checked')){
                    if($(this).parent().parent().prop('edit')){
                        $(this).parent().parent().prop('edit',false);

                        var t1 =  $(this).parent().next().children().val();
                        $(this).parent().next().html(t1);
                        var t2 =  $(this).parent().next().next().children().val();
                        $(this).parent().next().next().html(t2);

                        var t3_id = $(this).parent().next().next().next().children().val();
                        var t3_text = $(this).parent().next().next().next().children().find("option:selected").text();
                        console.log(t3_id);
                        $(this).parent().next().next().next().attr('selectid',t3_id);
                        $(this).parent().next().next().next().html(t3_text);


                    }

                }
            })

        }else {
            $('table').attr('edit',true);
            $(ths).val('退出编辑模式');

             $('input[type="checkbox"]').each(function (i) {
                if($(this).prop('checked')){
                    if(!$(this).parent().parent().prop('edit')){
                        $(this).parent().parent().prop('edit',true);

                        var t1 =  $(this).parent().next().text();
                        $(this).parent().next().html('<input type="text" value="' + t1 +'">');
                        var t2 =  $(this).parent().next().next().text();
                        $(this).parent().next().next().html('<input type="text" value="' + t2 +'">');

                        var t3_id = $(this).parent().next().next().next().attr('selectid');

                        $(this).parent().next().next().next().html('<select></select>');
                        for (var i=0; i<SELECTDATA.length; i++){
                            $(this).parent().next().next().next().children().append('<option value="'+ SELECTDATA[i].id +'">'+SELECTDATA[i].value+'</option>')
                        }

                       $(this).parent().next().next().next().children().prop('value',t3_id);

                    }

                }
            })

        }
    }