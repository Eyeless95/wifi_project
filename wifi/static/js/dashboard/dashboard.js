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
});
