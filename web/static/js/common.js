;
var common_ops = {
    init:function(){
       this.eventBind();
    },
    eventBind:function(){

    },
    buildUrl:function( path ,params ){
        var url = $(".hidden_val_wrap input[name=domain]").val() + path;
        var _paramUrl = "";
        if(  params ){
            _paramUrl = Object.keys( params ).map( function( k ){
                return [ encodeURIComponent( k ),encodeURIComponent( params[ k ] ) ].join("=");
            }).join("&");
            _paramUrl = "?" + _paramUrl;
        }
        return url + _paramUrl;
    },
    alert:function( msg ,cb ){
        layer.alert( msg,{
            yes:function( index ){
                if( typeof cb == "function" ){
                    cb();
                }
                layer.close( index );
            }
        });
    },
    confirm:function( msg,callback ){
        callback = ( callback != undefined )?callback: { 'ok':null, 'cancel':null };
        layer.confirm( msg , {
            btn: ['确定','取消'] //按钮
        }, function( index ){
            //确定事件
            if( typeof callback.ok == "function" ){
                callback.ok();
            }
            layer.close( index );
        }, function( index ){
            //取消事件
            if( typeof callback.cancel == "function" ){
                callback.cancel();
            }
            layer.close( index );
        });
    },
    tip:function( msg,target ){
        layer.tips( msg, target, {
            tips: [ 3, '#e5004f']
        });
        $('html, body').animate({
            scrollTop: target.offset().top - 10
        }, 100);
    },
    msg:function( msg,flag,callback ){
        callback = (callback != undefined && typeof callback == "function") ? callback : null;
        var params = {
            "icon":6,
            "time": 1000,
            "shade" :[0.5 , '#000' , true]
        };
        if( !flag ){
            params['icon'] = 5;
            params['time'] = 1500;
        }
        layer.msg( msg ,params,callback );
    },
};

$(document).ready(function () {
    common_ops.init();
});
