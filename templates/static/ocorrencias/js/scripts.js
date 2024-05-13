$(document).on('click', '.btn-nova-ocorrencia', function() {
    var modalInputId = $('#ocorrencia-id')
    var modalInputTitulo = $('#ocorrencia-titulo')
    var modalInputDescricao = $('#ocorrencia-descricao')

    modalInputId.val('')
    modalInputTitulo.val('')
    modalInputDescricao.val('')
})

$(document).on('click', '.editar-ocorrencia', function() {
    var relacaoId = $(this).attr('data-relacao')
    var ocorrenciaId = $(this).attr('data-id');
    $.ajax({
        url: `/ocorrencias/${relacaoId}/edit/${ocorrenciaId}`,
        type: 'GET',
        datatype: 'json',
        success: function(data){
            var id = data.ocorrencia.id,
            titulo = data.ocorrencia.titulo,
            descricao = data.ocorrencia.descricao
          
            var modalInputId = $('#ocorrencia-id')
            var modalInputTitulo = $('#ocorrencia-titulo')
            var modalInputDescricao = $('#ocorrencia-descricao')

            var btnNovaOcorrencia = $('.btn-nova-ocorrencia')
            btnNovaOcorrencia.trigger('click')

            modalInputId.val(id)
            modalInputTitulo.val(titulo)
            modalInputDescricao.val(descricao)
        }
    })
})
