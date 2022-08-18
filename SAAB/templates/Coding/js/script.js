const inputs = document.querySelectorAll('.input')

function handlefocus({ target }) {
  const span = target.previousElementSibling
  span.classList.add('span_active')
}

function handlefocusOut ({ target}){

  if(target.value === ''){
    const span = target.previousElementSibling
    span.classList.remove('span_active')
  }

  
  
}

inputs.forEach((input) => input.addEventListener('focus', handlefocus))
inputs.forEach((input) => input.addEventListener('focusout', handlefocusOut))