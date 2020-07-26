$(document).ready(function () {
    $("form").submit(function (e) {
        e.preventDefault(); // avoid to execute the actual submit of the form.

        var form = $(this);

        $.ajax({
            type: "POST",
            url: "/estimate",
            data: form.serialize(), // serializes the form's elements.
            success: function (data) {
                swal("Estimate", Math.round((parseFloat(data) + Number.EPSILON) * 100) / 100 + " Lakhs");
            }
        });


    });
});



$.ajax({
    type: "POST",
    url: "/get_loc",
    success: function (data) {
        try {
            loc = JSON.parse(data);
            console.log(loc);
            for (var i = 0; i < loc.length; i++) {
                $("#area").append("<option value='" + loc[i] + "'>" + loc[i] + "</option>");
            }
        }
        catch (err) {

        }
    }
});


