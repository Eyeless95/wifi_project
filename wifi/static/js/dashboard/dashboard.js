$(document).ready(function () {
    var dtable = $("#ads_datatable").dataTable({
        "bServerSide": true,
        "sAjaxSource": links.ajax_dashboard_datatable,
        "ordering": false,
        "bProcessing": true,
        "bLengthChange": true,
        "pageLength": 10,
        "bFilter": true,
        "autoWidth": false,
        "paging": true,
        "pagingType": 'numbers',
        "destroy": true,
        'sDom': 'rtpli',
        "bSortable": true,
        responsive: true,
        'aoColumnDefs': [
            {
                "aTargets": [0]
            },
            {
                "mRender": function (data, type, row) {
                    console.log(row[1]);
                    return '<img class="ad_image" src="' + row[1] + '">'
                },
                "aTargets": [1]
            },
            {
                "aTargets": [2]
            },
            {
                "aTargets": [3]
            }
        ]
    });

    $('#add_ad').click(function () {
        $('#add_modal').modal('show');
    });


    function add_adv(event) {
        event.preventDefault();
        var data = new FormData($('form').get(0));
        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: data,
            cache: false,
            processData: false,
            contentType: false,
            dataType: 'json',
            success: function (data) {
                if (data['status']) {
                    alert('Advertisement added successfully');
                    window.location.reload()
                }
                else {
                    alert('Advertisement was not added');
                    $('#add_modal').modal('hide')
                }
            }
        })
    }

    $('#add_form').submit(add_adv);
});
