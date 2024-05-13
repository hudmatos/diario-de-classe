$(document).on('click', '.btn-nova-programacao', function() {
    var modalInputId = $('#programa-id')
    var modalInputTitulo = $('#programa-titulo')
    var modalInputDescricao = $('#programa-descricao')

    modalInputId.val('')
    modalInputTitulo.val('')
    modalInputDescricao.val('')
})

$(document).on('click', '.editar-programa', function() {
    var relacaoId = $(this).attr('data-relacao')
    var programaId = $(this).attr('data-id');
    $.ajax({
        url: `/programados/${relacaoId}/edit/${programaId}`,
        type: 'GET',
        datatype: 'json',
        success: function(data){
            var id = data.programa.id,
            titulo = data.programa.titulo,
            descricao = data.programa.descricao
          
            var modalInputId = $('#programa-id')
            var modalInputTitulo = $('#programa-titulo')
            var modalInputDescricao = $('#programa-descricao')

            var btnNovoPrograma = $('.btn-nova-programacao')
            btnNovoPrograma.trigger('click')

            modalInputId.val(id)
            modalInputTitulo.val(titulo)
            modalInputDescricao.val(descricao)
        }
    })
})
