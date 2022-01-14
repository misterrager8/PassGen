function toggleDiv(divId) {
    $('#' + divId).toggle();
}

function refreshDiv(divId) {
    $('#' + divId).load(location.href + ' #' + divId);
}

function copyPass(accountId) {
    var x = $('#copyThis' + accountId);
    x.show();
    x.select();
    document.execCommand('copy');
    x.hide();
}

function accountCreate() {
    $.post('account_create', {
        name: $('#name').val(),
        user_: $('#user_').val(),
        pass_: $('#pass_').val(),
        hint: $('#hint').val()
    }, function(data) {
        refreshDiv('accounts');
    });
}

function accountDelete(accountId) {
    $.get('account_delete', {
        id_: accountId
    }, function(data) {
        refreshDiv('accounts');
    });
}