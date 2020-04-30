function handleUploadError() {
  $('#imageContainer').val('');
  $('#imageFile').val('');
  $('#imageDiv').hide();
  $('#alertText').text("uploaded image is invalid")
  $('#alertDiv').show();
}

function readUpload() {
  var files = $('#imageFile').prop('files');
  var reader = null;
  if (files && files[0]) {
    reader = new FileReader();
    reader.onload = function (e) {
      $('#extractImage').attr('src', e.target.result);
      $('#imageContainer').val(e.target.result);
      $('#imageDiv').show();
      $('#alertDiv').hide();
    };
    reader.onerror = function () {
      $('#imageContainer').val('');
      $('#imageFile').val('');
      $('#imageDiv').hide();
      $('#alertText').text("error occued while reading image")
      $('#alertDiv').show();
    }
    reader.readAsDataURL(files[0]);
  }
}

function resetUpload() {
  $('#imageFile').val('');
  $('#imageContainer').val('');
  $('#fromLanguage').val("detect");
  $('#imageDiv').hide();
  $('#alertDiv').hide();
}

function resetURL() {
  $('#imageURL').val('');
  $('#imageContainer').val('');
  $('#fromLanguage').val("detect");
  $('#imageDiv').hide();
  $('#alertDiv').hide();
}

function checkCapture() {
  var value = $('#imageContainer').val()
  if (value) {
    return true;
  } else {
    $('#alertText').text("please take photo first")
    $('#alertDiv').show();
    return false;
  }
}

function resetCapture() {
  stopCamera()
  $('#imageContainer').val('');
  $('#fromLanguage').val("detect");
  $('#imageDiv').hide();
  $('#alertDiv').hide();
}

var webcamStream = null;

function openCamera() {
  var video = $('#webcamVideo').get(0);
  if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(function (stream) {
        webcamStream = stream
        video.srcObject = stream;
        video.play();
        $('#buttonCamera').prop('disabled', true);
        $('#webcamDiv').show();
      })
      .catch(function (error) {
        $('#imageContainer').val('');
        $('#imageDiv').hide();
        $('#alertText').text('could not access the camera')
        $('#alertDiv').show();
      });
  } else {
    $('#imageContainer').val('');
    $('#imageDiv').hide();
    $('#alertText').text("your machine doesn't support webcam")
    $('#alertDiv').show();
  }
}

function stopCamera() {
  var video = $('#webcamVideo').get(0)
  if (video) {
    video.pause();
    video.src = '';
  }
  if (webcamStream) {
    webcamStream.getTracks()[0].stop();
  }
  $('#webcamDiv').hide();
  $('#buttonCamera').prop('disabled', false);
}

function takePhoto() {
  var canvas = $('#webcamCanvas').get(0);
  var video = $('#webcamVideo').get(0);
  var context = null;
  var data = '';
  if (canvas && video) {
    context = canvas.getContext('2d');
    canvas.height = video.videoHeight;
    canvas.width = video.videoWidth;
    context.drawImage(video, 0, 0);
    data = canvas.toDataURL('image/png');
    $('#imageContainer').val(data);
    $('#imageDiv').show();
    $('#alertDiv').hide();
  } else {
    stopCamera();
    $('#imageContainer').val('');
    $('#imageDiv').hide();
    $('#alertText').text("your machine doesn't support webcam")
    $('#alertDiv').show();
  }
}

function resetText() {
  $('#inputText').val('');
  $('#fromLanguage').val("detect");
  $('#toLanguage').val("en");
  $('#alertDiv').hide();
}

function copyText() {
  $('#outputText').select();
  document.execCommand("copy");
  alert('text copied to clipboard');
}

function hideAlert() {
  $('#alertDiv').hide();
}

function sendTo(id, toLocation) {
  var value = $(id).val();
  $('#hiddenForm').attr("action", toLocation);
  $('#hiddenInput').val(value)
  $('#hiddenForm').submit()
}