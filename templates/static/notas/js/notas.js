$(document).ready(function() {
    var notas01 = $('.nota-1')
    var notas02 = $('.nota-2')
    notas01.each(function() {
        var nota1 = $(this)
        nota1.val(nota1.val().replace(/,/g, '.'))
    })
    notas02.each(function() {
        var nota2 = $(this)
        nota2.val(nota2.val().replace(/,/g, '.'))
    })
})