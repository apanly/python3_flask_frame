;
var user_login_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        $(".login_wrap .do-login").click(function () {
            var btn_target = $(this);
            if (btn_target.hasClass("disabled")) {
                common_ops.alert("正在处理!!请不要重复提交~~");
                return;
            }

            var email = $(".login_wrap input[name=email]").val();
            var pwd = $(".login_wrap input[name=pwd]").val();
            if (email == undefined || email.length < 1) {
                common_ops.alert("请输入正确的蘑菇邮箱~~");
                return;
            }
            if (pwd == undefined || pwd.length < 1) {
                common_ops.alert("请输入正确的邮箱密码~~");
                return;
            }
            btn_target.addClass("disabled");
            $.ajax({
                url: common_ops.buildUrl("/user/login"),
                type: 'POST',
                data: {'email': email, 'pwd': pwd},
                dataType: 'json',
                success: function (res) {
                    btn_target.removeClass("disabled");
                    var callback = null;
                    if (res.code == 200) {
                        callback = function () {
                            window.location.href = res.data.next_url;
                        }
                    }
                    common_ops.alert(res.msg, callback);
                }
            })
        });
    }

};

$(document).ready(function () {
    user_login_ops.init();
});