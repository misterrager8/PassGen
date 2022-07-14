$(document).ready(function() {
    document.documentElement.setAttribute('data-theme', localStorage.getItem('PassGen'));
});

function changeTheme(theme) {
    localStorage.setItem('PassGen', theme);
    document.documentElement.setAttribute('data-theme', localStorage.getItem('PassGen'));
}

function toggleDiv(divId) {
    $('#' + divId).fadeToggle(150);
}

function refreshPage() {
    $('#pageContent').load(location.href + ' #pageContent');
}

function createAccount() {
    $('#spinner').show();
    $.post('create_account', {
        name: $('#name').val(),
        username: $('#username').val(),
        password: $('#password').val(),
        hint: $('#hint').val()
    }, function(data) {
        refreshPage();
    });
}

function deleteAccount(accountId) {
    $('#spinner').show();
    $.get('delete_account', {
        id_: accountId
    }, function(data) {
        refreshPage();
    });
}

function copyPass(accountId) {
    document.getElementById('pass' + accountId).select();
    document.execCommand('copy');
    
    $('#copyBtn' + accountId).toggleClass('bi-clipboard bi-clipboard-check text-success');
    setTimeout(function() { $('#copyBtn' + accountId).toggleClass('bi-clipboard bi-clipboard-check text-success'); }, 1500);
}