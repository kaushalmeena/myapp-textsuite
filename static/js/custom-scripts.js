function readImage(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            $('#ocrImage').attr('src', e.target.result)
            $('#imageContainer').val(e.target.result);
            $('#alertText').hide();
            $('#imageDiv').show();
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
    $('#buttonLoad').prop('disabled', true);
    $('#imageContainer').val(imageUrl);
    $('#imageDiv').show();
}

function resetImage() {
    $('#imageDiv').hide();
    $("#imageUpload").val("");
    $("#imageContainer").val("");
}

function resetUrl() {
    $('#buttonLoad').prop('disabled', false);
    $('#imageDiv').hide();
    $('#imageUrl').val("");
    $("#imageContainer").val("");
}

function resetText() {
    $("#inputText").val("");
    $('#alertText').hide();
    $('#fromLanguage').val("detect");
    $('#toLanguage').val("en");
}

function checkSubmit(elementID)
{
    var element = $(elementID).val();
    if (element.length) {
        stopCamera();
        $("#inputWidth").val($("#inputGroup").width() - 40);
        return true;
    } else {
        $('#alertText').show();
        return false;
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
        $('#imageContainer').val(data_uri);
        $('#alertText').hide();
        $('#imageDiv').show();
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

function hideAlert()
{
    $('#alertText').hide();    
}

function sendTo(elementID, toLocation) 
{
    var value = $(elementID).val();
    var form = $('<form></form>');
    form.attr("method", "post");
    form.attr("action", toLocation);

    var field = $('<input></input>');
    field.attr("type", "hidden");
    field.attr("name", 'inputText');
    field.attr("value", value);

    form.append(field);
        
    $(form).appendTo('body').submit();
}
