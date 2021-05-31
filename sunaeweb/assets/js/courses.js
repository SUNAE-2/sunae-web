var stripe;

fetch("./config/")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  stripe = Stripe(data.publicKey);
});

function enroll(name,price) {
    fetch("./create-checkout-session/"+name+"/"+price)
    .then((result) => { return result.json(); })
    .then((data) => {
      console.log(data);
      // Redirect to Stripe Checkout
      return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
    .then((res) => {
      console.log(res);
    });
}