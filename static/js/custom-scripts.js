function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#image').attr('src', e.target.result)
                $('#btn-1').hide();
                $('#btn-2').hide();
                $('#btn-3').prop('disabled',false);
                $('#image_container').val(e.target.result);
                $('#image').show();
            };

            reader.readAsDataURL(input.files[0]);
        }
    }

function openImage()
{
	$('#image_upload').trigger('click');   
}
