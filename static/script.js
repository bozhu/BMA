$('#compute').click(function() {
    $('#lfsr').val('Waiting...');
    $('#span').val('');
    $('#timeused').val('');

    var seq = $('#seq').val();
    console.log(seq);
    $.post('/compute', seq, function(result) {
        $('#lfsr').val(result.poly);
        $('#span').val(result.span);
        $('#timeused').val(result.time);
    }, 'json');
});
