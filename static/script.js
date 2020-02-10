//Fiona Yonkman 2020
//Javascript file that reads and places file to be uploaded from computer

document.getElementById('input-file').addEventListener('change', getFile);

//function that gets .txt file from computer to use for word frequency analysis
function getFile(event) {
	const input = event.target;
  if ('files' in input && input.files.length > 0) {
	  placeFileContent(
      document.getElementById('content-target'),
      input.files[0]);
    getFileName(
      document.getElementById('filename'),
      input.value);
  }
}

//places text from file in textarea HTML element
function placeFileContent(target, file) {
	readFileContent(file).then(content => {
  	target.value = content
  }).catch(error => console.log(error));
}

//sets filename value of HTML hidden input to the filename
function getFileName(target, filename){
  target.value = filename.split(/(\\|\/)/g).pop().split('.')[0];
}

//reads contents of selected .txt file into a string
function readFileContent(file) {
	const reader = new FileReader();
  return new Promise((resolve, reject) => {
    reader.onload = event => resolve(event.target.result);
    reader.onerror = error => reject(error);
    reader.readAsText(file);
  })
}
