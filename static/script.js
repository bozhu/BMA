$('#compute').click(function() {
    $('#lfsr').val('Waiting...');
    $('#span').val('');
    $('#timeused').val('');

    var seq = $('#seq').html();
    $.post('/compute', seq, function(result) {
        $('#lfsr').val(result.poly);
        $('#span').val(result.span);
        $('#timeused').val(result.time);
    }, 'json');
});
