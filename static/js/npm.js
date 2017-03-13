function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#image').attr('src', e.target.result)
                $('#btn-1').hide();
                $('#btn-2').hide();
                $('#btn-3').prop('disabled',false);
                $('#image').show();
            };

            reader.readAsDataURL(input.files[0]);
        }
    }

function openImage()
{
	$('#fileUpload').trigger('click');   
}