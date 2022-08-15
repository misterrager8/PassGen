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

function copyPass(accountId) {
    $('#pass' + accountId).show();
    $('#pass' + accountId).select();
    document.execCommand('copy');
    $('#pass' + accountId).hide();
    
    
    $('#copyBtn' + accountId).toggleClass('bi-clipboard bi-clipboard-check text-success');
    setTimeout(function() {
        $('#copyBtn' + accountId).toggleClass('bi-clipboard bi-clipboard-check text-success');
    }, 1500);
}

function exportAccounts() {
    $.get('export_accounts', function(data) {
        $('#exportStatus').text(data);
    });
}