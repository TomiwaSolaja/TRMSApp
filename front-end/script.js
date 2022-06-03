function access_request() {
    let getEmail = document.loginForm.emailField.value;
    let getUser = document.loginForm.employeeField.value;
    let getRequest = document.loginForm.requestField.value;
  
    verify_login(getEmail, getUser, getRequest);
  }
  
  async function verify_login(email, user_id, request_id) {
    const url = `http://localhost:5000/requests`;
    const httpResponse = await fetch(url);
    const body = await httpResponse.json();
  
    console.log("Verifying login credentials...");
    console.log(body);
  }
  
  // async function get_response(url) {
    
  // }
  
  function create_request() {
    console.log("Sending request form to database...");
  }
  
  
  