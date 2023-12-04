$(document).ready(function() {
    $("#doctorSelect").change(function(e){
        let doctorId = $(this).find(":selected").val()
        $.ajax({
            url:"http://localhost:8000/doctors/" + doctorId,
            type: "GET",
            success: function(streets){
                debugger
                let schedulesSelect = $("#schedulesSelect");
                schedulesSelect.html('')
                streets.forEach((element) =>{
                    schedulesSelect.append(`
                        <option value="${element.id}">${element.name}</option>
                        `)
                })
            }
        })
    });
})