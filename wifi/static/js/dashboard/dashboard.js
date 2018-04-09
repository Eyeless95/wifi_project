$(document).ready(function () {
    var ads_table = $("#ads_datatable").dataTable({
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
        "createdRow": function( row, data, dataIndex){
            if(!data[4]){
                $(row).addClass('disabled_row');
            }
        },
        'aoColumnDefs': [
            {
                "aTargets": [0]
            },
            {
                "mRender": function (data, type, row) {
                    return '<img class="ad_image" src="' + row[1] + '">'
                },
                "aTargets": [1]
            },
            {
                "aTargets": [2]
            },
            {
                "aTargets": [3]
            },
            {
                "mRender": function (data, type, row) {
                    if (!row[4]) {
                        $(row).addClass('disabled_row')
                    }
                    row.status_filter = '<div class="button-group">' +
                        format('<a data-btn-id="{btn_id}" class="del_btn">', {btn_id: row[5]}) +
                        format('<i class="fa fa-fw fa-trash" data-btn-id="{btn_id}"></i>', {btn_id: row[5]});
                    if (!row[4]) {
                        row.status_filter += format('<a data-btn-id="{btn_id}" data-action="show" class="show_btn">', {btn_id: row[5]});
                        row.status_filter += format('<i class="fa fa-fw fa-eye" data-action="show" data-btn-id="{btn_id}"></i></div>', {btn_id: row[5]});
                    }
                    else {
                        row.status_filter += format('<a data-btn-id="{btn_id}" data-action="hide" class="hide_btn">', {btn_id: row[5]});
                        row.status_filter += format('<i class="fa fa-fw fa-eye-slash" data-action="hide" data-btn-id="{btn_id}"></i></div>', {btn_id: row[5]});
                    }
                    return row.status_filter
                },
                "aTargets": [4]
            }
        ]
    });

    ads_table.on('click', '.show_btn, .hide_btn', function (event) {
        var btn = $(event.target);
        var id = btn.data('btn-id');
        var action = btn.data('action');
        var data = {'id': id, 'action': action};
        var csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            type: 'POST',
            url: links.change_ad_state,
            data: {
                csrfmiddlewaretoken: csrfmiddlewaretoken,
                'data': JSON.stringify(data)
            },
            dataType: 'json',
            success: function () {
                ads_table.api().ajax.reload(null, false)
            }
        })
    });

    ads_table.on('click', '.del_btn', function (event) {
        var btn = $(event.target);
        var id = btn.data('btn-id');
        var data = {'id': id, 'action': 'delete'};
        var c = confirm("Are yu sure you wan't to delete this ad?");
        if (!c) { return }
        var csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            type: 'POST',
            url: links.change_ad_state,
            data: {
                csrfmiddlewaretoken: csrfmiddlewaretoken,
                'data': JSON.stringify(data)
            },
            dataType: 'json',
            success: function () {
                ads_table.api().ajax.reload(null, false)
            }
        })
    });

    var format = function (str, col) {
        col = typeof col === 'object' ? col : Array.prototype.slice.call(arguments, 1);

        return str.replace(/\{\{|\}\}|\{(\w+)\}/g, function (m, n) {
            if (m == "{{") { return "{"; }
            if (m == "}}") { return "}"; }
            return col[n];
        });
    };


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
