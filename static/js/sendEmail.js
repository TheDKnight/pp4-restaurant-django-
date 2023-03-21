function sendMail(contactForm) {
    var messageElement = document.getElementById("message"); // get the message element from the HTML

    emailjs.send("service_2alti3j", "template_lktubg3", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "message": contactForm.message.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
            messageElement.innerHTML = "Your message was sent successfully."; // display success message to the user
            contactForm.reset(); // clear the form
        },
        function(error) {
            console.log("FAILED", error);
            messageElement.innerHTML = "There was an error sending your message. Please try again later."; // display error message to the user
        }
    );
    return false; // To block from loading a new page
}