$(document).ready(function() {
    if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|BB|PlayBook|IEMobile|Windows Phone|Kindle|Silk|Opera Mini/i.test(navigator.userAgent)) {
        $('#buttonCamera').hide();
        $('#linkWebCapture').hide();
    }
});


function readImage(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            $('#ocrImage').attr('src', e.target.result)
            $('#buttonExtract').prop('disabled', false);
            $('#buttonReset').prop('disabled', false);
            $('#imageContainer').val(e.target.result);
            $('#ocrImageDiv').show();
        };
        reader.readAsDataURL(input.files[0]);
    }
}

function openImage() {
    $('#imageUpload').trigger('click');
}

function loadImage() {
    var imageUrl = $('#imageUrl').val()
    $('#ocrImage').attr('src', imageUrl);
    $('#buttonExtract').prop('disabled', false);
    $('#buttonReset').prop('disabled', false);
    $('#buttonLoad').prop('disabled', true);
    $('#imageContainer').val(imageUrl);
    $('#ocrImageDiv').show();
}

function resetImage() {
    $('#ocrImageDiv').hide();
    $('#buttonExtract').prop('disabled', true);
    $('#buttonReset').prop('disabled', true);
    $("#imageUpload").val("");
}

function resetUrl() {
    $('#ocrImageDiv').hide();
    $('#buttonExtract').prop('disabled', true);
    $('#buttonReset').prop('disabled', true);
    $('#buttonLoad').prop('disabled', false);
    $('#imageUrl').val("");
}

function resetText() {
    $("#translateText").val("");
    $('#buttonTranslate').prop('disabled', true);
    $('#buttonReset').prop('disabled', true);
    $('#fromLanguage').val("detect");
    $('#toLanguage').val("af");
}

function detectText() {
    var translateText = $("#translateText").val();
    if (translateText.length) {
        $('#buttonTranslate').prop('disabled', false);
        $('#buttonReset').prop('disabled', false);
    } else {
        $('#buttonTranslate').prop('disabled', true);
        $('#buttonReset').prop('disabled', true);
    }
}

function openCamera() {
    $('#cameraDiv').show();
    $('#buttonCamera').prop('disabled', true);
    Webcam.attach('#ocrCamera');
}

function takeSnapshot() {
    Webcam.snap(function(data_uri) {
        $('#ocrImage').attr('src', data_uri)
        $('#buttonCamera').hide();
        $('#buttonExtract').prop('disabled', false);
        $('#buttonReset').prop('disabled', false);
        $('#imageContainer').val(data_uri);
        $('#ocrImageDiv').show();
    });
}

function stopCamera() {
    Webcam.reset();
    $('#cameraDiv').hide();
    $('#buttonCamera').show();
    $('#buttonCamera').prop('disabled', false);
}


function copyText() {
    $('#resultantText').select();
    document.execCommand("copy");
    alert('text copied to clipboard.');
}

function talkText() {
    ocrText = $('#resultantText').val();
    talkVoice = $('#talkVoice').val();
    responsiveVoice.speak(ocrText, talkVoice, {
        onstart: function() { $('#talkButton').prop('disabled', true) },
        onend: function() { $('#talkButton').prop('disabled', false) }
    });
}

function setVoice()
{
    var sourceLanguage = $('#toLanguage').val();
    var voice = 'UK English Female';
    switch (sourceLanguage)
    {
        case 'en': voice = "UK English Female"; break;
        case 'ar': voice = "Arabic Female"; break;
        case 'hy': voice = "Armenian Male"; break;
        case 'zh-CN': voice = "Chinese Female"; break;
        case 'cs': voice = "Czech Female"; break;
        case 'da': voice = "Danish Female"; break;
        case 'de': voice = "Deutsch Female"; break;
        case 'nl': voice = "Dutch Female"; break;
        case 'fi': voice = "Finnish Female"; break;
        case 'fr': voice = "French Female"; break;
        case 'el': voice = "Greek Female"; break;
        case 'hi': voice = "Hindi Female"; break;
        case 'hu': voice = "Hungarian Female"; break;
        case 'id': voice = "Indonesian Female"; break;
        case 'it': voice = "Italian Female"; break;
        case 'ja': voice = "Japanese Female"; break;
        case 'ko': voice = "Korean Female"; break;
        case 'la': voice = "Latin Female"; break;
        case 'no': voice = "Norwegian Female"; break;
        case 'pl': voice = "Polish Female"; break;
        case 'pt': voice = "Portuguese Female"; break;
        case 'ro': voice = "Romanian Male"; break;
        case 'ru': voice = "Russian Female"; break;
        case 'sk': voice = "Slovak Female"; break;
        case 'es': voice = "Spanish Female"; break;
        case 'sv': voice = "Swedish Female"; break;
        case 'ta': voice = "Tamil Male"; break;
        case 'th': voice = "Thai Femalee"; break;
        case 'tr': voice = "Turkish Female"; break;
        case 'af': voice = "Afrikaans Male"; break;
        case 'sq': voice = "Albanian Male"; break;
        case 'bs': voice = "Bosnian Male"; break;
        case 'ca': voice = "Catalan Male"; break;
        case 'hr': voice = "Croatian Male"; break;
        case 'eo': voice = "Esperanto Male"; break;
        case 'is': voice = "Icelandic Male"; break;
        case 'lv': voice = "Latvian Male"; break;
        case 'mk': voice = "Macedonian Male"; break;
        case 'sr': voice = "Serbian Male"; break;
        case 'sw': voice = "Swahili Male"; break;
        case 'vi': voice = "Vietnamese Male"; break;
        case 'cy': voice = "Welsh Male"; break;
    }
    $('#talkVoice').val(voice);
}
