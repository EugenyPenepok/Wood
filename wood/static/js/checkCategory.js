function checkCategory(){
	var header = $('#inputName').val();
	if(header == ''){
		$('#errorMessage').html('Задайте название');
		$('#errorMessage').removeClass('hidden');
		return false;
	}
	else{
		$('#errorMessage').html('');
		$('#errorMessage').addClass('hidden');
	}
	var description = $('#description').val();
	if(description == ''){
		$('#errorMessage').html('Задайте описание');
		$('#errorMessage').removeClass('hidden');
		return false;
	}
	else{
		$('#errorMessage').html('');
		$('#errorMessage').addClass('hidden');
	}
	var image = $('#image').val();
	if (image == ''){
		$('#errorMessage').html('Выберите картинку');
		$('#errorMessage').removeClass('hidden');
		return false;
	}
	else{
		$('#errorMessage').html('');
		$('#errorMessage').addClass('hidden');
	}	
	return true;
}