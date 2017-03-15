$(document).ready(function() {
    if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|BB|PlayBook|IEMobile|Windows Phone|Kindle|Silk|Opera Mini/i.test(navigator.userAgent)) {
        $('#buttonCamera').prop('disabled', true);    
    }
});

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            $('#ocrImage').attr('src', e.target.result)
            $('#buttonOpen').hide();
            $('#buttonCamera').hide();
            $('#buttonConvert').prop('disabled', false);
            $('#buttonReset').prop('disabled', false);
            $('#imageContainer').val(e.target.result);
            $('#ocrImage').show();
        };
        reader.readAsDataURL(input.files[0]);
    }
}

function openImage() {
    $('#imageUpload').trigger('click');
}

function openCamera() {
    $('#cameraDiv').show();
    $('#buttonCamera').prop('disabled', true);
    $('#buttonOpen').prop('disabled', true);
    Webcam.attach('#ocrCamera');
}

function resetImage() {
    $('#ocrImage').hide();
    $('#buttonOpen').show();
    $('#buttonCamera').show();
    $('#buttonConvert').prop('disabled', true);
    $('#buttonReset').prop('disabled', true);
}

function takeSnapshot() {
    Webcam.snap(function(data_uri) {
        $('#ocrImage').attr('src', data_uri)
        $('#buttonOpen').hide();
        $('#buttonCamera').hide();
        $('#buttonConvert').prop('disabled', false);
        $('#buttonReset').prop('disabled', false);
        $('#imageContainer').val(data_uri);
        $('#ocrImage').show();
    });
}

function stopCamera() {
    Webcam.reset();
    $('#cameraDiv').hide();
    $('#buttonCamera').prop('disabled', false);
    $('#buttonOpen').prop('disabled', false);
}

function copyText() {
    $("#ocrResult").select();
    document.execCommand("copy");
    alert('text copied to clipboard.');
}

function talkText() {
    responsiveVoice.speak($('#ocrResult').text());    
}